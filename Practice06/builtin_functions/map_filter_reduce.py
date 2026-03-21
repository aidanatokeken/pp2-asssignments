#1
numbers = [1, 2, 3, 4]
result = map(lambda x: x * 2, numbers)
print(list(result))

#2
numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))

#3
from functools import reduce
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)

#4
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
squared = map(lambda x: x ** 2, even_numbers)
print(list(squared))

#5
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6]
result = reduce(
    lambda x, y: x + y,
    map(lambda x: x**2,
        filter(lambda x: x % 2 == 0, numbers))
)
print(result)