#! python3
newFileName = input("Enter new file's name: ")


adj = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
noun2 = input("Enter a noun: ")

dict = {"ADJECTIVE":adj, "NOUN":noun, "VERB":verb,}

with open('text.txt','r') as file:
    string = file.read()

for i in dict.keys():
    string = string.replace(i, dict[i],1)

string = string.replace("NOUN", noun2)

with open(newFileName+".txt", 'a') as newFile:
    newFile.write(string)