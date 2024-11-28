import deckofcards
import heldcards
import db
import sys

def title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")

def player_hand(deck, bet):
    player_cards = [] # list that record the rank and suit of cards drawn
    player_ranks = [] # list that records the rank of cards drawn

    for starting_cards in range(2): # draws two starting cards for player and displays them
        hit(player_cards, player_ranks, deck)
    heldcards.show_player(player_cards)

    while True:
        total = sum(player_ranks)
        stand = input("Hit or stand? (hit/stand): ").lower()
        if stand == "stand":
            return total
            break
        else:
            hit(player_cards, player_ranks, deck)
            total = sum(player_ranks)
            if total > 21: # player loses
                print("Bust!")
                return total 
            elif total == 21: # player wins 
                print("Blackjack!")
                return total 
          

def dealer_hand(deck, dealer_cards, dealer_ranks, player_total):
    total = sum(dealer_ranks)

    if player_total >= 21: # skip the function if player got blackjack or busts
        return total
    
    else:
        while total < 17: # dealer draws until at least 17 points
            rank, suit = deckofcards.draw_card(deck)
            dealer_cards.append([rank, suit])
            rank = deckofcards.card_value(rank, total, True)
            dealer_ranks.append(int(rank))
            total = sum(dealer_ranks) # reassign total in loop to avoid infinite looping

            if total > 21:
                print("Dealer busts!")
                heldcards.show_dealer(dealer_cards)
                return total  # dealer loses if cards total more than 21
            elif total == 21:
                print("Dealer blackjack!")
                heldcards.show_dealer(dealer_cards)
                return total  # dealer wins if cards equal 21
            else:
                print("Dealer stands.")
                heldcards.show_dealer(dealer_cards)
                return total  # dealer stands
            
def show_card(deck):
    print("DEALER'S SHOW CARD:")
    dealer_cards = []
    dealer_ranks = []

    rank, suit = deckofcards.draw_card(deck)
    print(f"+-----+\n|{rank.ljust(2)}   |\n|  {suit}  |\n|   {rank.rjust(2)}|\n+-----+")

    dealer_cards.append([rank, suit])
    rank = deckofcards.card_value(rank, 0, True) # total is zero
    dealer_ranks.append(int(rank))
    
    return dealer_cards, dealer_ranks
    
def hit(player_cards, player_ranks, deck):
    total = sum(player_ranks)
    rank, suit = deckofcards.draw_card(deck) 
    player_cards.append([rank, suit])
    rank = deckofcards.card_value(rank, total, False)
    player_ranks.append(int(rank))
    if len(player_cards) >= 3: # avoids showing cards multiple times during starting cards
        heldcards.show_player(player_cards)

def print_totals(player_total, dealer_total):
    print()
    print(f"YOUR POINTS: {player_total}")
    print(f"DEALER'S POINTS: {dealer_total}")
    
    
    
def main():
    title()
    
    while True: # begins game
        print()
        money = db.current_money()
        deck = deckofcards.generate_deck() # generates shuffled deck
        print(f"Money: {money}") # display player's current money value
        
        while True:  # loop until a valid bet is entered
            if money < 5:
                buy_chips = input("You have under 5 chips, would you like to purchase more (y/n)?: ").lower() 
                if buy_chips == "y": # buy more chips
                    money = db.buy_more(money)
                else:
                    print("You're unable to play with under 5 chips.")
                    print("Please come back when you have more.")
                    sys.exit()
                
            try:
                bet = float(input("Bet amount: "))  # player inputs bet amount
                if bet > money:
                    print("You cannot afford to bet that much, please bet again.")
                elif bet < 5:
                    print("Minimum bet is 5, please bet again.")
                elif bet > 1000:
                    print("Maximum bet is 1000, please bet again.")
                else:
                    break
            except ValueError:
                print("Bet must be a valid number.")
        print()

        dealer_cards, dealer_ranks = show_card(deck)
        player_total = player_hand(deck, bet)
        dealer_total = sum(dealer_ranks) # gets dealer's total incase player wins
        
        if player_total >= 21:  # if player blackjack or busts, skip the dealer's turn
            if player_total == 21: # blackjack
                heldcards.show_dealer(dealer_cards)
                print_totals(player_total, dealer_total)
                db.update_money(bet, True)
            else: # bust
                heldcards.show_dealer(dealer_cards)
                print_totals(player_total, dealer_total)
                db.update_money(bet, False)
        
        elif player_total < 21: # if player stands under 21, dealer draws cards
            dealer_total = dealer_hand(deck, dealer_cards, dealer_ranks, player_total)
            if dealer_total == 21: # dealer blackjack, player loses
                heldcards.show_dealer(dealer_cards)
                print_totals(player_total, dealer_total)
                db.update_money(bet, False)
            elif dealer_total > 21: # dealer bust, player wins
                heldcards.show_dealer(dealer_cards)
                print_totals(player_total, dealer_total)
                db.update_money(bet, True)
            else:  # if neither player or dealer busts, compare totals to determine winner
                if player_total > dealer_total:
                    print("Player wins!")
                    heldcards.show_dealer(dealer_cards)
                    print_totals(player_total, dealer_total)
                    db.update_money(bet, True)
                elif dealer_total > player_total:
                    print("Dealer wins!")
                    heldcards.show_dealer(dealer_cards)
                    print_totals(player_total, dealer_total)
                    db.update_money(bet, False)
                else:
                    heldcards.show_dealer(dealer_cards)
                    print_totals(player_total, dealer_total)
                    print("Player and Dealer's hands equal the same value, it's a tie!")

        print()
        again = input("Play again? (y/n): ").lower() # player chooses to play again or end
        if again != "y":
            print()
            print("Come back soon!")
            print("Bye!")
            sys.exit()

        
if __name__ == "__main__":
    main()
