import random

def generate_deck():
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["♠", "♥", "♦", "♣"]
    deck = [[rank, suit] for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def draw_card(deck): # draws card from top of deck
    card = deck.pop()
    rank, suit = card
    return card

def card_value(rank, total, dealers_turn):
    if rank in ["J", "Q", "K"]: # assign 10 if rank is face/court card
        return 10
    elif rank == "A": # assign 11 to ace unless total would go over 21, then assign 1
        if dealers_turn == True:
            if total + 11 > 21:
                return 1
            else:
                return 11
        if dealers_turn == False:
            if total + 11 > 21:
                return 1
            else:
                choice = choose_ace()
                return choice
    else:
        return int(rank)


def choose_ace():
    while True:
        try:
            print()
            choice = int(input("You've drawn an Ace, would you like to count it as 1 or 11? "))
            if choice == 1:
                return 1
            elif choice == 11:
                return 11
            else:
                print("Invalid choice. Please choose 1 or 11.")
        except ValueError:
            print("Invalid choice. Please choose 1 or 11.")
