from user import User,Products
from admin import Admin
import colorama as c
while True:
    print(c.Style.BRIGHT +
          c.Fore.RED +
          ":.:.:.:.:.:" + c.Fore.YELLOW + "    Welcome to the Shop    " + c.Fore.RED +":.:.:.:.:.:",
          c.Fore.LIGHTWHITE_EX + "\n1_sign in",
          "2_sign up",
          "3_exit\n", sep="\n")
    operation_choice = input(c.Fore.WHITE + "-please enter 1 for sign in to your account or enter 2 to create account : ")
    while operation_choice == "1":
        username = input(c.Fore.BLUE + "\n~:~:~:~:" + c.Fore.WHITE + " Welcome Back " + c.Fore.BLUE + ":~:~:~:~\n\n" + c.Fore.LIGHTYELLOW_EX + "Please enter your username :\n")
        password = input("Please enter your password : \n")
        while username == "admin" and password == "admin1234":
            print(c.Fore.YELLOW + "\nNNNNNNNNNNN" + c.Fore.WHITE + " Welcome To Admin Page " + c.Fore.YELLOW + "NNNNNNNNNNN\n\n" + c.Fore.LIGHTWHITE_EX +
                  "1_ New Product\n" + "2_Remove Product\n" + "3_ Users Buy History\n" + "4_ Users List\n" + "5_ Store Account Balance\n" + "6_ Total Sell Price\n" + "7_ exit\n")
            admin_operation = input("-please enter your operation : ")
            if admin_operation == "1":
                collection = input(c.Fore.LIGHTYELLOW_EX + "\n-please enter your collection : \n")
                product = input("-please enter your product name : \n")
                price = input("-please enter price of product : \n")
                Admin.new_product(collection, product, price)
            elif admin_operation == "2":
                collection = input(c.Fore.LIGHTYELLOW_EX + "\n-please enter your collection : \n")
                product = input("-please enter your product name : \n")
                Admin.remove_product(collection, product)
            elif admin_operation == "3":
                Admin.buy_history()
            elif admin_operation == "4":
                Admin.user_list()
            elif admin_operation == "5":
                Admin.store_account_balance()
            elif admin_operation == "6":
                Admin.total_sell_price()
            elif admin_operation == "7":
                break
        while User.find((username + " : " + password), "user.txt"):
            print(c.Fore.MAGENTA + "\n-:-:-:-:" + c.Fore.WHITE + " Welcome To Manage Shop List " + c.Fore.MAGENTA + ":-:-:-:-\n\n" + c.Fore.LIGHTWHITE_EX)
            number = 1
            for collection in Products.collection_list():
                print(str(number) + "_ " + collection)
                number += 1
            print(str(number) + "_ Pay Cash\n" + str(number+1) + "_ Delete User\n"+ str(number+2) + "_ exit")
            user_operation = int(input("\n-please enter your operation from top list : "))
            try:
                user = Products(username, password)
                user.food_collection(Products.collection_list()[user_operation-1])
            except:
                if str(user_operation) == str(number):
                    user = Products(username, password)
                    user.pay_cash()
                elif str(user_operation) == str(number+1):
                    user = User(username, password)
                    user.user_remove()
                elif str(user_operation) == str(number+2):
                    break
                else:
                    print(c.Fore.LIGHTRED_EX + "Your insert is wrong!")
    while operation_choice == "2":
        username = input(c.Fore.BLUE + "\n~:~:~:~:" + c.Fore.WHITE + " Welcome " + c.Fore.BLUE + ":~:~:~:~\n\n" + c.Fore.LIGHTYELLOW_EX + "Please enter your username :\n")
        password = input("Please enter your password : \n")
        user = User(username, password)
        condition = user.user_create()
        if condition:
            break
    if operation_choice == "3":
        print(c.Fore.LIGHTGREEN_EX + "Have a good day :)", "Good Luck." + c.Style.RESET_ALL, sep="\n")
        break
    elif operation_choice not in ["1", "2", "3"]:
        print(c.Fore.LIGHTRED_EX + "\nYour insert is Wrong!\n")
        continue