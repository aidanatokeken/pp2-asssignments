#1
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Ayan", 10)
print(s.name, s.grade)

#2
class Person:
    def say_hello(self):
        print("Hello from Person")

class Student(Person):
    def say_hello(self):
        super().say_hello()
        print("Hello from Student")

s = Student()
s.say_hello()

#3
class A:
    def action(self):
        print("Action from A")

class B(A):
    def action(self):
        super().action()
        print("Action from B")

b = B()
b.action()

#4
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        super().greet()
        print("Hello from B")

class C(B):
    def greet(self):
        super().greet()
        print("Hello from C")

c = C()
c.greet()

#5
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

t = Teacher("Dana", "Math")
print(t.name, "-", t.subject)
