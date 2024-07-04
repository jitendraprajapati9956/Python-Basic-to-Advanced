print("----->If Else<-----")
print("\n")

print("If statement:")
a = 33
b = 200
if b > a:
    print("b is greater than a")
print("\n")

print("Indentation:")
a = 33
b = 200
if b > a:
    print("b is greater than a") # you will get an error
print("\n")

print("Elif:")
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
print("\n")

print("Else:")
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
print("\n")

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
print("\n")

print("Short Hand If:")
if a > b: print("a is greater than b")
print("\n")

print("Short Hand If ... Else:")
a = 2
b = 330
print("A") if a > b else print("B")
print("\n")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
print("\n")

print("And:")
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
print("\n")

print("Or:")
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")
print("\n")

print("Not:")
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")
print("\n")

print("Nested If:")
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

print("\n")

print("The pass Statement:")
a = 33
b = 200

if b > a:
    pass

print("\n")










































































