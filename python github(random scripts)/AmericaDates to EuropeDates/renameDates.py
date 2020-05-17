import os, re, shutil

list102 = [1,0,2]
str = ""
listEu = []
pathEurope = "C:\\Users\\mkacz\\OneDrive\\Desktop\\python_guide\\AmericaDates to EuropeDates\\europe"
pathAmerica = "C:\\Users\\mkacz\\OneDrive\\Desktop\\python_guide\\AmericaDates to EuropeDates\\america"

try:
    os.mkdir(pathEurope)
except OSError:
    print ("Creation of the directory %s failed" % pathEurope)
else:
    print ("Successfully created the directory %s " % pathEurope)

list0 = os.listdir(pathAmerica)
list = " ".join(list0)

americaRegex = re.compile(r'(\d{2})\.(\d{2})\.(\d{4})')
find1 = americaRegex.findall(list)
length = len(find1)

for k in range(length):
    for i in list102:
        str += find1[k][i]+"."
    listEu.append(str)
    str = ""

for i in range(length):
    listEu[i] += "txt"

for i in range(length):
    shutil.copy(pathAmerica+"\\"+list0[i], pathEurope+"\\"+listEu[i])








