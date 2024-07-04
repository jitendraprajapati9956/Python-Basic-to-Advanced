print("----->Dictionaries<-----")
print("\n")

print("Create and print a dictionary:")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
print("\n")

print("Dictionary Items:")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])
print("\n")

print("Duplicates Not Allowed:")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)
print("\n")

print("Dictionary Length:")
print(len(thisdict))
print("\n")

print("Data Types:")
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict)
print("\n")

print("type():")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(type(thisdict))
print("\n")

print("dict() Constructor:")
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
print("\n")

print("Access Dictionary Items:")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print("x:",x)
print("Get the value of the 'model' key:")
x = thisdict.get("model")
print("x:",x)
print("\n")

print("Get Keys:")
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change
print("\n")

print("Get Values:")
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
print("\n")

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
print("\n")

print("Get Items:")
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
print("\n")

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
print("\n")

print("Check if Key Exists:")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
print("\n")

print("Change Dictionary Items:")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("thisdict:",thisdict)
thisdict["year"] = 2018
print("thisdict:",thisdict)
print("\n")

print("Update Dictionary:")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("thisdict:",thisdict)
thisdict.update({"year": 2020})
print("thisdict:",thisdict)
print("\n")

print("Add Dictionary Items:")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("thisdict:",thisdict)
thisdict["color"] = "red"
print("thisdict:",thisdict)
print("\n")

print("Update Dictionary:")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("thisdict:",thisdict)
thisdict.update({"color": "red"})
print("thisdict:",thisdict)
print("\n")

print("Remove Dictionary Items:")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("thisdict:",thisdict)
thisdict.pop("model")
print("thisdict:",thisdict)
print("\n")

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("thisdict:",thisdict)
thisdict.popitem()
print("thisdict:",thisdict)
print("\n")

print("Clear() Dictionary Items:")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

print("Delete Dictionary Items:")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)
print("\n")

print("Loop Dictionaries:")
for x in thisdict:
    print(x)
print("\n")

for x in thisdict:
    print(thisdict[x])
print("\n")

for x in thisdict.values():
    print(x)
print("\n")

for x in thisdict.keys():
    print(x)
print("\n")

for x, y in thisdict.items():
    print(x, y)
print("\n")

print("Copy Dictionaries:")
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("thisdict:",thisdict)
mydict = thisdict.copy()
print("mydict:",mydict)
print("\n")


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("thisdict:",thisdict)
mydict = dict(thisdict)
print("mydict:",mydict)
print("\n")

print("Nested Dictionaries:")
myfamily = {
    "child1" : {
        "name" : "Naran",
        "year" : 1996
    },
    "child2" : {
        "name" : "Hiral",
        "year" : 1998
    },
    "child3" : {
        "name" : "Rajesh",
        "year" : 1999
    }
}
print(myfamily)
print("\n")
child1 = {
    "name" : "Naran",
    "year" : 1996
}
child2 = {
    "name" : "Hiral",
    "year" : 1998
}
child3 = {
    "name" : "Rajesh",
    "year" : 1999
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(myfamily)
print("\n")

print("Access Items in Nested Dictionaries:")
print(myfamily["child2"]["name"])
print("\n")

print("Loop Through Nested Dictionaries:")
for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])

print("\n")


print("Dictionaries Comprehsion:")

my_dict = {num:num**2 for num in range(1,11)}
print(my_dict)

random_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

my_new_dict = {k:v**2 for k,v in random_dict.items()}
print(my_new_dict)

my_new_dict2 = {k:v**2 for k,v in random_dict.items() if v % 2 == 0}
print(my_new_dict2)

print("\n")












































































































