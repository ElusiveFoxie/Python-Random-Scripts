list = []
len = int(input('podaj dlugosc listy '))
min = int(input('parametr: mniejsze od '))
for i in range(len):
    x = int(input('podaj wartosc '+str(i+1)+' elementu z listy '))
    list.append(x)
print ('Twoja lista: 'list)
newlist = []
for i in range(len):
    if(list[i]<min):
        newlist.append(list[i])
print (newlist)


