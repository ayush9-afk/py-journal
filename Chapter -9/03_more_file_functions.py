f = open("file.txt")

lines = f.readlines()
print(lines, type(lines))

lines1 = f.readlines()
print(lines, type(lines1))

line = f.readline()
while(line !=""):
    print(line)
    line = f.readline()

    f.close()