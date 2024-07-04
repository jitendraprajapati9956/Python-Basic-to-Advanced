print("----->String<-----")

print("Assign String to a Variable:")
y = "Jitendra Prajapati"
x = 'Hello,Jitendra'

print("y:",y)
print("x:",x)
print("\n")

print("Quotes Inside Quotes:")
print("Single or Double Quotes:")
print("Hello,Jitendra")
print("Hello,'Jitendra'")
print('"Hello,Jitendra"')
print("\n")

print("Multiline Strings:")
a = """
Hello, I am Jitendra
I am 22 Year old,I am Studying in
Master Of Computer Application
"""
print(a)
print("Or three single quotes:")
a = '''
Hello, I am Jitendra
I am 22 Year old,I am Studying in
Master Of Computer Application
'''
print(a)
print("\n")

print("Strings are Arrays:")
a = "Jitendra Prajapati"
print(a[1])
print("\n")

print("Looping Through a String:")
for x in "Jitendra":
    print(x)
print("\n")

print("String Length:")
a = "Jitendra Prajapati"
print(len(a))
print("\n")

print("Check String:")
txt = "Morning Since Walking Up"
print("Since" in txt)
print("Today" not in txt)
if "Since" in txt:
    print("Yes, 'Since' is present.")

print("\n")

print("Slicing Strings:")
b = "Jitendra Prajapati"
print(b[2:5])
print("Slice From the Start:")
b = "Jitendra Prajapati"
print(b[:5])
print("Slice To the End:")
print(b[2:])
print("Negative Indexing:")
print(b[-5:-2])
print("\n")

print("Modify Strings:")
print("Upper Case:")
b = "Jitendra, Prajapati"
print(b.upper())
print("Lower Case:")
print(b.lower())
print("Remove Whitespace:")
print(b.strip())
print("Replace String:")
print(a.replace("J", "N"))
print("Split String:")
print(a.split(","))
print("\n")

print("String Concatenation:")
a = "Hello"
b = "Jitendra"
c = a + b
print(c)

a = "Hello"
b = "Jitendra"
c = a + " " + b
print(c)
print("\n")

print("String Format:")
age = 22
# txt = "My name is Jitendra, I am " + age  #error age
#print(txt)

print("F-Strings:")
txt = f"My name is Jitendra, I am {age}"
print(txt)
print("\n")
print("Placeholders and Modifiers:")
price = 100
txt = f"The price is {price} rupees"
print(txt)
txt = f"The price is {price:.2f} rupees"
print(txt)
txt = f"The price is {20 * 59} rupees"
print(txt)
print("\n")

print("Escape Character:")
print("My name is Jitendra\'")
print("My name is Jitendra\\")
print("My name is Jitendra\n")
print("My name is Jitendra\r")
print("My name is Jitendra\t")
print("My name is Jitendra\b")
print("My name is Jitendra\f")
print("My name is Jitendra\000")

print("\n")

print("String Formatting:")
print("F-Strings:")
txt = f"The price is 49 rupees"
print(txt)
print("\n")

print("Placeholders and Modifiers:")
price = 59
txt = f"The price is {price} rupees"
print(txt)
print("\n")

price = 59
txt = f"The price is {price:.2f} rupees"
print(txt)
print("\n")

txt = f"The price is {95:.2f} rupees"
print(txt)
print("\n")

print("Perform Operations in F-Strings:")
txt = f"The price is {20 * 59} rupees"
print(txt)
print("\n")

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} rupees"
print(txt)
print("\n")

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)
print("\n")

print("Execute Functions in F-Strings:")
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)
print("\n")

def myconverter(x):
    return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)
print("\n")

print("More Modifiers:")

price = 59000
txt = f"The price is {price:,} rupees"
print(txt)
print("\n")





















