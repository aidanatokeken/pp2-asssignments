#1
import shutil
shutil.move("example.txt", "folder/example.txt")
print("File moved successfully")

#2
import shutil
shutil.move("example.txt", "folder/new_name.txt")
print("File moved and renamed")

#3
import shutil
shutil.move("my_folder", "backup/my_folder")
print("Folder moved")

#4
import os
import shutil
if os.path.exists("example.txt"):
    shutil.move("example.txt", "folder/example.txt")
    print("File moved")
else:
    print("File does not exist")

#5
import os
import shutil
source = "source_folder"
destination = "destination_folder"
files = os.listdir(source)
for file in files:
    shutil.move(os.path.join(source, file), destination)
print("All files moved")