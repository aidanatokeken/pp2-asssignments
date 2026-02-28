#1
def simple_gen():
    yield 1
    yield 2
    yield 3

for value in simple_gen():
    print(value)       #A function with yield returns one value at a time.

#2
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)          #The generator returns numbers from 1 to n.

#3
def squares(n):
    for i in range(1, n+1):
        yield i * i

print(list(squares(5)))      #[1, 4, 9, 16, 25]

#4
def infinite_counter():
    i = 1
    while True:
        yield i
        i += 1

gen = infinite_counter()
print(next(gen))
print(next(gen))
print(next(gen))   #1  2  3

#5
def even_numbers(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            yield i

print(list(even_numbers(10)))    #[2, 4, 6, 8, 10]