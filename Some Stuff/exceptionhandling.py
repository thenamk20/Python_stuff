
try:
    a = int(input("Enter divided number: "))
    b = int(input("Enter number to divide by: "))
    
    res = a/b

except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero")


except ValueError as e:
    print(e)
    print("Only number, plz")

except Exception as e:
    print(e)
    print("Something went wrong :(")

else:
    print(res)
finally:
    print("this always be executed")    