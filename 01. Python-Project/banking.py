import csv

#Class 1
# --------------- FOR CREATE NEW ACCOUNT ---------------#
class createAccount:
    def __init__(self, username, password):
        username = username
        password = password
    def login():
        username = input("Username: ")
        password = input("Password: ")
    def register():
        username = input("Username: ")
        password = input("Password: ")
# ------------------------------------------------------#

#Class 2
# --------------- FOR CHECKING, SAVINGS, OR BOTH ---------------#
        class AddNewCustomer:
            pass
# --------------------------------------------------------------#

#Class 3
# --------------- FOR WITHDRAW ---------------#
            class Withdraw:
                pass
# --------------------------------------------#

#Class 4
# --------------- FOR DEPOSIT ---------------#
                class Deposit:
                    pass
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
        print("======================")
        print("Welcome to the Bank :)")
        print("======================")
        print("1: Login")
        print("2: Create new account")
        print("3: Exit")
        user_input = input("Enter your choice: ")
        if user_input == "1":
            createAccount.login()
        elif user_input == "2":
            createAccount.register()
        elif user_input == "3":
            is_running = False
        else: print("Enter a valid choice !!")
# # -----------------------------------------#

main()
