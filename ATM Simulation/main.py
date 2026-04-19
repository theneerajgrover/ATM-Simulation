from display_balance import display
from withdraw_money import withdraw
from deposit_money import deposit
from statement import record

def atm() :
    while True :
        print("\n1. Display Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Bank Statement")
        print("5. Exit")
        choice = int(input("ENTER YOUR CHOICE : "))
        
        if choice == 1:       display()
        elif choice == 2:     withdraw()
        elif choice == 3:     deposit()
        elif choice == 4:     record()
        elif choice == 5:
            print("THANKYOU !!")
            break
        else :
            print("INVALID CHOICE !!")
            print("ENTER YOUR CHOICE AGAIN !!")
atm()