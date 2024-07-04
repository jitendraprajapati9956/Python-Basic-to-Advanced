import createmodule
#import createmodule as mx
import platform
print("----->Modules<-----")
print("\n")

print("Create a Module:")
'''
def greeting(name):
    print("Hello, " + name)
'''

print("Use a Module:")
createmodule.greeting("Jitendra Prajapati")
print("\n")


print("Variables in Module:")

a = createmodule.person1["age"]
print(a)
print("\n")


print("Naming a Module:")

a = createmodule.person1["age"]
print(a)
print("\n")


print("Built-in Modules:")
x = platform.system()
print(x)
print("\n")

print("Using the dir() Function:")
x = dir(platform)
print(x)
print("\n")















