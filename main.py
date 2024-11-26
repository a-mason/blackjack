import deckofcards
import heldcards
import db

def title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()

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
          

def dealer_hand(deck, dealer_cards, dealer_ranks):
    total = sum(dealer_ranks)
    while total < 17: # dealer draws until at least 17 points
        rank, suit = deckofcards.draw_card(deck)
        dealer_cards.append([rank, suit])
        rank = deckofcards.card_value(rank, total, True)
        dealer_ranks.append(int(rank))
        total = sum(dealer_ranks) # reassign total in loop to avoid infinite looping

        
        if total > 21:
            print("Dealer bust, player wins!")
            db.update_money(bet, True)
            return total  # dealer loses if cards total more than 21
        elif total == 21:
            print("Dealer blackjack!")
            db.update_money(bet, False)
            return total  # dealer wins if cards equal 21
        else:
            print("Dealer stands.")
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
    
    
def main():
    title()
    money = db.current_money()         
    print(f"Money: {money}") # display player's current money value
    bet = float(input("Bet amount: ")) # player inputs bet amount
    print()
    deck = deckofcards.generate_deck() # generates shuffled deck
    dealer_cards, dealer_ranks = show_card(deck)
    
    while True:
        player_total = player_hand(deck, bet)
        
        if player_total >= 21:  # if player blackjack or busts, skip the dealer's turn
            if player_total == 21: # blackjack
                print()
                print(f"YOUR POINTS: {player_total}")
                print(f"DEALER'S POINTS: {sum(dealer_ranks)}") # prints as sum to avoid square brackets
                db.update_money(bet, True)
            else: # bust
                print()
                print(f"YOUR POINTS: {player_total}")
                print(f"DEALER'S POINTS: {sum(dealer_ranks)}") # prints as sum to avoid square brackets
                db.update_money(bet, False)
        
        elif player_total < 21: # if player stands under 21, dealer draws cards
            dealer_total = dealer_hand(deck, dealer_cards, dealer_ranks)
            print()
            print(f"YOUR POINTS: {player_total}")
            print(f"DEALER'S POINTS: {dealer_total}")

        else:  # if neither player or dealer busts, compare totals to determine winner
            if player_total > dealer_total:
                print("Player wins!")
                db.update_money(bet, True)
            elif dealer_total > player_total:
                print("Dealer wins!")
                db.update_money(bet, False)
            else:
                print("Player and Dealer's hands equal the same value, it's a tie!")

        print()
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print()
            print("Come back soon!")
            print("Bye!")
            break

        
if __name__ == "__main__":
    main()
