#1
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, numbers))
print(squares)

#2
nums = [5, 10, 15, 20]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)

#3
words = ["apple", "banana", "cherry"]
uppercased = list(map(lambda s: s.upper(), words))
print(uppercased)

#4
a = [1, 2, 3]
b = [4, 5, 6]
sum_list = list(map(lambda x, y: x + y, a, b))
print(sum_list)

#5
celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda t: (t * 9/5) + 32, celsius))
print(fahrenheit)
