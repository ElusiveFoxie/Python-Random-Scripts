import random

x = int(input('liczba znakow w hasle '))
haslo=''

for i in range(x):
    haslo += chr(random.randint(33,126))

print(haslo)