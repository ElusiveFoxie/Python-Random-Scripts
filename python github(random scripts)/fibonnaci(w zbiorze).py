'''
x = 1
y = 2
z = x + y
a = z + y
b = a + z
'''
def calk(x,y):
    list = []
    while (x <= y):
        list.append(x)
        x += 1
    return list
d = int(input('poczatek zbioru: '))
e = int(input('koniec zbioru: '))

k = calk(d,e)
x = 0
y = 1
lista = [0,1]


for i in range(e):
    lista.append(lista[x] + lista[y])
    x += 1
    y += 1


wynik = list(set(k).intersection(set(lista)))
wynik.sort()


print(wynik)


