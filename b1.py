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