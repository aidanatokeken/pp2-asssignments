#1
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

#2
file = open("example.txt", "r")
content = file.read(10) 
print(content)
file.close()

#3
file = open("example.txt", "r")
print(file.readline()) 
print(file.readline())
file.close()

#4
file = open("example.txt", "r")
for line in file:
    print(line)
file.close()

#5
with open("example.txt", "r") as file:
    content = file.read()
    print(content)