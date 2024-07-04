print("----->Booleans<-----")
print("Boolean Values:")

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

print("if-else:")
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
print("\n")

print("Evaluate Values and Variables:")
print(bool("Hello"))
print(bool(15))
print("Evaluate two variables:")
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print("Most Values are True:")
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

print("Some Values are False:")
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
print("\n")
print("function:")

class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

print("Functions can Return a Boolean:")
def myFunction() :
    return True

print(myFunction())

def myFunction() :
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")

print("isinstance() function:")
x = 200
print(isinstance(x, int))