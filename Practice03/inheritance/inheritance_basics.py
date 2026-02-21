#1
class Person:
    def __init__(self, name):
        self.name = name

    def printname(self):
        print(self.name)

class Student(Person):
    pass

x = Student("Ayan")
x.printname()

#2
class Person:
    def greet(self):
        print("Hello from Person")

class Student(Person):
    def greet(self):
        print("Hello from Student")

s = Student()
s.greet()

#3
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s = Student("Dana", 10)
print(s.name, s.grade)

#4
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Dana", 12)
print(s.name, s.grade)

#5
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, year):
        super().__init__(name)
        self.year = year

    def welcome(self):
        print("Welcome", self.name, "to class of", self.year)

s = Student("Aruzhan", 2025)
s.welcome()
