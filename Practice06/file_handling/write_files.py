#1
file = open("example.txt", "w")
file.write("Hello, this is my first file.\n")
file.write("Python is easy!")
file.close()

#2
file = open("example.txt", "a")
file.write("\nThis line is added later.")
file.close()

#3
file = open("newfile.txt", "x")
file.write("New file created!")
file.close()

#4
with open("example2.txt", "w") as file:
    file.write("Using with statement\n")
    file.write("File will close automatically")

#5
lines = ["Apple\n", "Banana\n", "Cherry\n"]

with open("fruits.txt", "w") as file:
    for line in lines:
        file.write(line)
        