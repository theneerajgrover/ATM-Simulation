import util
from datetime import datetime

def withdraw () :
    amount = int(input("ENTER AMOUNT YOU WANT TO WITHDRAW : "))
    if amount <= util.balance :
        util.history.append(f"Withdrawn {amount}Rs at {datetime.now()}")
        print("You have debited", amount,"Rs from your account at", datetime.now())
        util.balance -= amount
    else :
        print("Insufficient Balance.")