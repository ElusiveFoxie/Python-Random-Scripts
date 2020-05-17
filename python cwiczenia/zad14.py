
import random

x = random.randint(0, 30)
y = int(input('podaj dlugosc listy: '))

a = []

for i in range(y):
    a.append(x)
    x = random.randint(0, 30)

a = set(a)
a = list(a)

print(a)
