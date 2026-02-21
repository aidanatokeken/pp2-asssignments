#1
class Person:
    def greet(self):
        print("Hello from Person!")

p = Person()
p.greet()

#2
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(5, 10))

#3
class Dog:
    def __init__(self, name):
        self.name = name

    def rename(self, new_name):
        self.name = new_name

d = Dog("Rex")
d.rename("Max")
print(d.name)

#4
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

c = Circle(5)
print(c.area())

#5
class Student:
    school = "High School"

    @classmethod
    def get_school(cls):
        return cls.school

print(Student.get_school())
