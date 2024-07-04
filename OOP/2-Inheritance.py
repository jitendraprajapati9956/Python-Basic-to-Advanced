print("----->Inheritance<-----")
print("\n")

print("Create a Parent Class:")

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Jitendra", "prajapati")
x.printname()
print("\n")

print("Create a Child Class:")
class Student(Person):
    pass

x = Student("Rajesh", "Prajapati")
x.printname()
print("\n")

print(" __init__() Function:")

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

x = Student("Rajesh", "Prajapati")
x.printname()
print("\n")

print("super() Function:")
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x = Student("Jitendra", "Prajapati")
x.printname()
print("\n")

print("Add Properties:")
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Jitendra", "Prajapati", 2025)
x.printname()
print("\n")

print("Add Methods:")
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the Graduation Year of", self.graduationyear)

x = Student("Jitendra", "Prajapati", 2025)
x.welcome()





























































