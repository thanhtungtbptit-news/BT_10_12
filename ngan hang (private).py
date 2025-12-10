# %%
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):
        print(f"Xin chao ,tôi là {self.name} năm nay {self.age} tuổi")
s1=Person ("Tung",21)
s1.say_hello()

class car:
    def __init__ ( self,brand,color) :
        self.brand=brand
        self.color=color

car1=car("Ford","Red")
print(f"Hãng xe :", car1.brand)
print(f"Màu xe : ",car1.color)

# %%
class BankAccount:
    def __init__ (self,owner,balance) :
        self.owner = owner
        self.__balance = balance
    
    def show_balance(self) :
        print("Số dư : " , {self.__balance})
    
    def change_balance(self,amount,OTP):
        if OTP == 1304 :
            self.__balance=amount
            print("Số dư : ",self.__balance)

acc=BankAccount("Tung",2000)
acc.show_balance()
acc.change_balance(500,13)
acc.show_balance()


