import csv

#Class 1
# --------------- FOR Login & Register ---------------#
class Bank:
    def __init__():
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
# --------------- FOR CREATING CHECKING, SAVINGS, OR BOTH ACCOUNTS ---------------#
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


#Class 3
# --------------- FOR CHECK BALANCE ---------------#
class check:
    #Checking account balance
    def checking_account():
        checking_balance = 200
        return checking_balance

    #Savings account balance
    def saving_account():
        saving_balance = 200
        return saving_balance 

# --------------------------------------------------------------#

#Class 4
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
                amount = float(input("Enter the amount: "))
                balance = check.checking_account()
                if amount <= balance:
                    balance -= amount  #To decrease the amount of the account
                    print(f"Withdraw completed successfully, your new checking account balance is: {balance}$")
                    user_input = input("Press 'Enter' to return to main menu ")
                else:
                    print("You don't have this amount of money !!")

            elif user_input == "2":
                print(" -- Savings account withdraw -- ")
                amount = float(input("Enter the amount: "))
                balance = check.checking_account()
                if amount <= balance:
                    balance -= amount  #To decrease the amount of the account
                    print(f"Withdraw completed successfully, your new checking account balance is: {balance}$")
                    user_input = input("Press 'Enter' to return to main menu ")
                else:
                    print("You don't have this amount of money !!")

            elif user_input == "3":
                is_running = False
            else:
                print("Enter a valid choice !!")
# --------------------------------------------#

#Class 5
# --------------- FOR DEPOSIT ---------------#
class Deposit:
    def deposit_money():
        is_running = True
        Bank.login()
        while is_running:
            print("Which account do you want to deposit to?")
            print("1. Checking Account")
            print("2. Savings Account")
            print("3. Back to the past page")
            user_input = input("Enter your choice: ")
            
            if user_input == "1":
                print(" -- Deposit to checking account -- ")
                amount = float(input("Enter the amount: "))
                balance = check.checking_account()
                balance += amount  #To decrease the amount of the account
                print(f"Deposit completed successfully, your new checking account balance is: {balance}$")
                user_input = input("Press 'Enter' to return to main menu ")

            elif user_input == "2":
                print(" -- Deposit to savings account -- ")
                amount = float(input("Enter the amount: "))
                balance = check.checking_account()
                balance += amount  #To decrease the amount of the account
                print(f"Deposit completed successfully, your new checking account balance is: {balance}$")
                user_input = input("Press 'Enter' to return to main menu ")

            elif user_input == "3":
                is_running = False
            else:
                print("Enter a valid choice !!")
        
# -------------------------------------------#

#Class 6
# --------------- FOR TRANSFER ---------------#
class Transfer:
    pass
# --------------------------------------------#

#Class 7
# --------------- FOR OVER DRAFT PROTECTION ---------------#
class overDraftProtection:
    pass
# ---------------------------------------------------------#



# --------------- Main menu Page ---------------#
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
