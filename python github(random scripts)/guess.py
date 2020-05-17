import random
guess = int(random.randrange(0,20))
print ("zgadnij liczbe z przedziału od 0-20")
k = False
x = int(input("podaj liczbe "))
while (k == False):
	if( x == guess):
		print("brawo")
		k = True
	elif( x < guess):
		print ("twoja liczba jest za mała")
		x = int(input("podaj liczbe "))
	elif( x > guess):
		print ("twoja liczba jest za duża")
		x = int(input("podaj liczbe "))

