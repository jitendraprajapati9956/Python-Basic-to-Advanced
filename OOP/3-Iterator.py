print("----->Iterators<-----")
print("\n")


print("Iterator vs Iterable:")
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print("\n")
print("Strings are also iterable objects, containing a sequence of characters::")

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print("\n")


print("Looping Through an Iterator:")
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)

print("\n")

mystr = "banana"

for x in mystr:
    print(x)
print("\n")

print("Create an Iterator:")
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print("\n")


print("StopIteration:")
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
print("\n")





