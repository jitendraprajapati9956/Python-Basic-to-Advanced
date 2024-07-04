import json
print("----->JSON<-----")
print("\n")

print("Parse JSON - Convert from JSON to Python")
# some JSON:
x =  '{ "name":"Jitendra", "age":22, "city":"Deesa"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
print("\n")

print("Convert from Python to JSON")
# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
print("\n")

print(json.dumps({"name": "Jitendra", "age": 22}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
print("\n")


x = {
    "name": "Mohanbhai",
    "age": 22,
    "married": True,
    "divorced": False,
    "children": ("Naran","Rajesh"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))

print("\n")

print("Format the Result")
json.dumps(x, indent=4)
json.dumps(x, indent=4, separators=(". ", " = "))


print("Order the Result")
json.dumps(x, indent=4, sort_keys=True)



