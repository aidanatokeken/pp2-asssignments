#1 example
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n == 3:
        break
    print(n)

#2 example
for i in range(1, 20):
    if i == 10:
        break
    print(i)

#3 example
for letter in "abcdef":
    if letter == "c":
        break
    print(letter)

#4 example
numbers = [10, 20, 55, 40, 60]
for n in numbers:
    if n > 50:
        break
    print(n)

#5 example
words = ["hello", "world", "stop", "python"]
for w in words:
    if w == "stop":
        break
    print(w)