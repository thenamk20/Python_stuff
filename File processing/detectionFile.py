import os

path = "Learning\\File processing\\alive.txt"

if os.path.exists(path):
    print("That location exist!")
    if os.path.isfile(path):
        print("It's a file")
    elif os.path.isdir(path):
        print("It's a directory")

else:
    print("That location doesn't exist!")