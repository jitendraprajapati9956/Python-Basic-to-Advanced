print("----->Classes and Objects<-----")
print("\n")

print("Create a Class:")
class MyClass:
    x = 5

print("Create Object:")
p1 = MyClass()
print(p1.x)
print("\n")

print("__init__() Function:")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Jitendra", 22)

print(p1.name)
print(p1.age)
print("\n")

print("__str__() Function:")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Jitendra", 22)

print(p1)
print("\n")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("Jitendra", 22)

print(p1)
print("\n")

print("Object Methods:")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("Jitendra", 22)
p1.myfunc()
print("\n")

print("self Parameter:")
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("Jitendra", 22)
p1.myfunc()
print("\n")

print("Modify Object Properties:")
p1.age = 40

print("Delete Object Properties:")
del p1.age

print("Delete Objects:")
del p1

print("pass Statement:")
class Person:
    pass
print("\n")


class OurOwnRange():
    current = 0
    def __init__(self,first,last):
        self.first = first
        self.last = last
        
    def __iter__(self):
        return self
    
    def __next__(self):
        print("hehehheh")
        # if self.current < self.last:
        #     num = OurOwnRange.current
        #     OurOwnRange.current += 1
        #     return num
        # raise StopIteration
    
gen = OurOwnRange(0,10)
print(gen)

for i in gen:
    print(i)

'''
loops by default deal with StopIteration error. they have build in functionality to handle them.
'''








































