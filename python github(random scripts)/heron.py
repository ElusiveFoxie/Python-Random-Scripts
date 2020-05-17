import math

def heron(x,y,z):
	p = int((x+y+z)/2)
	wynik = math.sqrt(p*(p-x)*(p-y)*(p-z))
	print('Pole to: ',wynik)

x = float(input('podaj x: '))
y = float(input('podaj y: '))
z = float(input('podaj z: '))

heron(x,y,z)
    