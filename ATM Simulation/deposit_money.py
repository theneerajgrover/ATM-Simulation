import util
from datetime import datetime

def deposit() :
    amount = int(input("ENTER AMOUNT YOU WANT TO DEPOSIT : "))
    if amount > 0 :
        util.history.append(f"Deposited {amount}Rs at {datetime.now()}")
        print("You have credited", amount, "Rs in your account at", datetime.now())
        util.balance += amount
    else :
        print("Invalid Input.")