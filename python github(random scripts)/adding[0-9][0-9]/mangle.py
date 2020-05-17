
f = open("words.txt", "r")
words = []
for x in f:
    y = x.replace('\n','')
    words.append(y)
f.close()

f2 = open("words.txt", "w")
for i in words:
    for k in range(0,99):
        f2.write(i+str(k)+'\n')
f2.close()

