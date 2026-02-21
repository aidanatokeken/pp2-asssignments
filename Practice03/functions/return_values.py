#1
def get_number():
    return 10

num = get_number()
print(num)  # 10


#2
def say_hello():
    return "Hello!"

message = say_hello()
print(message)

#3
def add(a, b):
    return a + b

result = add(5, 7)
print(result)  #  12

#4
def is_even(num):
    return num % 2 == 0

print(is_even(4))  # True
print(is_even(7))  # False

#5
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

my_pet = Dog()
print(my_pet.sound())  # Bark