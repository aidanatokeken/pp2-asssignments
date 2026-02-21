#1
class Person:
    pass
p = Person()
print(p)

#2
class Person:
    def say_hello(self):
        print("Hello!")

p = Person()
p.say_hello()

#3
class Car:
    wheels = 4

my_car = Car()
print(my_car.wheels)

#4
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Ayan")
print(p.name)

#5
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(10, 20))