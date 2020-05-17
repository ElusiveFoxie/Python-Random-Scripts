'''
x = 1
y = 2
z = x + y
a = z + y
b = a + z
'''

x = 0
y = 1
z = int(input('ile liczb: '))
lista = [0,1,2]


for i in range(z):
    lista.append(lista[x] + lista[y])
    x += 1
    y += 1

print(lista)