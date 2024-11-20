import random

def generate_deck():
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["♠", "♥", "♦", "♣"]
    deck = [[rank, suit] for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def draw_card(deck):
    card = random.choice(deck)
    rank, suit = card
    return card

def card_value(card):
    rank, suit = card
    if rank in ["J", "Q", "K"]: #assign 10 if rank is face card
        return 10
    elif rank == "A":
        return 11  #assign 11 if rank is ace
    else:
        return int(rank)
