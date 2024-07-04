import os

print("----->File Handling<-----")
print("\n")

f = open("file.txt", "r")
print(f.read())

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

f = open("myfile.txt", "x")

os.remove("demofile.txt")

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

