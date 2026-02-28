#1.Create a generator that generates the squares of numbers up to some number N.
def square_generator(N):
    for i in range(1, N + 1):
        yield i ** 2
# Example usage
N = int(input("Enter N: "))
for square in square_generator(N):
    print(square)

#2.Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_generator(n):
    for i in range(0, n + 1, 2):  # step 2 to get even numbers
        yield i
# Input from console
n = int(input("Enter n: "))
# Generate even numbers and join them as comma-separated string
even_numbers = ','.join(str(num) for num in even_generator(n))
print(even_numbers)

#3.Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Input from console
n = int(input("Enter n: "))

# Using the generator
for number in divisible_by_3_and_4(n):
    print(number, end=' ')

#4.Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

# Input from console
a = int(input("Enter start number (a): "))
b = int(input("Enter end number (b): "))

# Using the generator and printing each value
for sq in squares(a, b):
    print(sq)

#5.Implement a generator that returns all numbers from (n) down to 0.
def countdown(n):
    for i in range(n, -1, -1):  # start from n, end at 0, step -1
        yield i
# Input from console
n = int(input("Enter n: "))
# Using the generator
for num in countdown(n):
    print(num)
