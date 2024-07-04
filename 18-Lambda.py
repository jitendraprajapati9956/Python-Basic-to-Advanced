import functools

print("----->Lambda<-----")
print("\n")

print("Syntax")
print("lambda arguments : expression")
print("\n")

print("Add 10 to argument a, and return the result:")
x = lambda a : a + 10
print(x(5))
print("\n")

print("Lambda functions can take any number of arguments::")
x = lambda a, b : a * b
print(x(5, 6))
print("\n")

print("Summarize argument a, b, and c and return the result::")
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
print("\n")

print("Why Use Lambda Functions?:")
print("Functions:")
def myfunc(n):
    return lambda a : a * n

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
print("\n")

def myfunc(n):
    return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))




my_list = [1,2,3,4,5]

print(list(map(lambda item: item*2, my_list)))

print(list(filter(lambda item: item % 2 != 0, my_list)))

print(functools.reduce(lambda acc,item: item+acc, my_list))

'''
syntax:
lambda param: action(param)
it automatically returns the action taken,
it do not have any name, doesn't get stored in the memory.
and so used only once.
and behaves exactly like a function.
'''


a = [(0,2),(4,4),(10,-1),(5,3)]

a.sort(key=lambda x:x[1], reverse=False)
print(a)














