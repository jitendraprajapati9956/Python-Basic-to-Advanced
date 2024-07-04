print("----->Sets<-----")
print("Sets are used to store multiple items in a single variable.")
print("A set is a collection which is unordered, unchangeable*, and unindexed.")
print("\n")

print("Create a Set:")
thisset = {"apple", "banana", "cherry"}
print(thisset)
print("\n")

print("Duplicates Not Allowed:")
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
print("\n")

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
print("\n")

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
print("\n")

print("Get the Length of a Set:")
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
print("\n")

print("Data Types:")
set1 = {"apple", "banana", "cherry"}
print("set1:",set1)
set2 = {1, 5, 7, 9, 3}
print("set2",set2)
set3 = {True, False, False}
print("set3",set3)
print("\n")

set1 = {"abc", 34, True, 40, "male"}
print("set1:",set1)
print("\n")

print("type():")
myset = {"apple", "banana", "cherry"}
print(type(myset))
print("\n")

print("set() Constructor:")
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
print("\n")

print("Access Set Items:")
thisset = {"apple", "banana", "cherry"}
print(thisset)
for x in thisset:
    print(x)
print("\n")

thisset = {"apple", "banana", "cherry"}
print(thisset)
print("banana" in thisset)
print("\n")

thisset = {"apple", "banana", "cherry"}
print(thisset)
print("banana" not in thisset)
print("\n")

print("Change Items:")
print("Once a set is created, you cannot change its items, but you can add new items.")
print("\n")


print("Add Set Items:")
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.add("orange")
print(thisset)
print("\n")


print("Add Sets:")
thisset = {"apple", "banana", "cherry"}
print("thisset:",thisset)
tropical = {"pineapple", "mango", "papaya"}
print("tropical:",tropical)

thisset.update(tropical)
print("thisset:",thisset)
print("\n")

print("Add Any Iterable:")
thisset = {"apple", "banana", "cherry"}
print("thisset:",thisset)
mylist = ["kiwi", "orange"]
print("mylist:",mylist)
thisset.update(mylist)
print("thisset:",thisset)
print("\n")

print("Remove Set Items:")
thisset = {"apple", "banana", "cherry"}
print("thisset:",thisset)
thisset.remove("banana")
print(thisset)
print("\n")

thisset = {"apple", "banana", "cherry"}
print("thisset:",thisset)
thisset.discard("banana")
print(thisset)
print("\n")

thisset = {"apple", "banana", "cherry"}
print("thisset:",thisset)
x = thisset.pop()
print(x)
print(thisset)
print("\n")

thisset = {"apple", "banana", "cherry"}
print("thisset:",thisset)
thisset.clear()
print(thisset)
print("\n")


thisset = {"apple", "banana", "cherry"}
print("thisset:",thisset)
del thisset
#print(thisset)
print("\n")


print("Loop Items:")
thisset = {"apple", "banana", "cherry"}
print("thisset:",thisset)
for x in thisset:
    print(x)
print("\n")

print("Join Sets:")
print("The union() and update() methods joins all items from both sets.")
print("The intersection() method keeps ONLY the duplicates.")
print("The difference() method keeps the items from the first set that are not in the other set(s).")
print("The symmetric_difference() method keeps all items EXCEPT the duplicates.")
print("\n")

print("Union:")
set1 = {"a", "b", "c"}
print("set1",set1)
set2 = {1, 2, 3}
print("set2",set2)
set3 = set1.union(set2)
print("set3",set3)
print("\n")

set1 = {"a", "b", "c"}
print("set1",set1)
set2 = {1, 2, 3}
print("set2",set2)
set3 = set1 | set2
print("set3",set3)
print("\n")

print("Join Multiple Sets:")
set1 = {"a", "b", "c"}
print("set1",set1)
set2 = {1, 2, 3}
print("set2",set2)
set3 = {"Jitendra", "Rajesh"}
print("set3",set3)
set4 = {"apple", "bananas", "cherry"}
print("set4",set4)

myset = set1.union(set2, set3, set4)
print(myset)
print("\n")

set1 = {"a", "b", "c"}
print("set1",set1)
set2 = {1, 2, 3}
print("set2",set2)
set3 = {"Jitendra", "Rajesh"}
print("set3",set3)
set4 = {"apple", "bananas", "cherry"}
print("set4",set4)
myset = set1 | set2 | set3 |set4
print(myset)
print("\n")

print("Join a Set and a Tuple:")
x = {"a", "b", "c"}
print("x:",x)
y = (1, 2, 3)
print("y:",y)
z = x.union(y)
print("z:",z)
print("\n")

print("Update:")
set1 = {"a", "b", "c"}
print("set1",set1)
set2 = {1, 2, 3}
print("set2:",set2)
set1.update(set2)
print("set1",set1)
print("\n")

print("Intersection:")
set1 = {"apple", "banana", "cherry"}
print("set1:",set1)
set2 = {"google", "microsoft", "apple"}
print("set2:",set2)
set3 = set1.intersection(set2)
print("set3:",set3)
print("\n")

set1 = {"apple", "banana", "cherry"}
print("set1:",set1)
set2 = {"google", "microsoft", "apple"}
print("set2:",set2)
set3 = set1 & set2
print("set3:",set3)
print("\n")

set1 = {"apple", "banana", "cherry"}
print("set1:",set1)
set2 = {"google", "microsoft", "apple"}
print("set2:",set2)
set1.intersection_update(set2)
print("set1:",set1)
print("\n")

set1 = {"apple", 1,  "banana", 0, "cherry"}
print("set1:",set1)
set2 = {False, "google", 1, "apple", 2, True}
print("set2:",set2)
set3 = set1.intersection(set2)
print("set3:",set3)
print("\n")

print("Difference:")
set1 = {"apple", "banana", "cherry"}
print("set1:",set1)
set2 = {"google", "microsoft", "apple"}
print("set2:",set2)
set3 = set1.difference(set2)
print("set3:",set3)
print("\n")

set1 = {"apple", "banana", "cherry"}
print("set1:",set1)
set2 = {"google", "microsoft", "apple"}
print("set2:",set2)
set3 = set1 - set2
print("set3:",set3)
print("\n")

set1 = {"apple", "banana", "cherry"}
print("set1:",set1)
set2 = {"google", "microsoft", "apple"}
print("set2:",set2)
set1.difference_update(set2)
print("set1:",set1)
print("\n")

print("Symmetric Differences:")
set1 = {"apple", "banana", "cherry"}
print("set1:",set1)
set2 = {"google", "microsoft", "apple"}
print("set2:",set2)
set3 = set1.symmetric_difference(set2)
print("set3:",set3)
print("\n")

set1 = {"apple", "banana", "cherry"}
print("set1:",set1)
set2 = {"google", "microsoft", "apple"}
print("set2:",set2)
set3 = set1 ^ set2
print("set3:",set3)
print("\n")

set1 = {"apple", "banana", "cherry"}
print("set1:",set1)
set2 = {"google", "microsoft", "apple"}
print("set2:",set2)
set1.symmetric_difference_update(set2)
print("set1:",set1)
print("\n")



print("List & set Comprehesion:")
my_list = []

for item in 'hello':
    my_list.append(item)

print(my_list)

my_list1 = [item for item in 'Jitendra']
print(my_list1)

my_list2 = [num**2 for num in range(1,11)]
print(my_list2)

# only even squares
my_set = {num**2 for num in range(1,11) if num**2 % 2 == 0}
print(my_set)
# remember that set don't contain duplicate values
