import os, zipfile

path = "C:\\Users\\mkacz\\OneDrive\\Desktop\\python_guide\\ZipBackUps"

num = 1

while ('BackUp_' + str(num) in os.listdir(path)):
    num +=1

newZip = zipfile.ZipFile('BackUp_'+str(num), 'w')
for dirname, subdirs, files in os.walk("folderToBackUp"):
    newZip.write(dirname)
    for filename in files:
        newZip.write(os.path.join(dirname, filename))
newZip.close()


