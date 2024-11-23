import random

def generate_deck():
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["♠", "♥", "♦", "♣"]
    deck = [[rank, suit] for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def draw_card(deck):
    card = deck.pop()
    rank, suit = card
    print("Drawn card:") # show a visual for drawn card
    print(f"+-----+\n|{rank.ljust(2)}   |\n|  {suit}  |\n|   {rank.rjust(2)}|\n+-----+")
    return card

def card_value(card):
    if rank in ["J", "Q", "K"]: # assign 10 if rank is face card
        return 10
    elif rank == 'A': # assign 1 or 11 if rank is ace
        while True:
            try:
                choice = int(input("You've drawn an Ace, would you like to count it as 1 or 11? "))
                if choice == 1:
                    return 1
                elif choice == 11:
                    return 11
                else:
                   print("Invalid choice. Please choose 1 or 11.") 
            except ValueError:
                print("Invalid choice. Please choose 1 or 11.")
    else:
        return int(rank)
