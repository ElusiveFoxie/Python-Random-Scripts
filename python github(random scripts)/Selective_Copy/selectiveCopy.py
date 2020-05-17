'''
Write a program that walks through a folder tree and searches for files
with a certain file extension (such as .pdf or .jpg). Copy these files
from whatever location they are in to a new folder.
'''

import os, re, shutil

pathFrom = "C:\\Users\\mkacz\\OneDrive\\Desktop\\python_guide\\Selective_Copy\\folderToSearchIn"
pathTo = "C:\\Users\\mkacz\\OneDrive\\Desktop\\python_guide\\Selective_Copy\\FolderToCopyIn"

try:
    os.mkdir(pathTo)
except OSError:
    print ("Creation of the directory %s failed" % pathTo)
else:
    print ("Successfully created the directory %s " % pathTo)

#PdfRegex = re.compile(r'\S*?\.pdf')
JpgRegex = re.compile(r'\S*\.jpg')

for folderName, subfolders, filenames in os.walk(pathFrom):

    for filename in filenames:
        string = folderName + '\\'+ filename
        find1 = JpgRegex.findall(string)
        if (find1 != []):
            print(find1[0])
            shutil.copy(find1[0], pathTo)










