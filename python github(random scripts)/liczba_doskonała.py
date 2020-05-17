

def dzielniki(x):
	k = 1
	wynik = 0
	for i in range(x):
		if (x%k==0):
			wynik += k
			k += 1
		else:
			k += 1
	wynik -= x
	return wynik

l =	int(input('podaj liczbe '))
y = dzielniki(l)


if (l == y):
	print(l, 'to liczba doskonała')
else:
	print('nope')
