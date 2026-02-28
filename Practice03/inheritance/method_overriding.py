#1
class Person:
    def greet(self):
        print("Hello from Person")

class Student(Person):
    def greet(self):
        print("Hello from Student")

s = Student()
s.greet()

#2
class Person:
    def greet(self):
        print("Hello from Person")

class Student(Person):
    def greet(self):
        print("Before override")
        super().greet()
        print("After override")

s = Student()
s.greet()

#3
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    pass

d = Dog()
c = Cat()
d.sound() # bra
c.sound() # some

#4
class Person:
    def __init__(self):
        self.name = "Unknown"

class Student(Person):
    def __init__(self):
        self.name = "Student"

s = Student()
print(s.name)

#5
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Aruzhan", 11)
print(s.name, s.grade)
