import csv

checking = False
savings = False
active = True
overdraft_count = 0

fieldnames = [
    'id',
    'username',
    'password',
    'checking',
    'savings',
    'overdraft_count'
]


#Class 1
# --------------- FOR Login & Register ---------------#
class Bank:
    # def __init__():
    #     username = username
        
    users = []
    logged_user = None
    
    def save_users():
        with open('/home/majedyalmalki/code/PythonBankProject/01. Python-Project/bank.csv', mode='w', newline='') as write_file:
            writer = csv.DictWriter(write_file, fieldnames=fieldnames)
            writer.writeheader()
            for user in Bank.users:
                writer.writerow(user)
    
    def load_users():
        with open('/home/majedyalmalki/code/PythonBankProject/01. Python-Project/bank.csv', mode='r', newline='') as read_file:
            reader = csv.DictReader(read_file)
            for row in reader:
                Bank.users.append(row)
    #For Login
    def login():
        while True:
            username = input("Username: ").lower()
            password = input("Password: ")
            for user in Bank.users:
                if username == user['username'] and password == user["password"]:
                    Bank.logged_user = user
                    return print(f"\n\nWelcome back {username} 👋!!")
            else:
                print("Wrong username or password !!\n")
                continue
    
    #For register
    def register():
        username = input("Username: ").lower()
        password = input("Password: ")
        id = 1000  

        with open("/home/majedyalmalki/code/PythonBankProject/01. Python-Project/bank.csv", 'r') as read_file:
            reader = csv.DictReader(read_file)
            existing_ids = [int(row['id']) for row in reader]
            if existing_ids:
                id = max(existing_ids) + 1  

        user_data = {
            'id': id,
            'username': username,
            'password': password,
            'checking': checking,
            'savings': savings,
            'overdraft_count': overdraft_count
        }

        with open("/home/majedyalmalki/code/PythonBankProject/01. Python-Project/bank.csv", 'a', newline='') as write_file:
            writer = csv.DictWriter(write_file, fieldnames=fieldnames)
            writer.writerow(user_data)
        Bank.load_users()

        print("\nUser registered successfully!✅😊")
        user_input = input("Press 'Enter' to return to main menu 🔙 ")

# ---------------------------------------------------------------------------------#




#Class 2
# --------------- FOR CREATING CHECKING, SAVINGS, OR BOTH ACCOUNTS ---------------#
class AddNewCustomer:
    def createAccounts_page():
        is_running = True
        while is_running:
            print("\n\n## Which account do you want to create? ##")
            print("1. Create checking account")
            print("2. Create savings account")
            print("3. Create both accounts (Checking & savings)")
            print("4. Exit")
            user_input = input("Enter your choice: ")
            
            #For Choice 1
            if user_input == "1":
                AddNewCustomer.create_checking_account()
            
            #For Choice 2
            elif user_input == "2":
                AddNewCustomer.create_saving_account()

            #For Choice 3
            elif user_input == "3":
                AddNewCustomer.creating_both_accounts()
            
            #For exiting
            elif user_input =="4":
                is_running = False
                
            #If user enter a choice not on the list
            else: print("Enter a valid choice !!")



    #To create checking account
    def create_checking_account():
        if Bank.logged_user["checking"] == "False":
            Bank.logged_user["checking"] = 0
            print("\nYour checking account created successfully✅")
            Bank.save_users()
        else:
            print("You already have an account !!!")
        user_input = input("Press 'Enter' to return to creating menu 🔙 ")



    #To create savings account
    def create_saving_account():
        if Bank.logged_user["savings"] == "False":
            Bank.logged_user["savings"] = 0
            print("\nYour Savings account created successfully✅")
            Bank.save_users()
        else:
            print("You already have an account !!!")
            user_input = input("Press 'Enter' to return to creating menu 🔙 ")



    #To create both checking and savings account
    def creating_both_accounts():
        if Bank.logged_user["checking"] == "False" and Bank.logged_user["savings"] == "False":
            Bank.logged_user["checking"] = 0
            Bank.logged_user["savings"] = 0
            print("\nYour checking & savings account has created successfully✅")
            Bank.save_users()
            user_input = input("Press 'Enter' to return to creating menu 🔙 ")
        else:
            print("You have account already")
            user_input = input("Press 'Enter' to return to creating menu 🔙 ")




#Class 3
# ---------------------- FOR CHECK BALANCE ----------------------#
class check:
    #Check for Checking account balance
    def checking_account():
        return Bank.logged_user["checking"]

    #Check for Savings account balance
    def saving_account():
        return Bank.logged_user["savings"]

# ---------------------------------------------------------------#





#Class 4
# ------------------------ FOR WITHDRAW ------------------------#
class Withdraw:
    def withdraw_money():
        is_running = True
        while is_running:
            print("\n💰Which account do you want to withdraw from?💰")
            print("1️⃣. Checking Account ")
            print("2️⃣. Savings Account")
            print("3️⃣. Back to the past menu🔙")
            user_input = input("Enter your choice: ")
            
            
# --------- #For withdraw from Checking account:-----------#
            if user_input == "1":
                if Bank.logged_user["checking"] == "False":
                    print("\n***You don't have checking account*** !!!")
                    continue
                else:
                    print("\n\n -- Checking account withdraw -- ")
                    amount = float(input("Enter the amount💲: "))
                    current_checking_balance = float(Bank.logged_user["checking"])
                
                if amount > 100:
                    print("You cannot withdraw more than 100$ !!\n")
                #------------------------ Overdraft ----------------------------#
                if current_checking_balance <= 0:
                    overdraft_decrease = 35
                    Bank.logged_user["checking"] = current_checking_balance - amount - overdraft_decrease
                    Bank.logged_user["overdraft_count"] =int(Bank.logged_user["overdraft_count"]) + 1
                    updated_checking_balance = check.checking_account()
                    print(f"35$ overdraft, your new account balance is: {updated_checking_balance}")
                    Bank.save_users()
                    user_input = input("Press 'Enter' to return to withdraw menu📃 ")
                #--------------------------------------------------------------------------#

                elif amount <= current_checking_balance:
                    Bank.logged_user["checking"] = current_checking_balance - amount  #To decrease the amount from balance account
                    updated_checking_balance = check.checking_account()
                    print(f"Withdraw completed successfully✅, your new checking account balance is: {updated_checking_balance}$💵")
                    Bank.save_users()
                    user_input = input("Press 'Enter' to return to withdraw menu📃 ")
                else:
                    print("You don't have this amount of money ❌!!")
# -------------------------------------------------------------------------------------------#




# -------------------------- For withdraw from Savings account: ------------------------------#
            elif user_input == "2":
                if Bank.logged_user["savings"] == "False":
                    print("\n***You don't have savings account*** !!!")
                    continue
                else:
                    print("\n\n -- Savings account withdraw -- ")
                    amount = float(input("Enter the amount💲: "))
                    current_savings_balance = float(Bank.logged_user["savings"])
                if amount > 100:
                    print("You cannot withdraw more than 100$ !!\n")

                #------------------------ Overdraft ----------------------------#
                elif current_savings_balance <= 0:
                    overdraft_decrease = 35
                    Bank.logged_user["savings"] = current_savings_balance - amount - overdraft_decrease
                    Bank.logged_user["overdraft_count"] =int(Bank.logged_user["overdraft_count"]) + 1
                    updated_savings_balance = check.saving_account()
                    print(f"35$ overdraft, your new account balance is: {updated_savings_balance}")
                    Bank.save_users()
                    user_input = input("Press 'Enter' to return to withdraw menu📃 ")
                #--------------------------------------------------------------------------#


                elif amount <= current_savings_balance:
                    Bank.logged_user["savings"] = current_savings_balance - amount  #To decrease the amount from balance account
                    updated_savings_balance = check.saving_account()
                    print(f"Withdraw completed successfully✅, your new saving account balance is: {updated_savings_balance}$")
                    Bank.save_users()
                    user_input = input("Press 'Enter' to return to withdraw menu📃 ")
                else:
                    print("You don't have this amount of money ❌!!")

            #For exiting
            elif user_input == "3":
                is_running = False

            #If user enter a choice not on the list
            else:
                print("Enter a valid choice !!")
# --------------------------------------------------------------------------------------#




#Class 5
# ------------------------------------ FOR DEPOSIT -------------------------------------#
class Deposit:
    def deposit_money():
        is_running = True
        while is_running:
            print("\nWhich account do you want to deposit to?")
            print("1️⃣. Checking Account")
            print("2️⃣. Savings Account")
            print("3️⃣. Back to the past menu🔙")
            user_input = input("Enter your choice: ")
            
            #For Choice 1
            if user_input == "1":
                if Bank.logged_user["checking"] == "False":
                    print("\n**You don't have checking account** !!")
                    continue
                else:
                    print(" -- Deposit to checking account -- ")
                    amount = float(input("Enter the amount💲: "))
                    current_checking_balance = float(Bank.logged_user["checking"])
                    Bank.logged_user["checking"] = current_checking_balance + amount  #To increase the amount of the account
                    updated_checking_balance = check.checking_account()
                    print(f"Deposit completed successfully✅, your new checking account balance is: {updated_checking_balance}$")
                    Bank.save_users()
                    user_input = input("Press 'Enter' to return to deposit menu📃 ")
                
            #For Choice 2
            elif user_input == "2":
                if Bank.logged_user["savings"] == "False":
                    print("\n**You don't have savings account** !!")
                    continue
                else:
                    print(" -- Deposit to savings account -- ")
                    amount = float(input("Enter the amount💲: "))
                    current_savings_balance = float(Bank.logged_user["savings"])
                    Bank.logged_user["savings"] = current_savings_balance + amount  #To increase the amount of the account
                    updated_savings_balance = check.saving_account()
                    print(f"Deposit completed successfully✅, your new saving account balance is: {updated_savings_balance}$")
                    Bank.save_users()
                    user_input = input("Press 'Enter' to return to deposit menu📃 ")
                
            #For exiting
            elif user_input == "3":
                is_running = False
            
            #If user enter a choice not on the list
            else:
                print("Enter a valid choice !!")
        
# -------------------------------------------------------------------------------------#





#Class 6
# ----------------------------------- FOR TRANSFER ------------------------------------#
class Transfer:
    def transfer_from():
        is_running = True
        while is_running:
            print("\n-------- Transfer --------")
            print("** 💸Which account do you want to transfer from?💸 **")
            print("1️⃣. Checking Account")
            print("2️⃣. Savings Account")
            print("3️⃣. Back to the past menu🔙")
            user_input = input("Enter your choice: ")
            
            #For Choice 1
            if user_input == "1":
                if Bank.logged_user["checking"] == "False":
                    print("\nYou don't have checking account !!!")
                    continue
                else:
                    Transfer.transfer_from_checking()
            
            #For Choice 2
            elif user_input == "2":
                if Bank.logged_user["savings"] == "False":
                    print("\nYou don't have savings account !!!")
                    continue
                else:
                    Transfer.transfer_from_savings()
            
            #For exiting
            elif user_input == "3":
                is_running = False
            
            #If user enter a choice not on the list
            else:
                print("Enter a valid choice !!")

#-----------------------------------------------------------------------------------------------------------#

    #If you select to transfer from Checking account:
    def transfer_from_checking():
        is_running = True
        while is_running:
            #Now you should select which account you will transfer to:
            print("\n## Which account do you want to transfer to? ##")
            print("1️⃣. Savings Account")
            print("2️⃣. Customer's Account")
            print("3️⃣. Back to the past menu🔙")
            user_input = input("Enter your choice: ")
            
# -----------------------------------------------------------------------------------------------------------#




#---------------------------------- TRANSFER FROM CHECKING TO SAVINGS ---------------------------------------#

            #For Choice  1 < from Checking account to Savings account:
            if user_input == "1":
                if Bank.logged_user["savings"] == "False":
                    print("\n**You don't have savings account** !!")
                    continue
                else:
                    print("\n\nNow you will transfer money from your 'Checking' to 'Savings' account")
                    amount = float(input("Enter the amount💲: "))
                    current_checking_balance = float(Bank.logged_user["checking"])
                    current_savings_balance = float(Bank.logged_user["savings"])
                
                    if amount <= current_checking_balance:
                        Bank.logged_user["checking"] = current_checking_balance - amount
                        Bank.logged_user["savings"] = current_savings_balance + amount
                        updated_checking_balance = check.checking_account()
                        updated_savings_balance = check.saving_account()
                        print(f"Transfer completed✅,\n[your Savings account balance is {updated_savings_balance}$💵 .]\n[your Checking account balance is {updated_checking_balance}$💸 .]\n")
                        Bank.save_users()
                        user_input = input("Press 'Enter' to return to transfer to menu📃 ")

                #If the balance of the account you want to transfer from is less than the amount you put:
                    elif amount > current_checking_balance:
                        print("You don't have this amount of money ❌!!")

# -------------------------------------------------------------------------------------------------------------------------------------------#




#----------------------------------------- TRANSFER FROM CHECKING TO CUSTOMER ---------------------------------------------------------------#

            #For Choice 2 < from Checking account to customer's account:
            if user_input == "2":
                
                print("\nNow you will transfer money from your 'Checking' to 'Customer's' account")
                user_input = (input("Enter the customer ID: "))
                amount = float(input("Enter the amount💲: "))
                current_checking_balance = float(Bank.logged_user["checking"])
                if amount <= current_checking_balance:
                    Bank.logged_user["checking"] = current_checking_balance - amount
                    updated_checking_balance = check.checking_account()
                    print(f"Transfer completed✅, your checking account balance {updated_checking_balance}$")
                    Bank.save_users()
                    user_input = input("Press 'Enter' to return to transfer to menu📃 ")

                #If the balance of the account you want to transfer from is less than the amount you put:
                elif amount > current_checking_balance:
                    print("You don't have this amount of money ❌!!")

            #For exiting
            if user_input == "3":
                is_running = False

# ------------------------------------------------------------------------------------------------------------#

    #If you select to transfer from Savings account:
    def transfer_from_savings():
        is_running = True
        while is_running:
            print("\n\n## Which account do you want to transfer to? ##")
            print("1️⃣. Checking Account")
            print("2️⃣. Customer's Account")
            print("3️⃣. Go to the past menu")
            user_input = input("Enter your choice: ")
            
#----------------------------------------------------------------------------------------------------------#




#---------------------------------- TRANSFER FROM SAVINGS TO CHECKING --------------------------------------#

            #For Choice 1 < from Savings account to Checking account:
            if user_input == "1":
                print("\n\nNow you will transfer money from your 'Savings' to 'Checking' account")
                amount = float(input("Enter the amount💲: "))
                current_checking_balance = float(Bank.logged_user["checking"])
                current_savings_balance = float(Bank.logged_user["savings"])
                if amount <= current_savings_balance:
                    Bank.logged_user["checking"] = current_checking_balance + amount
                    Bank.logged_user["savings"] = current_savings_balance - amount
                    updated_checking_balance = check.checking_account()
                    updated_savings_balance = check.saving_account()
                    print(f"Transfer completed✅,\n[your Checking account balance is {updated_checking_balance}$💵 .]\n[your Savings account balance is {updated_savings_balance}$💸 .]\n")
                    Bank.save_users()
                    user_input = input("Press 'Enter' to return to transfer to menu📃 ")

                #If the balance of the account you want to transfer from is less than the amount you put:
                elif amount > current_savings_balance:
                    print("You don't have this amount of money ❌!!")

#----------------------------------------------------------------------------------------------------------------------------------#




#---------------------------------------------- TRANSFER FROM SAVINGS TO CUSTOMER -------------------------------------------------#

            #For Choice 2 < from Savings account to Customer's account:
            elif user_input == "2":
                print("\n\nNow you will transfer money from your 'Savings' to 'Customer's' account")
                user_input = (input("Enter the customer ID: "))
                amount = float(input("Enter the amount💲: "))
                current_savings_balance = float(Bank.logged_user["savings"])
                if amount <= current_savings_balance:
                    Bank.logged_user["savings"] = current_savings_balance - amount
                    updated_savings_balance = check.saving_account()
                    print(f"Transfer completed✅, your Savings account balance {updated_savings_balance}$")
                    Bank.save_users()
                    user_input = input("Press 'Enter' to return to transfer to menu📃 ")

                #If the balance of the account you want to transfer from is less than the amount you but:
                elif amount > current_savings_balance:
                    print("You don't have this amount of money ❌!!")

            #For exiting
            elif user_input == "3":
                is_running = False

            #If user enter a choice not on the list
            else:
                print("Enter a valid choice!!")

# --------------------------------------------------------------------------------------------------------------------------------#




# ---------------------------------------------------- Main menu Page ------------------------------------------------------------#

def main():
    Bank.load_users()
    is_running = True
    while is_running:
        print("\n======================")
        print("Select transaction: ")
        print("======================")
        print("1: Withdraw")
        print("2: Deposit")
        print("3: Transfer")
        print("--- If you don't have an account: ---")
        print("4: Create checking & savings accounts")
        print("5: Log out")
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
            is_running = False
        else: print("Enter a valid choice !!")
    print("Have a good day sir 😉")
# # -----------------------------------------------------------------------------------------------------------------------------#




#----------------------------------------------------- FIRST MENU ---------------------------------------------------------------#
def welcome_menu():
    Bank.load_users()
    is_running = True
    while is_running:
        print("\n======================")
        print("Welcome to the Bank :)")
        print("======================")
        print("1: Login")
        print("2: Register")
        print("3: Exit")
        user_input = input("Enter your choice: ")
        if user_input == "1":
            Bank.login()
            is_running = True
            while is_running:
                if is_running == True:
                    main()
                    break
        elif user_input == "2":
            Bank.register()
            is_running = True
            while is_running:
                if is_running == True:
                    Bank.login()
                    main()
                    break
        elif user_input == "3":
            is_running = False
        else: print("Enter a valid choice !!")
#------------------------------------------------------------------------------------------------------------------------------#

welcome_menu()