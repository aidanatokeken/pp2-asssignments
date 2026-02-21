#1
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Aigul")
print(p.name)

#2
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

my_car = Car("Toyota", 2020)
print(my_car.brand, my_car.year)

#3
class Dog:
    def __init__(self, name="Buddy"):
        self.name = name

d1 = Dog("Rex")
d2 = Dog()
print(d1.name, d2.name)

#4
class Account:
    def __init__(self, balance):
        self.__balance = balance

acc = Account(1000)
print(acc._Account__balance)

#5
class Person:
    def __init__(self, name):
        self.name = name
        self.greet()

    def greet(self):
        print("Hello,", self.name)

p = Person("Aidana")

