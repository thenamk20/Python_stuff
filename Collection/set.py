# set =  a collection which is unordered, unindexed. No duplicate values

animal = {"fox","cat","dog","dragon"}

animal.add("horse")

animal.remove("fox")

animal.clear()

myth = {"dragon","unicorn","fairy"}

animal.update(myth)

something = animal.union(myth)    # join two set together

## compare:
print(animal.difference(myth))

print(myth.difference(animal))

## print common item
print(animal.intersection(myth)) 

# for x in animal:
#     print(x)