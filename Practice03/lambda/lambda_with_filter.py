#1
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

#2
nums = [3, 12, 7, 18, 5]
greater_than_10 = list(filter(lambda x: x > 10, nums))
print(greater_than_10)

#3
words = ["apple", "banana", "kiwi", "strawberry"]
long_words = list(filter(lambda w: len(w) > 5, words))
print(long_words)

#4
values = [-10, 3, -1, 12, -5, 0]
negative = list(filter(lambda x: x < 0, values))
print(negative)

#5
nums = [11, 16, 23, 42, 55]
odd_numbers = list(filter(lambda x: x % 2 != 0, nums))
print(odd_numbers)