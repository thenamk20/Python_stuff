# A dicntionary: a changeable, unorder collection of unique key:value pair 
#                they fast cause they use hasing 

capitals = {'Vietnam':'Hanoi',
            "Japan":"Tokyo",
            'England':"London"}


print(capitals['Japan']) # print value

print(capitals.get("Vietnam")) # print value safer

capitals.pop("Japan") #delete a item

capitals.update({'Vietnam':"Saigon"})  # change value of a key

capitals.update({'Korean':'Soeul'})   # add a key-value item

a = len(capitals)
 
print(capitals)
print(capitals.keys()) # print all keys
print(capitals.values()) # print all values

for key,value in capitals.items():
    print(key, value)