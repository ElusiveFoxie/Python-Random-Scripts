print("""PRESS 1 if Celsius to Farenheit
PRESS 2 id Celsius to Kelvin
PRESS 3 if Farenheit to Celsius
PRESS 4 if Farenheit to Kelvin 
PRESS 5 if Kelvin to Celsius
PRESS 6 if Kelvin to Farenheit """)

czy = int(input())
if (czy == 1):
    a = float(input("Podaj wartosc w Celsjuszach "))
    b = 32 + 1.8 * a
    print(b, "Farenheit")

elif (czy == 2):
    ab = float(input("Podaj wartosc w Celsjuszach "))
    bb = ab + 273.15
    print(bb, "Kelvin")

elif (czy == 3):
    cb = float(input("Podaj wartosc w Farenheit "))
    db = (cb - 32) / 1.8
    print (db, "Celsius")

elif (czy == 4):
    e = float(input("Podaj wartosc w Farenheit "))
    f = 255.372222 + e * 0.555556
    print (f, "Kelvin")

elif (czy == 5):
    eb = float(input("Podaj wartosc w Kelwinach "))
    fb = eb - 273.15
    print(fb, "Celsius")

elif (czy == 6):
    g = float(input("Podaj wartosc w Kelwinach "))
    h = (g - 255.372222) / 0.555556
    print (h, "Farenheit")

else:
    print("Wybrales zly numer, sprobuj ponownie")


