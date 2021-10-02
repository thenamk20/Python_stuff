
try:
    with open('Learning/File processing/something.txt') as file:
        print(file.read())

except FileNotFoundError:
    print("Not found")