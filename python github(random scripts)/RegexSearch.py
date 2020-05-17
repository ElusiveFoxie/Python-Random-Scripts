import os, re
x = input("User Regex: ")
UserRegex = re.compile(x)
FileRegex = re.compile(r'\S+.txt')
files = os.listdir(os.curdir)
str = " ".join(files)

findList = FileRegex.findall(str)

for i in range(len(findList)):
    with open(findList[i]) as f:
        print(f.name.center(40, '='))
        for line in f:
            print(UserRegex.findall(line))

