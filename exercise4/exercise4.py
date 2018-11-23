import os
directory = input("Directory: ")
file = input("Name of file: ")
path = directory + "/" + file + ".txt"
execute = "notepad.exe " + path
try:
    os.stat(directory)
except:
    os.mkdir(directory)
os.system(execute)
count = len(open(path).readlines())

if count == 0:
    print("puste")
    f = open("puste.txt", "a+")
    f.write(path + "\n")
    f.close()
elif count == 1:
    print("krótkie")
    f = open("krotkie.txt", "a+")
    f.write(path + "\n")
    f.close()
elif count < 10:
    print("średnie")
    f = open("srednie.txt", "a+")
    f.write(path + "\n")
    f.close()
else:
    print("długie")
    f = open("dlugie.txt", "a+")
    f.write(path + "\n")
    f.close()
