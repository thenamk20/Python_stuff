
#str.format
import math
some = "me"

thing = "moon"

#some ways to format 
print("Fly {} to the {} ".format(some,thing)) #default
print("Fly {1} to the {0} ".format(some,thing)) # positional index
print("Fly {last} to the {first} ".format(first = some,last = thing)) #keyword argument

sentence = "Fly {0} to the {1}"  #use as variable
print(sentence.format(thing, "sun"))


#format with padding for string
print("Fly {} to the {} and let me play".format(some, thing))
print("Fly {:5} to the {:10} and let me play".format(some, thing)) # "some" occupies three space, "thing" occupy ten space
print("Fly {} to the {:<10} and let me play".format(some, thing))  # right padding (default)
print("Fly {} to the {:>10} and let me play".format(some, thing))  # left padding
print("Fly {} to the {:^10} and let me play".format(some, thing))  # padding for both side


#format for number
number = 10000
pi = 3.141529

print("{:.3f} is a number!".format(pi))  #3.141
print("{:,} is a number!".format(number)) #10,000
print("{:b} is a binary number!".format(number)) # convert to binary
print("{:o} is a octal number!".format(number)) # convert to octal
print("{:X} is a hexa number!".format(number)) # convert to hexa
print("{:e} is a number!".format(number)) # convert to epsilon

def hello():
    print("Hello everyone!")

def bye():
    print("See ya")