print("----->Tuples<-----")
print("Tuple items are ordered, unchangeable, and allow duplicate values.")
print("Tuple items are indexed, the first item has index [0], the second item has index [1] etc.")
print("\n")


print("Create a Tuple:")
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print("\n")

print("Tuple Items:")
print("Allow Duplicates:")
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print("\n")

print("Tuple Length:")
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
print("\n")

print("Create Tuple With One Item:")
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
print("\n")

print("Data Types:")
tuple1 = ("apple", "banana", "cherry")
print("tuple1:",tuple1)
tuple2 = (1, 5, 7, 9, 3)
print("tuple2:",tuple2)
tuple3 = (True, False, False)
print("tuple3:",tuple3)
print("\n")

tuple1 = ("abc", 34, True, 40, "male")
print("tuple1:",tuple1)
print("\n")

print("type():")
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
print("\n")

print("tuple() Constructor:")
thistuple = tuple(("apple", "banana", "cherry")) # double round-brackets
print(thistuple)
print("\n")

print("Access Tuple Items:")
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
print("\n")

print("Negative Indexing:")
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
print("\n")

print("Range of Indexes:")
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
print("\n")

print("Check if Item Exists:")
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
print("\n")

print("Update Tuples:")
print("Change Tuple Values:")
x = ("apple", "banana", "cherry")
print("x:",x)
y = list(x)
print("y:",y)
y[1] = "kiwi"
print("y:",y)
x = tuple(y)
print("x:",x)
print("\n")

print("Add Items:")
thistuple = ("apple", "banana", "cherry")
print("this tuple:",thistuple)
y = list(thistuple)
print("y:",y)
y.append("orange")
thistuple = tuple(y)
print("this tuple:",thistuple)
print("\n")

print("Add tuple to a tuple.:")
thistuple = ("apple", "banana", "cherry")
print("this tuple:",thistuple)
y = ("orange",)
print("y:",y)
thistuple += y
print(thistuple)
print("\n")

print("Remove Items:")
thistuple = ("apple", "banana", "cherry")
print("this tuple:",thistuple)
y = list(thistuple)
print("y:",y)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
print("\n")

thistuple = ("apple", "banana", "cherry")
print("this tuple:",thistuple)
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists
print("\n")

print("Unpack Tuples:")
fruits = ("apple", "banana", "cherry")
print("fruits:",fruits)
print("\n")

fruits = ("apple", "banana", "cherry")
print("fruits:",fruits)
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
print("\n")

print("Using Asterisk*:")
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
print("fruits:",fruits)
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
print("\n")

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
print("fruits:",fruits)
(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
print("\n")

print("Loop Tuples:")
thistuple = ("apple", "banana", "cherry")
print("thistuple:",thistuple)
for x in thistuple:
    print(x)
print("\n")

print("Loop Through the Index Numbers:")
thistuple = ("apple", "banana", "cherry")
print("thistuple:",thistuple)
for i in range(len(thistuple)):
    print(thistuple[i])
print("\n")

print("Using a While Loop:")
thistuple = ("apple", "banana", "cherry")
print("thistuple:",thistuple)
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
print("\n")

print("Join Tuples:")
tuple1 = ("a", "b" , "c")
print("tuple1:",tuple1)
tuple2 = (1, 2, 3)
print("tuple2:",tuple2)
tuple3 = tuple1 + tuple2
print("tuple3:",tuple3)
print("\n")

print("Multiply Tuples:")
fruits = ("apple", "banana", "cherry")
print("fruits:",fruits)
mytuple = fruits * 2
print(mytuple)
print("\n")




















