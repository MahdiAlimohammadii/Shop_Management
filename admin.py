import colorama as c
from user import User
class Admin:
    @staticmethod
    def new_product(collection, product, price):
        if User.find(collection, "products.txt") and not User.find(product, "products.txt"):
            with open("products.txt", "r+") as products:
                product_list = products.readlines()
                collection_list = []
                for item in product_list:
                    if collection in item:
                        collection_list.append(item)
                collection_list = sorted(collection_list)
                number = str(int(collection_list[-1][0]) + 1)
                products.write(number + "_ " + collection + " : " + product +
                               " , price : " + price + " $\n")
            print(c.Fore.GREEN + "\nYour product has been added.")
        elif not User.find(collection, "products.txt") and not User.find(product, "products.txt"):
            with open("products.txt", "a") as products:
                products.write("1_ " + collection + " : " + product +
                               " , price : " + price + " $\n")
            print(c.Fore.GREEN + "\nYour product has been added.")
        elif User.find(product, "products.txt"):
            print(c.Fore.LIGHTRED_EX + "\nthis product exist!")
    
    @staticmethod
    def remove_product(collection, product):
        if User.find(collection, "products.txt") and User.find(product, "products.txt"):
            with open("products.txt", "r") as products:
                product_list = products.readlines()
            with open("products.txt", "w") as products:
                collection_list = []
                for item in product_list:
                    if collection in item and product not in item:
                        collection_list.append(item)
                collection_list = sorted(collection_list)
                for item in product_list:
                    if collection in item:
                        pass
                    else:
                        products.write(item)
                for number in range(1, (len(collection_list) + 1)):
                    products.write(str(number) + collection_list[number-1][1:])
                print(c.Fore.GREEN + "\nproduct " + collection + " : " + product + " has been deleted.")
        else:
            print(c.Fore.LIGHTRED_EX + "\nproduct not exist.")
    
    @staticmethod
    def print_from_list(file_name):
        with open(file_name, "r") as file:
            file_list = file.readlines()
            file_list = sorted(file_list)
            for item in file_list:
                print(c.Fore.LIGHTWHITE_EX + item)
    
    @staticmethod
    def buy_history():
        Admin.print_from_list("Factor.txt")
    
    @staticmethod
    def user_list():
        Admin.print_from_list("user.txt")
    
    @staticmethod
    def store_account_balance():
        with open("admin.txt", "r") as admin_file:
            storage = admin_file.readline()
            print(c.Fore.GREEN + "\n" + storage[16:])
    
    @staticmethod
    def total_sell_price():
        with open("Factor.txt", "r") as factor:
            factor_list = factor.readlines()
            total_sell = 0
            for factor in factor_list:
                if "Paid" in factor:
                    total_sell += int(factor[(factor.find(":")+2):-8])
            else:
                print(c.Fore.GREEN + "\nTotal Sell Price : " + str(total_sell) + " $")
    
