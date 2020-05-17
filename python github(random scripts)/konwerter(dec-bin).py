x = int(input("podaj liczbe: "))

k = ""
while(x!=0):
	if(x%2 == 1):
		k = k +"1"
		x = (x-1)/2
	elif(x%2 == 0):
		k = k + "0"
		x = x/2
	elif(x==1):
		k = k +"1"
		x -= 1

k = k[::-1]
	
print(k)
