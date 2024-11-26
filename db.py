def current_money():
    with open("money.txt") as file:
        money = file.readline()
    return float(money)

def update_money(bet, win):
    money = current_money()
    
    if win:
        print()
        print("Congrats! You won!")
        new_money = str(money + (bet * 1.5))
        with open("money.txt", "w") as file:
            file.write(new_money)

    else:
        print()
        print("Sorry. You lose.")
        new_money = str(money - bet)
        with open("money.txt", "w") as file:
            file.write(new_money)

    print(f"Money: {new_money}")
    return new_money

