## **kwargs = parameter that will pack all argument into a dictionary
##             function can accept a varying amount of keyword argument


def hello(**stuff):
    # print("Hello " + stuff['last'] + " " + stuff['first'])

    print("Hello", end = " ")
    for key,value in stuff.items():
        print(value, end = " ")

# def hello(**stuff):
#     print("Nothing here: ", end = " ")
#     for key,value in stuff.items():
#         print(value, end = " ")

# def hello():
#     pass

# hello(last = "pham", first = "nam")
hello(last = "pham", mid = "the", first = "nam")