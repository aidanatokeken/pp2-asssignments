#1 
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3, 4))  # 10

#2
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key + ":", value)

print_info(name="Ay", age=18)

#3 
def show_all(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

show_all(1, 2, name="Aida", city="Almaty")

#4
class Animal:
    def __init__(self, *args):
        self.traits = args

class Dog(Animal):
    pass

d = Dog("furry", "friendly", "four legs")
print(d.traits)

#5
class Person:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "")
        self.age = kwargs.get("age", 0)

class Student(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grade = kwargs.get("grade", "")

s = Student(name="Aruzhan", age=17, grade="10A")
print(s.name, s.age, s.grade)