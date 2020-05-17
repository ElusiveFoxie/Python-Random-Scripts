import math

x = int(input('podaj liczbe do sprawdzenia: '))

if(math.sqrt(x)%1==0):
    print ('pierwiastek jest całkowity')

else:
    print('pierwiastek nie jest całkowity')