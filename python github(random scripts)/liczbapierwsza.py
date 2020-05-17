import math

x = int(input('podaj liczbe do sprawdzenia: '))
i = 2
y = True
if (x == 1 or math.sqrt(x)%1==0):
    y = False
else:
    while(x > i):
        if (x % i == 0):
            y = False
            break
        i += 1

print (y)
