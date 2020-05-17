
f = open("names.txt", "r")
words = []
for x in f:
    y = x.replace('\n','')
    words.append(y)
f.close()

f2 = open("result.txt", "w")
for i in words:
    f2.write(i+'@mail.com\n')

f2.close()

