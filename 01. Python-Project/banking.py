import csv

#Class 1
# --------------- FOR Login & Register ---------------#
class Bank:
    def __init__():
        username = username

    #For Login
    def login():
        username = input("Username: ").lower()
        password = input("Password: ")
        print(f"\n\nWelcome back {username} !!")
    
    #For register
    def register():
        username = input("Username: ").lower()
        password = input("Password: ")
        print(f"\nWelcome {username}!!, Your account created successfully ✅")
        user_input = input("Press 'Enter' to return to main menu 🔙 ")

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
            
            #For Choice 1
            if user_input == "1":
                AddNewCustomer.create_checking_account()
            
            #For Choice 2
            elif user_input == "2":
                AddNewCustomer.create_saving_account()
            
            #For exiting
            elif user_input =="3":
                is_running = False
                
            #If user enter a choice not on the list
            else: print("Enter a valid choice !!")


    #To create checking account
    def create_checking_account():
        print("Your checking account created successfully✅")
        user_input = input("Press 'Enter' to return to main menu 🔙 ")

    #To create savings account
    def create_saving_account():
        print("Your saving account created successfully✅")
        user_input = input("Press 'Enter' to return to main menu 🔙 ")


#Class 3
# --------------- FOR CHECK BALANCE ---------------#
class check:
    #Check for Checking account balance
    def checking_account():
        checking_balance = 200
        return checking_balance

    #Check for Savings account balance
    def saving_account():
        saving_balance = 35
        return saving_balance 

# --------------------------------------------------------------#

#Class 4
# --------------- FOR WITHDRAW ---------------#
class Withdraw:
    def withdraw_money():
        is_running = True
        Bank.login()
        while is_running:
            print("💰Which account do you want to withdraw from?💰")
            print("1️⃣. Checking Account ")
            print("2️⃣. Savings Account")
            print("3️⃣. Back to the past menu🔙")
            user_input = input("Enter your choice: ")
            
            #For Choice 1
            if user_input == "1":
                print("\n\n -- Checking account withdraw -- ")
                amount = float(input("Enter the amount💲: "))
                balance = check.checking_account()
                
                if amount <= balance:
                    balance -= amount  #To decrease the amount from balance account
                    print(f"Withdraw completed successfully✅, your new checking account balance is: {balance}$💵")
                    user_input = input("Press 'Enter' to return to withdraw menu📃 ")
                else:
                    print("You don't have this amount of money ❌!!")

            #For Choice 2
            elif user_input == "2":
                print("\n\n -- Savings account withdraw -- ")
                amount = float(input("Enter the amount💲: "))
                balance = check.saving_account()
                if amount <= balance:
                    balance -= amount  #To decrease the amount from balance account
                    print(f"Withdraw completed successfully✅, your new saving account balance is: {balance}$")
                    user_input = input("Press 'Enter' to return to withdraw menu📃 ")
                else:
                    print("You don't have this amount of money ❌!!")

            #For exiting
            elif user_input == "3":
                is_running = False

            #If user enter a choice not on the list
            else:
                print("Enter a valid choice !!")
# --------------------------------------------#

#Class 5
# ------------------------------ FOR DEPOSIT ------------------------------#
class Deposit:
    def deposit_money():
        is_running = True
        Bank.login()
        while is_running:
            print("Which account do you want to deposit to?")
            print("1️⃣. Checking Account")
            print("2️⃣. Savings Account")
            print("3️⃣. Back to the past menu🔙")
            user_input = input("Enter your choice: ")
            
            #For Choice 1
            if user_input == "1":
                print(" -- Deposit to checking account -- ")
                amount = float(input("Enter the amount💲: "))
                balance = check.checking_account()
                balance += amount  #To increase the amount of the account
                print(f"Deposit completed successfully✅, your new checking account balance is: {balance}$")
                user_input = input("Press 'Enter' to return to deposit menu📃 ")
                
            #For Choice 2
            elif user_input == "2":
                print(" -- Deposit to savings account -- ")
                amount = float(input("Enter the amount💲: "))
                balance = check.saving_account()
                balance += amount  #To increase the amount of the account
                print(f"Deposit completed successfully✅, your new saving account balance is: {balance}$")
                user_input = input("Press 'Enter' to return to deposit menu📃 ")
                
            #For exiting
            elif user_input == "3":
                is_running = False
            
            #If user enter a choice not on the list
            else:
                print("Enter a valid choice !!")
        
# -------------------------------------------------------------------------------------#

#Class 6
# -------------------------- FOR TRANSFER --------------------------#
class Transfer:
    #To select which account you want to transfer from
    def transfer_from():
        is_running = True
        Bank.login()
        while is_running:
            print("\n-------- Transfer --------")
            print("** 💸Which account do you want to transfer from?💸 **")
            print("1️⃣. Checking Account")
            print("2️⃣. Savings Account")
            print("3️⃣. Back to the past menu🔙")
            user_input = input("Enter your choice: ")
            
            #For Choice 1
            if user_input == "1":
                Transfer.transfer_one()
            
            #For Choice 2
            elif user_input == "2":
                Transfer.transfer_two()
            
            #For exiting
            elif user_input == "3":
                is_running = False
            
            #If user enter a choice not on the list
            else:
                print("Enter a valid choice !!")

#---------------------------------------------------------------------#

    #If you select to transfer from Checking account:
    def transfer_one():
        is_running = True
        while is_running:
            #Now you should select which account you will transfer to:
            print("\n\n## Which account do you want to transfer to? ##")
            print("1️⃣. Savings Account")
            print("2️⃣. Customer's Account")
            print("3️⃣. Back to the past menu🔙")
            user_input = input("Enter your choice: ")

            #For Choice  1 < from Checking account to Savings account:
            if user_input == "1":
                print("\n\nNow you will transfer money from your 'Checking' to 'Savings' account")
                amount = float(input("Enter the amount💲: "))
                CheckingBalance = check.checking_account()
                SavingsBalance = check.saving_account()
                
                if amount <= CheckingBalance:
                    CheckingBalance -= amount
                    SavingsBalance += amount
                    print(f"Transfer completed✅,\n[your Savings account balance is {SavingsBalance}$💵 .]\n[your Checking account balance is {CheckingBalance}$💸 .]\n")
                    user_input = input("Press 'Enter' to return to transfer to menu📃 ")

                #If the balance of the account you want to transfer from is less than the amount you put:
                elif amount > CheckingBalance:
                    print("You don't have this amount of money ❌!!")
                
                #If user enter a choice not on the list
                else:
                    print("Enter a valid choice !!")

#-------------------------------------------------------------------------------------------------------------------------------------------#

            #For Choice 2 < from Checking account to customer's account:
            if user_input == "2":
                print("\n\nNow you will transfer money from your 'Checking' to 'Customer's' account")
                user_input = (input("Enter the customer ID: "))
                amount = float(input("Enter the amount💲: "))
                CheckingBalance = check.checking_account()

                if amount <= CheckingBalance:
                    CheckingBalance -= amount
                    print(f"Transfer completed, your Checking account balance is {CheckingBalance} 💵")
                    user_input = input("Press 'Enter' to return to transfer to menu📃 ")

                #If the balance of the account you want to transfer from is less than the amount you put:
                elif amount > CheckingBalance:
                    print("You don't have this amount of money ❌!!")

            #For exiting
            if user_input == "3":
                is_running = False

            #If user enter a choice not on the list
            else:
                print("Enter a valid choice !!")

# ----------------------------------------------------------------------------#

    #If you select to transfer from Savings account:
    def transfer_two():
        is_running = True
        while is_running:
            print("\n\n## Which account do you want to transfer to? ##")
            print("1️⃣. Checking Account")
            print("2️⃣. Customer's Account")
            print("3️⃣. Go to the past menu")
            user_input = input("Enter your choice: ")

            #For Choice 1 < from Savings account to Checking account:
            if user_input == "1":
                print("\n\nNow you will transfer money from your 'Savings' to 'Checking' account")
                amount = float(input("Enter the amount💲: "))
                CheckingBalance = check.checking_account()
                SavingsBalance = check.saving_account()

                if amount <= SavingsBalance:
                    CheckingBalance += amount
                    SavingsBalance -= amount
                    print(f"Transfer completed✅,\n[your Checking account balance is {CheckingBalance}$💵 .]\n[your Savings account balance is {SavingsBalance}$💸 .]\n")
                    user_input = input("Press 'Enter' to return to transfer to menu📃 ")

                #If the balance of the account you want to transfer from is less than the amount you put:
                elif amount > CheckingBalance:
                    print("You don't have this amount of money ❌!!")

#----------------------------------------------------------------------------------------------------------------------------------#

            #For Choice 2 < from Savings account to Customer's account:
            elif user_input == "2":
                print("\n\nNow you will transfer money from your 'Savings' to 'Customer's' account")
                user_input = (input("Enter the customer ID: "))
                amount = float(input("Enter the amount💲: "))
                SavingsBalance = check.saving_account()
                
                if amount <= SavingsBalance:
                    SavingsBalance -= amount
                    print(f"Transfer completed✅, your Savings account balance {SavingsBalance}$")
                    user_input = input("Press 'Enter' to return to transfer to menu📃 ")

                #If the balance of the account you want to transfer from is less than the amount you but:
                elif amount > SavingsBalance:
                    print("You don't have this amount of money ❌!!")

            #For exiting
            elif user_input == "3":
                is_running = False

            #If user enter a choice not on the list
            else:
                print("Enter a valid choice!!")

# --------------------------------------------------------------------------------------------------------------------------------#

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
        print("1️⃣: Withdraw")
        print("2️⃣: Deposit")
        print("3️⃣: Transfer")
        print("4️⃣: Create checking & savings accounts")
        print("5️⃣: Register main account")
        print("6️⃣: Exit")
        user_input = input("Enter your choice: ")
        if user_input == "1":
            Withdraw.withdraw_money()
        elif user_input == "2":
            Deposit.deposit_money()
        elif user_input == "3":
            Transfer.transfer_from()
        elif user_input == "4":
            AddNewCustomer.createAccounts_page()
        elif user_input == "5":
            Bank.register()
        elif user_input == "6":
            is_running = False
        else: print("Enter a valid choice !!")
    print("Have a good day sir 😉")
# # -----------------------------------------#

main()
