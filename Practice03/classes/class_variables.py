#1
class Dog:
    species = "Canis familiaris"

d1 = Dog()
d2 = Dog()

print(d1.species)                
print(d2.species)

#Canis familiaris
#Canis familiaris

#2
class Car:
    wheels = 4

c1 = Car()
c2 = Car()

Car.wheels = 3

print(c1.wheels)
print(c2.wheels)          #3       3

#3
class Person:
    species = "Human"

p1 = Person()
p1.name = "Alina"

print(p1.name)
print(p1.species)      #Alina       Human

#4
class Student:
    school = "High School"

s1 = Student()
s2 = Student()

s1.school = "Middle School"

print(s1.school)
print(s2.school)                #Middle School      High School

#5
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
c3 = Counter()

print(Counter.count)        #3