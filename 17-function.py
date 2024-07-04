print("----->Functions<-----")
print("\n")

print("Creating a Function:")

def my_function():
    print("Hello from a function")
print("\n")


print("Calling a Function:")
def my_function():
    print("Hello from a function")

my_function()
print("\n")

print("Arguments:")
def my_function(fname):
    print(fname + " Prajapati")

my_function("Naran")
my_function("Rajesh")
my_function("kishan")
print("\n")

print("Number of Arguments:")
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Naran", "Rajesh")
print("\n")

print("Arbitrary Arguments, *args:")
def my_function(*kids):
    print("The youngest child is " + kids[1])

my_function("Naran", "Rajesh", "Kishan")
print("\n")

print("Keyword Arguments:")
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Naran", child2 = "Kishan", child3 = "Rajesh")
print("\n")

print("Arbitrary Keyword Arguments, **kwargs:")
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Rajesh", lname = "Prajapati")
print("\n")

print("Default Parameter Value:")
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
print("\n")

print("Passing a List as an Argument:")
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
print("\n")

print("Return Values:")
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
print("\n")

print("pass Statement:")
def myfunction():
    pass
print("\n")

print("Positional-Only Arguments:")
def my_function(x, /):
    print(x)

my_function(3)
print("\n")

def my_function(x):
    print(x)

my_function(x = 3)
print("\n")

print("Keyword-Only Arguments:")
def my_function(*, x):
    print(x)

my_function(x = 3)

def my_function(x):
    print(x)

my_function(3)
print("\n")

print("Combine Positional-Only and Keyword-Only:")
def my_function(a, b, /, *, c, d):
    print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
print("\n")


def multiply_by2(li):
    new_li = []
    for item in li:
        new_li.append(item)
    return new_li

print(multiply_by2([5,6,8]))

'''
If we define 'new_li' outside the function, or print something inside the function, then it is no longer
a pure function.
'''


















