print("----->Recursion<-----")
print("\n")

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)
print("\n")


def iterative_factorial(number):
    f = 1
    for i in range(1, number+1):
        f = f * i
    return f

print(iterative_factorial(0))
#1
print(iterative_factorial(5))
#120
print(iterative_factorial(50))
#30414093201713378043612608166064768844377641568960512000000000000

def recursive_factorial(number):
    if number <= 1:
        return 1
    else:
        return number * recursive_factorial(number-1)

print(recursive_factorial(0))
#1
print(recursive_factorial(5))
#120
print(recursive_factorial(50))
#30414093201713378043612608166064768844377641568960512000000000000
print(recursive_factorial(1000))
#RecursionError: maximum recursion depth exceeded in comparison

print("\n")

#Given a number, we have to return the number at that index of the fibonacci sequence.
#Fibonacci Sequence - 0 1 1 2 3 5 8 13 21 34 55 89 144 . . . .
#For example, fibonacci(5) should return 5 as the 5th index (staring from 0) of the fibonacci sequence is the number 5
#Again , we will do both the iterative and recursive solutions

def iterative_fibonacci(index):
    first_number = 0
    second_number = 1
    if index == 0:
        return first_number
    if index == 1:
        return second_number
    for i in range(2,index +1):
        third_number = first_number + second_number
        first_number = second_number
        second_number = third_number
    return third_number

print(iterative_fibonacci(0))  #0
print(iterative_fibonacci(1))  #1
print(iterative_fibonacci(5))  #5
print(iterative_fibonacci(7))  #13
print(iterative_fibonacci(10)) #55
print(iterative_fibonacci(12)) #144

print("\n")


def recursive_fibonacci(index):
    if index == 0: #Base case 1
        return 0
    if index == 1: #Base case 2
        return 1
    return  recursive_fibonacci(index-1) + recursive_fibonacci(index-2) #Every term in fib sequence = sum of previous two terms

print(recursive_fibonacci(0))   #0
print(recursive_fibonacci(1))   #1
print(recursive_fibonacci(5))   #5
print(recursive_fibonacci(7))   #13
print(recursive_fibonacci(10))  #55
print(recursive_fibonacci(12))  #144

print("\n")

#Given a string , we need to reverse it using recursion (and iteration)
#For example, input = "Zero To Mastery", output = "yretsaM oT oreZ"

#First we will implement the iterative solution
def iterative_reverse(string): #Here we use a second string to store the reversed version. Time and Space complexity = O(n)
    reversed_string = ''
    for i in range(len(string)):
        reversed_string = reversed_string + string[len(string)-i-1]
    return reversed_string

print(iterative_reverse("Zero To Mastery"))
#yretsaM oT oreZ

#Here we append the string backwards into the original string itself and then slice it to contain only the 2nd half,i.e.,the reversed part.
#Time complexity = O(n). Space complexity = O(n)
def second_iterative_reverse(string):
    original_length = len(string)
    for i in range(original_length):
        string = string + string[original_length - i - 1]
    string = string[original_length:]
    return string

print(second_iterative_reverse("Zero To Mastery"))
#yretsaM oT oreZ


def recursive_reverse(string):
    print(string)
    if len(string) == 0:
        return string
    else:
        return recursive_reverse(string[1:]) + string[0]

print(recursive_reverse("Zero To Mastery"))
'''
Zero To Mastery
ero To Mastery
ro To Mastery
o To Mastery
 To Mastery
To Mastery
o Mastery
 Mastery
Mastery
astery
stery
tery
ery
ry
y

yretsaM oT oreZ
'''