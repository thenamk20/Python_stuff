import os
import shutil

path = "alive2.txt"

dir_path = "Learning/folder"

try:
    os.remove(path) #remove file
    os.rmdir(dir_path) #delete a empty directory
    shutil.rmtree(dir_path) #delete a directory and all file which contain in

except FileNotFoundError:
    print("File doen't exist!")

except PermissionError:
    print("You don't have permisson")   

except OSError:
    print("You can use that function to delete ")

else:
    print(dir_path+" was delete")