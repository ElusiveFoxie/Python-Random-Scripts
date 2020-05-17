d = int(input('podaj dzien '))
m = int(input('podaj mies '))
r = int(input('podaj rok '))
k = 0

if(r%4==0):
	tablica = [31,29,31,30,31,30,31,31,30,31,30,31]
else:
	tablica = [31,28,31,30,31,30,31,31,30,31,30,31]
k = d

if(m!=1):
	for i in range(m - 1):
		k = k + tablica[i]

print (k)

