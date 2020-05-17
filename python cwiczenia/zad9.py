import random
x = random.randint(1,9)
y = input('zgadnij liczbe ')
z = 1
if (y != 'exit'):
    while (x!=int(y)):
        print('nie zgadles')
        y = int(input('sprobuj jeszcze raz '))
        z += 1
    print ('brawo zgadles za ',z,' razem')
