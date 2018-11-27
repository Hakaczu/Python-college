import os
import datetime
// ogólnie nie ma żadnej walidacji tego co ktoś wpisze xd
// directory = input("Directory: ")
directory = input("Directory: ")
while not os.path.isdir(folder) and folder != '':
    print('invalid folder, try again')
    directory = str(input("Directory: "))

// według polecenia nazwa pliku powinna być datą
// file = input("Name of file: ")
date = datetime.datetime.now()
file = str(date).replace(':', '') + '.txt'
// ścieżka jest inna pod windowsem a inna pod unixem/linuxem dlatego lepiej użyć os.path.join()
// path = directory + "/" + file + ".txt"
path = os.path.join(directory, file + ".txt")
execute = "notepad.exe " + path

// sprawdzasz czy istnieje coś co ma nazwę directory i czy da się to czytać - nie sprawdzasz czy jest folderem
// https://docs.python.org/2/library/stat.html
// try:
//     os.stat(directory)
// except:
//     os.mkdir(directory)
if not os.path.isdir(directory):
    try:
        os.mkdir(directory)
    except Exception as e:
        print(e)
        
os.system(execute)
count = len(open(path).readlines())

// obczaj coś takiego jak with open() - po zakończeniu bloku nie trzeba pamiętać o .close()
// np.
// if counter == 0:
//     with open("puste.txt", 'a+') as f:
//         f.write(path + '\n')
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
