#1 example
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

#2 example
i = 1
while i <= 10:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1

#3 example
while True:
    text = input("Enter the text: ")
    if text == "":
        continue
    print("You enter:", text)
#4 example
i = -3
while i <= 3:
    if i < 0:
        i += 1
        continue
    print(i)
    i += 1
    
#5 example
word = "banana"
i = 0

while i < len(word):
    if word[i] == "a":
        i += 1
        continue
    print(word[i])
    i += 1