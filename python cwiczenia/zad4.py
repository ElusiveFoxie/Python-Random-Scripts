x = int(input('podaj liczbe '))
k = 1
wynik = []
for i in range(x):
    if (x % k == 0):
        wynik.append(k)
        k += 1
    else:
        k += 1
print(wynik)
