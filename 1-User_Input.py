print("----->User Input<-----")
print("\n")


print("User Input:")

username = input("Enter username:")
print("Username is: " + username)
print("\n")

print("\n")


print("Fibbnocci Series:")


def fib(num):
    a = 0
    b= 1
    li=[]
    for i in range(num):
        li.append(a)
        temp = a
        a = b
        b = temp + b
    print(li)

num = int(input("Enter a number: "))
fib(num)


def fib(num):
    a = 0
    b= 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b

num = int(input("Enter a number: "))

for i in fib(num):
    print(i)




























































