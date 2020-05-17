x = str(input("podaj liczbe binarną: "))
x = x[::-1]

k=0

n = 0



for i in range(len(x)):
	if (x[n:n+1:1] == "1"):
		k = k + 2 ** (n)
		n += 1
		

	else:
		n += 1
print(k)
	
