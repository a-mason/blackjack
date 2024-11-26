# code to print cards in hand as ASCII art

def show_player(player_cards):
    row = []
    leftrank_row = []
    middle_row = []
    rightrank_row = []

    print()
    print("YOUR CARDS:")
    for rank, suit in player_cards:
        row.append("+-----+")
        leftrank_row.append(f"|{rank.ljust(2)}   |")
        middle_row.append(f"|  {suit}  |")
        rightrank_row.append(f"|   {rank.rjust(2)}|")

    # use asterik to unpack lists and print as a single line
    print(*row)
    print(*leftrank_row)
    print(*middle_row)
    print(*rightrank_row)
    print(*row)

def show_dealer(dealer_cards):
    row = []
    leftrank_row = []
    middle_row = []
    rightrank_row = []

    print()
    print("DEALER'S CARDS:")
    for rank, suit in dealer_cards:
        row.append("+-----+")
        leftrank_row.append(f"|{rank.ljust(2)}   |")
        middle_row.append(f"|  {suit}  |")
        rightrank_row.append(f"|   {rank.rjust(2)}|")

    print(*row)
    print(*leftrank_row)
    print(*middle_row)
    print(*rightrank_row)
    print(*row)

