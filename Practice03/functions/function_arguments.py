#1 example
def greet(name):
    print("Hello " + name)

greet("Aidana")

#2 example
def full_name(first, last):
    print(first + " " + last)

full_name("Aidana", "Asylovna")

#3 example
def students(*names):
    print("First student is " + names[0])

students("Ali", "Aruzhan", "Dias")

#4 example
def info(name, age):
    print("Name:", name)
    print("Age:", age)

info(age=18, name="Aidana")

#5 example
def country(name="Kazakhstan"):
    print("I am from " + name)

country("Turkey")
country()