class customer:
    def __init__(self, id, Name, Room):
        self.id = id
        self.Name = Name
        self.Room = Room


class admin:
    def __init__(self, Username, pwd):
        self.Username = Username
        self.password = pwd


class products:
    def __init__(self, ctg, name, CP, quantity, stock, disc):
        self.name = name
        self.category = ctg
        self.costprice = CP
        self.quantity = quantity
        self.stock = stock
        self.dic = disc


class cart:
    def __init__(self):
        self.items = []


user = input("Enter the usertype ADMIN or STUDENT")
if (user == "ADMIN"):
    usr = input("Enter the username: ")
    pwd = input("Enter the password: ")

else:
    Name = input("Enter your name : ")
    id = input("Enter your id : ")
    Room = input("Enter your Bhawan and Room Number : ")
    c = customer(Name, id, Room)
