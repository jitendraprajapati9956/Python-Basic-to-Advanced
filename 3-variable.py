
print("----->Variables<-----")

print("Creating Variables:")
x = 5
y = "Jitendra Prajapati"
print("x:",x)
print("y:",y)
print("\n")

print("----->Casting<-----")
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)

print("x:",x)
print("y:",y)
print("z:",z)
print("\n")

print("----->Get the Type<-----")
print(x)
print(type(x))

print(y)
print(type(y))

print(z)
print(type(z))
print("\n")
print("----->Case-Sensitive<-----")
x = 5
X = "jitendra"
print("x:",x)
print("X:",X)
print("\n")
print("----->Variable Names<-----")
print("legal Variable names:")
myvar = "Jitendra"
my_var = "Jitendra"
_my_var = "Jitendra"
myVar = "Jitendra"
MYVAR = "Jitendra"
myvar2 = "Jitendra"
print("myvar")
print("my_var")
print("_my_var")
print("myVar")
print("MYVAR")
print("myvar2")
print("\n")

print("ilegal Variable names:")
print("2myvar")
print("my-var")
print("my var")
print("\n")

print("Multi Words Variable Names:")
print("Camel Case:")
myvariableName = "Jitendra"   #each word ,except first,start in capital letter
print("myvariableName:",myvariableName)
print("\n")

print("Pascal Case:")
MyVariableName = "Jitendra"   #start in capital letter
print("MyVariableName:",MyVariableName)
print("\n")

print("Snake Case:")
my_variable_name = "Jitendra"  #each word is by underscore character
print("my_variable_name:",my_variable_name)
print("\n")


print("----->Assign Multiple Values<-----")
x, y, z = "C", "JAVA", "Python"
print("x:",x)
print("y:",y)
print("z:",z)
print("\n")

print("One Value to Multiple Variables:")
x = y = z = "C"
print("x:",x)
print("y:",y)
print("z:",z)
print("\n")


print("Unpack a Collection:")
language = ["C", "JAVA", "Python"]
x, y, z = language
print("x:",x)
print("y:",y)
print("z:",z)
print("\n")

print("----->Output Variables<-----")
x = "Python is awesome"
print("x:",x)

x = "Python"
y = "is"
z = "awesome"
print("x,y,z:",x, y, z)

x = "Python "
y = "is "
z = "awesome"
print("x+y+z:",x + y + z)

x = 5
y = 10
print("x+y",x + y)
print("\n")

print("----->Global Variables<-----")
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)
print("\n")

print("----->global Keyword<-----")
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)