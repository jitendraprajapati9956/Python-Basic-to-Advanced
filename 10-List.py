print("----->Lists<-----")
print("List items are ordered, changeable, and allow duplicate values.")
print("List items are indexed, the first item has index [0], the second item has index [1] etc")
print("\n")

thislist = ["apple", "banana", "cherry"]
print("thislist:",thislist)
print("\n")

print("Allow Duplicates:")
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print("thislist:",thislist)
print("\n")

print("List Length:")
thislist = ["apple", "banana", "cherry"]
print("length:",len(thislist))
print("\n")

print("List Items - Data Types:")
list1 = ["apple", "banana", "cherry"]
print("thislist:",list1)
list2 = [1, 5, 7, 9, 3]
print("thislist:",list2)
list3 = [True, False, False]
print("thislist:",list3)
print("\n")

list1 = ["abc", 34, True, 40, "male"]
print("thislist:",list1)
print("\n")

print("type():")
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
print("\n")

print("list() Constructor:")
thislist = list(("apple", "banana", "cherry")) # double round-brackets
print(thislist)
print("\n")

print("Python Collections (Arrays):")
print("Access Items:")
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print("\n")

print("Negative Indexing:")
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
print("\n")

print("Range of Indexes:")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
print("\n")

print("Check if Item Exists:")
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
print("\n")

print("Change List Items:")
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[1] = "blackcurrant"
print(thislist)
print("\n")

print("Change a Range of Item Values:")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist)
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
print("\n")

thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
print("\n")

thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[1:3] = ["watermelon"]
print(thislist)
print("\n")

print("Insert Items:")
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.insert(2, "watermelon")
print(thislist)
print("\n")

print("Add List Items:")
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.append("orange")
print(thislist)
print("\n")

print("Insert Items:")
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.insert(1, "orange")
print(thislist)
print("\n")

print("Extend List:")
thislist = ["apple", "banana", "cherry"]
print(thislist)
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
print("\n")

print("Add Any Iterable:")
thislist = ["apple", "banana", "cherry"]
print(thislist)
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
print("\n")

print("Remove List Items:")
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.remove("banana")
print(thislist)
print("\n")

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
print(thislist)
thislist.remove("banana")
print(thislist)
print("\n")

print("Remove Specified Index:")
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.pop(1)
print(thislist)
print("\n")

thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.pop()
print(thislist)
print("\n")

thislist = ["apple", "banana", "cherry"]
print(thislist)
del thislist[0]
print(thislist)
print("\n")

thislist2 = ["apple", "banana", "cherry"]
del thislist2
print(thislist2)
print("\n")

print("Clear the List:")
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.clear()
print(thislist)
print("\n")

print("Loop Lists:")
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
print("\n")

print("Loop Through the Index Numbers:")
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
print("\n")

print("Using a While Loop:")
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
print("\n")

print("Looping Using List Comprehension:")
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
print("\n")

print("List Comprehension:")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

print("\n")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
print("\n")

print("The Syntax")
print("newlist = [expression for item in iterable if condition == True]")
print("\n")

print("Condition:")
print("newlist = [x for x in fruits if x != 'apple']")
print("newlist = [x for x in fruits]")
print("\n")

print("Iterable:")
newlist = [x for x in range(10)]
print(newlist)
print("\n")
newlist = [x for x in range(10) if x < 5]
print(newlist)
print("\n")

print("Expression:")
newlist = [x.upper() for x in fruits]
print(newlist)
print("\n")

newlist = ['hello' for x in fruits]
print(newlist)
print("\n")

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
print("\n")

print("Sort Lists:")
print("Sort List Alphanumerically:")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(thislist)
thislist.sort()
print(thislist)
print("\n")

thislist = [100, 50, 65, 82, 23]
print(thislist)
thislist.sort()
print(thislist)
print("\n")

print("Sort Descending:")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(thislist)
thislist.sort(reverse = True)
print(thislist)
print("\n")

thislist = [100, 50, 65, 82, 23]
print(thislist)
thislist.sort(reverse = True)
print(thislist)
print("\n")

print("Customize Sort Function:")
def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
print("\n")

print("Case Insensitive Sort:")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(thislist)
thislist.sort()
print(thislist)
print("\n")

thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(thislist)
thislist.sort(key = str.lower)
print(thislist)
print("\n")

print("Reverse Order:")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(thislist)
thislist.reverse()
print(thislist)
print("\n")

print("Copy a List:")
thislist = ["apple", "banana", "cherry"]
print(thislist)
mylist = thislist.copy()
print(mylist)
print("\n")

thislist = ["apple", "banana", "cherry"]
print(thislist)
mylist = list(thislist)
print(mylist)
print("\n")


print("Join Two Lists:")
list1 = ["a", "b", "c"]
print("List1:",list1)
list2 = [1, 2, 3]
print("List2:",list2)
list3 = list1 + list2
print(list3)
print("\n")

list1 = ["a", "b" , "c"]
print("List1:",list1)
list2 = [1, 2, 3]
print("List2:",list2)
for x in list2:
    list1.append(x)

print(list1)
print("\n")

list1 = ["a", "b" , "c"]
print("List1:",list1)
list2 = [1, 2, 3]
print("List2:",list2)

list1.extend(list2)
print(list1)














