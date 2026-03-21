#1
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

for name, score in zip(names, scores):
    print(name, score)

#2
fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits):
    print(i, fruit)

#3
names = ["Ali", "Aru", "Dana"]
grades = [90, 85, 95]

for i, (name, grade) in enumerate(zip(names, grades), start=1):
    print(i, name, grade)

#4
names = ["Ali", "Aru"]
ages = [18, 19]
city = ["Almaty", "Astana"]

for name, age, c in zip(names, ages, city):
    print(name, age, c)

#5
numbers = [1, 2, 3]
letters = ["a", "b", "c"]
result = list(zip(numbers, letters))

print(result)
