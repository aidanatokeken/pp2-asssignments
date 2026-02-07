#1 example
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#2 example
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)

#3 example
for letter in "banana":
    if letter == "a":
        continue
    print(letter)

#4 example
words = ["code", "python", "java", "go", "ruby"]
for w in words:
    if len(w) == 4:
        continue
    print(w)

#5 example
numbers = [-2, 3, -1, 5, -6, 2]
for n in numbers:
    if n < 0:
        continue
    print(n)