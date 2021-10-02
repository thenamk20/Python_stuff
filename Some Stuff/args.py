# *args  =  parameter that will pack all arguments into a tuple
#           usefull so that a function can accept a varying amount of arguments
#           (truyen tham so khong gioi han)


def sum(*stuff):
    sum = 0

    #cause tuple is unchangeable, so we can do like this for changing argument value
    # stuff = list(stuff)
    # stuff[0] = 2

    for i in stuff:
        sum += i
    return sum


print(sum(1,2,3,4,5))