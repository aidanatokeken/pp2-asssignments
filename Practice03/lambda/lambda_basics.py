#1 
square = lambda x: x * x
print(square(5))  #  25

#2
add = lambda a, b: a + b
print(add(3, 7))  # 10

#3
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, numbers))
print(squares)

#4
numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # [2, 4, 6]

#5
students = [("Ali", 15), ("Dana", 18), ("Zhan", 17)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)