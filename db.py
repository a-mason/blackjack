def current_money():
    try:
        with open("money.txt") as file:
            money = file.readline()
        return float(money)
    except FileNotFoundError:
        print("File 'money.txt' not found. Creating one with balance of 100.0.")
        with open("money.txt", "w") as file: # create new file
            file.write("100.0")
        return float(100) # default starting money if the file isn't found
    
def update_money(bet, win):
    money = current_money()
    
    if win:
        print()
        print("Congrats! You won!")
        new_money = str(round(money + (bet * 1.5)))
        with open("money.txt", "w") as file:
            file.write(new_money)

    else:
        print()
        print("Sorry. You lose.")
        new_money = str((money - bet))
        with open("money.txt", "w") as file:
            file.write(new_money)

    print(f"Money: {new_money}")
    return new_money

def buy_more(bet):
    while True:
        try:
            amount = float(input("How many chips would you like to purchase?: "))
            break
        except ValueError:
            print("Purchase amount must be valid number, please try again")
    
    new_amount = amount + bet
    print(f"Purchase successful, your new balance is: {new_amount}")
    
    with open("money.txt", "w") as file: # overwrite with updated amount
            file.write(f"{new_amount}")

    return float(new_amount)


