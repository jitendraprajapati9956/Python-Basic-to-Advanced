print("----->Data Types<-----")
print("\n")

print("Built-in Data Types:")
print("Text Type:	str")
print("Numeric Types:	int, float, complex")
print("Sequence Types:	list, tuple, range")
print("Mapping Type:	dict")
print("Set Types:	set, frozenset")
print("Boolean Type:	bool")
print("Binary Types:	bytes, bytearray, memoryview")
print("None Type:	NoneType")
print("\n")

print("Getting the Data Type:")
x = 5
print("x = 5")
print(type(x))


x = "Hello World"
print("x = Hello World")
print(type(x))

x = 20.5
print("x = 20.5")
print(type(x))

x = 1j
print("x = 1j")
print(type(x))

x = ["apple", "banana", "cherry"]
print("x = ['apple', 'banana', 'cherry']")
print(type(x))


x = ("apple", "banana", "cherry")
print("x = ('apple', 'banana', 'cherry')")
print(type(x))

x = range(6)
print("x = range(6)")
print(type(x))

x = {"name" : "Jitendra", "age" : 22}
print("x = {'name' : 'Jitendra', 'age' : 22}")
print(type(x))


x = {"apple", "banana", "cherry"}
print("x = {'apple', 'banana', 'cherry'}")
print(type(x))


x = frozenset({"apple", "banana", "cherry"})
print("x = frozenset({'apple', 'banana', 'cherry'})")
print(type(x))

x = True
print("x = True")
print(type(x))

x = b"Hello"
print("x = b'hello'")
print(type(x))

x = bytearray(5)
print("x = bytearray(5)")
print(type(x))

x = memoryview(bytes(5))
print("x = memoryview(bytes(5))")
print(type(x))

x = None
print("x = None")
print(type(x))

print("\n")

print("Setting the Specific Data Type:")
x = str("Hello World")
print(x)
x = int(20)
print(x)
x = float(20.5)
print(x)
x = complex(1j)
print(x)
x = list(("apple", "banana", "cherry"))
print(x)
x = tuple(("apple", "banana", "cherry"))
print(x)
x = range(6)
print(x)
x = dict(name="John", age=36)
print(x)
x = set(("apple", "banana", "cherry"))
print(x)
x = frozenset(("apple", "banana", "cherry"))
print(x)
x = bool(5)
print(x)
x = bytes(5)
print(x)
x = bytearray(5)
print(x)
x = memoryview(bytes(5))
print(x)