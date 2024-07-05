import colorama as c
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    @staticmethod
    def find(item, file_name):
        # this func for find item in file . if exist True . else False
        with open(file_name, "r") as file:
            file_list = file.readlines()
        for element in file_list:
            if item in element:
                return True
        else:
            return False
    
    def user_create(self):
        user_file = open("user.txt", "a")
        if not(User.find(self.username, "user.txt")):
            user_file.write(str(self.username) + " : " + str(self.password) + " , manage payment : settle\n")
            print(c.Fore.GREEN + "\nyour account has been created.")
            return True
        else:
            print(c.Fore.LIGHTRED_EX + "\nsomeone exist with your username.")
            return False
        user_file.close()
    
    def user_remove(self):
        condition = False
        with open("user.txt", "r") as user:
            user_list = user.readlines()
        user_file = open("user.txt", "w")
        for user in user_list:
            if self.username in user:
                condition = True
            else:
                user_file.write(user)
        if condition:
            print(c.Fore.GREEN + "\nuser has been deleted.")
        else:
            print(c.Fore.LIGHTRED_EX + "\nuser not exist.")
    
    @staticmethod
    def user_manage_payment():
        with open("user.txt", "r") as users:
            user_list = users.readlines()
        user_list = sorted(user_list)
        with open("Factor.txt", "r") as factor:
            factor_list = factor.readlines()
        with open("user.txt", "w") as users:
            for user in user_list:
                indebted = 0
                for factor in factor_list:
                    if user[:(user.find(":")-1)] in factor and "Paid" not in factor:
                        indebted += int(factor[(factor.find(":")+2):-3])
                else:
                    if indebted == 0:
                        users.write(user[:(user.find("manage payment : ")+17)] +  "settle\n")
                    else:
                        users.write(user[:(user.find("manage payment : ")+17)] + str(indebted) + " $\n") 

class Products(User):    
    def food_collection(self, collection):
        with open("products.txt", "r") as product:
            product_list = product.readlines()
            collection_list = []
            for item in product_list:
                if collection in item:
                    collection_list.append(item)
            product_list = sorted(collection_list)
            for item in product_list:
                print(c.Fore.LIGHTWHITE_EX + item)
            choice = input(c.Fore.LIGHTYELLOW_EX + "\nWhat you want?(please enter thes number)\n")
            while True:
                try:
                    if 1 <= int(choice) <= len(product_list):
                        break
                    else:
                        print(c.Fore.LIGHTRED_EX + "\nyour insert is wrong!")
                except:
                    print(c.Fore.LIGHTRED_EX + "\nyour insert is wrong!")
                for item in product_list:
                    print(c.Fore.LIGHTWHITE_EX + item)
                choice = input(c.Fore.LIGHTYELLOW_EX + "\nWhat you want?(please enter thes number)\n")
            for item in product_list:
                    if choice == item[0]:
                        print(c.Fore.LIGHTWHITE_EX + "\n" + item)
                        choice = input(c.Fore.LIGHTYELLOW_EX + "\nDo you mean this ? \n")
                        while True:
                            if choice.capitalize() == "Yes":
                                choice = input(c.Fore.LIGHTYELLOW_EX + "\nHow much you want it? (1 or 2 or ...)\n")
                                while True:
                                    try:
                                        int(choice)
                                        break
                                    except:
                                        print(c.Fore.LIGHTRED_EX + "\nyour insert is wrong!")
                                    choice = input(c.Fore.LIGHTYELLOW_EX + "\nHow much you want it? (1 or 2 or ...)\n")
                                final = input(c.Fore.LIGHTYELLOW_EX + "\nAre you sure want " + choice + " of this item ? \n")
                                while True:
                                    if final.capitalize() == "Yes":
                                        with open("Factor.txt", "a") as factor:
                                            factor.write(str(self.username) + " buy " + choice + " " + item[(item.find(":")+2):(item.find(","))] +
                                                         "with price : " + str(int(choice) * int(item[(item.find("price")+8):-2])) + " $\n")
                                        print(c.Fore.GREEN + "\n" + str(self.username) + " buy " + choice + " " + item[(item.find(":")+2):(item.find(","))] +
                                              "with price : " + str(int(choice) * int(item[(item.find("price")+8):-2])) + " $")
                                        User.user_manage_payment()
                                        break
                                    elif final.capitalize() == "No":
                                        print(c.Fore.LIGHTRED_EX + "\nThe operation was stopped.")
                                        break
                                    else:
                                        print(c.Fore.LIGHTRED_EX + "\nyour insert is wrong!")
                                        final = input(c.Fore.LIGHTYELLOW_EX + "\nAre you sure want " + choice + " of this item ? \n")
                                        continue
                                break
                            if choice.capitalize() == "No":
                                print(c.Fore.LIGHTRED_EX + "\nThe operation was stopped.")
                                break
                            else:
                                print(c.Fore.LIGHTRED_EX + "\nyour insert is wrong!\n")
                                print(c.Fore.LIGHTWHITE_EX + item)
                                choice = input(c.Fore.LIGHTYELLOW_EX + "\nDo you mean this ? \n")
                                continue
                        break
    
    @staticmethod
    def collection_list():
        with open("products.txt", "r") as products:
            product_list = products.readlines()
            collection_List = []
            for product in product_list:
                collection_List.append(product[3:(product.find(":")-1)])
            # for delete repeated item in list and sort this
            collection_List = set(collection_List)
            collection_List = list(collection_List)
            collection_List = sorted(collection_List)
            return collection_List
    
    def pay_cash(self):
        factor_file = open("Factor.txt", "r")
        factor_list = factor_file.readlines()
        factor_file.close()
        factor_file = open("Factor.txt", "w")
        for factor in factor_list:
            if self.username in factor and "Paid" not in factor:
                cash = int(factor[(factor.find(":")+2):-3])
                admin_file = open("admin.txt", "r")
                admin_list = admin_file.readlines()
                with open("admin.txt", "w") as admin:
                    for item in admin_list:
                        if "Storage_Money" in item:
                            storage = int(item[16:-3]) + cash
                            admin.write("Storage_Money = " + str(storage) + " $\n")
                        else:
                            admin.write(item)
                factor_file.write(factor[:-1] + " Paid\n")
            else:
                factor_file.write(factor)
        print(c.Fore.GREEN + "\ndone.")
        factor_file.close()
        User.user_manage_payment()
