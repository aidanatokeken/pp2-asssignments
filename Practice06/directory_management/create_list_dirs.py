#1
import os
os.mkdir("my_folder")
print("Folder created")

#2
import os
if not os.path.exists("my_folder"):
    os.mkdir("my_folder")
    print("Folder created")
else:
    print("Folder already exists")

#3
import os
os.makedirs("parent/child/grandchild")
print("Nested folders created")

#4
import os
files = os.listdir(".")  # текущая папка

for file in files:
    print(file)

#5
import os
os.mkdir("test_folder")
os.chdir("test_folder")
print("Current directory:", os.getcwd())
print("Contents:", os.listdir())