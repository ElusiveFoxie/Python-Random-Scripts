import random

x = random.randint(0, 30)
y = int(input('podaj dlugosc 1 listy: '))
z = int(input('podaj dlugosc 2 listy: '))
a = []
b = []
c = []
for i in range(y):
    a.append(x)
    x = random.randint(0, 30)

for i in range(z):
    b.append(x)
    x = random.randint(0, 30)

if (len(a)>len(b)):
    for i in b:
        if i in a:
            c.append(i)
else:
    for i in a:
        if i in b:
            c.append(i)


print(a)
print(b)
print(c)
