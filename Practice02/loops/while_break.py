#1 example
i = 1
while True:
    print(i)
    if i == 5:
        break
    i += 1

#2 example
while True:
    text = input("Enter the text: ")
    if text == "stop":
        break
    print("You are enter:", text)

#3 example
i = 1
total = 0
while True:
    total += i
    if total >= 20:
        break
    i += 1
print(total)

#4 example
i = 1
while True:
    if i % 2 == 0:
        break
    print(i)
    i += 1

#5 example
attempts = 0

while True:
    attempts += 1
    print("Yor attempts", attempts)
    if attempts == 3:
        break