import csv

#Class 1
# --------------- FOR Login & Register ---------------#
class Bank:
    def __init__(self, username):
        username = username

        
    def login():
        username = input("Username: ").lower()
        password = input("Password: ")
        print(f"\n\nWelcome back {username} !!")
        
    def register():
        username = input("Username: ").lower()
        password = input("Password: ")
        print(f"\nWelcome {username}!!, Your account created successfully")
        user_input = input("Press 'Enter' to return to main menu ")


# ------------------------------------------------------#

#Class 2
# --------------- FOR CHECKING, SAVINGS, OR BOTH ---------------#
class AddNewCustomer:
    def createAccounts_page():
        is_running = True
        while is_running:
            print("\n Hello")
            print("1. Create checking account")
            print("2. Create savings account")
            print("3. Exit")
            user_input = input("Enter your choice: ")
            if user_input == "1":
                AddNewCustomer.create_checking_account()
            elif user_input == "2":
                AddNewCustomer.create_saving_account()
            elif user_input =="3":
                is_running = False
            else: print("Enter a valid choice !!")
    
    
    #To create checking account
    def create_checking_account():
        print("Your checking account created successfully")
        user_input = input("Press 'Enter' to return to main menu ")

    #To create savings account
    def create_saving_account():
        print("Your saving account created successfully")
        user_input = input("Press 'Enter' to return to main menu ")

    #Checking account balance
    def checking_account(amount):
        checking_balance = 0

    #Savings account balance
    def saving_account():
        saving_balance = 0

# --------------------------------------------------------------#

#Class 3
# --------------- FOR WITHDRAW ---------------#
class Withdraw:
    def withdraw_money():
        is_running = True
        Bank.login()
        while is_running:
            print("Which account do you want to withdraw from?")
            print("1. Checking Account")
            print("2. Savings Account")
            print("3. Back to the past page")
            user_input = input("Enter your choice: ")
            if user_input == "1":
                print(" -- Checking account withdraw -- ")
                user_input = input("Enter the amount: ")
                amount = int(user_input)
                amount -= AddNewCustomer.checking_account() #To decrease the amount of the account
            elif user_input == "2":
                print(" -- Savings account withdraw -- ")
                user_input = input("Enter the amount: ")
                amount = int(user_input)
                amount -= AddNewCustomer.saving_account() #To decrease the amount of the account
            elif user_input == "3":
                is_running = False
            else:
                print("Enter a valid choice !!")
# --------------------------------------------#

#Class 4
# --------------- FOR DEPOSIT ---------------#
class Deposit:
    def deposit_money():
        is_running = True
        Bank.login()
        while is_running:
            print("Which account do you want to Deposit to?")
            print("1. Checking Account")
            print("2. Savings Account")
            print("3. Back to the past page")
            user_input = input("Enter your choice: ")
            if user_input == "1":
                print("-- Checking account deposit --")
                user_input = input("Enter the amount: ")
                user_input += AddNewCustomer.checking_account() #To increase the amount of the account
            elif user_input == "2":
                print("-- Savings account deposit -- ")
                user_input = input("Enter the amount: ")
                user_input += AddNewCustomer.saving_account() #To increase the amount of the account
            elif user_input == "3":
                is_running = False
            else:
                print("Enter a valid choice !!")
# -------------------------------------------#

#Class 5
# --------------- FOR TRANSFER ---------------#
class Transfer:
    pass
# --------------------------------------------#

#Class 6
# --------------- FOR OVER DRAFT PROTECTION ---------------#
class overDraftProtection:
    pass
# ---------------------------------------------------------#



# --------------- Start Page ---------------#
def main():
    is_running = True
    while is_running:
        print("\n\n======================")
        print("Welcome to the Bank :)")
        print("======================")
        print("1: Withdraw")
        print("2: Deposit")
        print("3: Transfer")
        print("4: Create checking & savings accounts")
        print("5: Register main account")
        print("6: Exit")
        user_input = input("Enter your choice: ")
        if user_input == "1":
            Withdraw.withdraw_money()
        elif user_input == "2":
            Deposit.deposit_money()
        elif user_input == "3":
            Transfer
        elif user_input == "4":
            AddNewCustomer.createAccounts_page()
        elif user_input == "5":
            Bank.register()
        elif user_input == "6":
            is_running = False
        else: print("Enter a valid choice !!")
    print("Have a good day sir ;)")
# # -----------------------------------------#

main()
