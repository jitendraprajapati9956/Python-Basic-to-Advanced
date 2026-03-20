class Stack():

    def __init__(self):
        self.array = []

    def peek(self):
        return self.array[len(self.array)-1]

    def push(self, data):
        self.array.append(data)
        return

    def pop(self):
        if len(self.array)!= 0:
            self.array.pop()
            return
        else:
            print("Stack Empty")
            return

    def print_stack(self):
        for i in range(len(self.array)-1, -1, -1):
            print(self.array[i])
        return



my_stack = Stack()
my_stack.push("Andrei's")
my_stack.push("Courses")
my_stack.push("Are")
my_stack.push("Awesome")
my_stack.print_stack()
#Awesome
#Are
#Courses
#Andrei's

my_stack.pop()
my_stack.pop()
my_stack.print_stack()
#Courses
#Andrei's

print(my_stack.peek())
#Courses

print(my_stack.__dict__)
#{'array': ["Andrei's", 'Courses']}


'''Stacks can be implemented in Python in two more ways.
1. Using the 'deque' class from 'collections' module. Same methods used in lists, append and pop are used in deques
2. Using 'LifoQueue' from the 'queue' module . 'put()' and 'get()' methods are used for pushing and popping. It comes with some other useful metjods async well. 
'''
