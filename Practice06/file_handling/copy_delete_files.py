#1
import shutil
shutil.copy("example.txt", "copy_example.txt")
print("File copied successfully")

#2
import os
os.remove("copy_example.txt")
print("File deleted")

#3
import os
if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("File deleted")
else:
    print("File does not exist")

#4
import os
os.rmdir("myfolder")
print("Folder removed")

#5
import shutil
shutil.rmtree("myfolder")
print("Folder and all contents deleted")