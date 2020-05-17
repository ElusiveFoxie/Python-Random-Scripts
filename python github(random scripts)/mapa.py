
d = float(input("Podaj deklinacje(w stopniach): "))
declinationYear = float(input("Podaj rok deklinacji: "))
actualYear = float(input("Podaj aktualny rok: "))
declinationChange1 = float(input("Podaj zmiane deklinacji w ciagu roku(w minutach): "))
declinationChange2 = declinationChange1 / 60

windDir = str(input("Podaj kierunek wiatru(N,E,S,W): "))
pw1 = float(input("Podaj poprawke na wiatr w kursie bajdewind: "))
pw2 = float(input("Podaj poprawke na wiatr w kursie polwiatr: "))
pw3 = float(input("Podaj poprawke na wiatr w kursie baksztag i fordewind: "))

pp = float(input("Podaj poprawke na prady(jesli nie wystepuja wpisz 0): "))

actualDeclination = (actualYear - declinationYear) * declinationChange2  + d

KK = float(input("Podaj Kurs Kompasowy(w stopniach: "))
deviation = float(input("Podaj dewiację dla Kursu kompasowego: "))

cp = actualDeclination + deviation

NK1 = float(input("Podaj 1. namiar kompasowy: "))
NK2 = float(input("Podaj 2. namiar kompasowy: "))

NR1 = NK1 + cp 
NR2 = NK2 + cp


if (windDir == "N"):
    if (KK > 0 and KK < 90):
        courseByTheWind = str("bajdewind")
        pw = pw1
    elif (KK < 360 and KK > 270):
        courseByTheWind = str("bajdewind")
        pw = - pw1
    elif (KK == 90):
        courseByTheWind = str("polwiatr")
        pw = pw2
    elif (KK == 270):
        courseByTheWind = str("polwiatr")
        pw = - pw2
    elif (KK > 90 and KK < 180):
        courseByTheWind = str("baksztag")
        pw = pw3
    elif (KK > 180 and KK < 270):
        courseByTheWind = str("baksztag")
        pw = -pw3
    elif (KK == 180):
        courseByTheWind = str("fordewind")
        pw = 0
    elif (KK == 0):
        courseByTheWind = str("mordewind")
        pw = 0

elif (windDir == "E"):
    if (KK > 90 and KK < 180):
        courseByTheWind = str("bajdewind")
        pw = pw1
    elif (KK < 90 and KK > 0):
        courseByTheWind = str("bajdewind")
        pw = - pw1
    elif (KK == 180):
        courseByTheWind = str("polwiatr")
        pw = pw2
    elif (KK == 360):
        courseByTheWind = str("polwiatr")
        pw = - pw2
    elif (KK > 180 and KK < 270):
        courseByTheWind = str("baksztag")
        pw = pw3
    elif (KK > 270 and KK < 360):
        courseByTheWind = str("baksztag")
        pw = -pw3
    elif (KK == 270):
        courseByTheWind = str("fordewind")
        pw = 0
    elif (KK == 90):
        courseByTheWind = str("mordewind")
        pw = 0

elif (windDir == "S"):
    if (KK > 180 and KK < 270):
        courseByTheWind = str("bajdewind")
        pw = pw1
    elif (KK < 180 and KK > 90):
        courseByTheWind = str("bajdewind")
        pw = - pw1
    elif (KK == 270):
        courseByTheWind = str("polwiatr")
        pw = pw2
    elif (KK == 90):
        courseByTheWind = str("polwiatr")
        pw = - pw2
    elif(KK > 270 and KK < 360):
        courseByTheWind = str("baksztag")
        pw = pw3
    elif(KK > 0 and KK < 90):
        courseByTheWind = str("baksztag")
        pw = -pw3
    elif(KK == 360):
        courseByTheWind = str("fordewind")
        pw = 0
    elif(KK == 180):
        courseByTheWind = str("mordewind")
        pw = 0

elif (windDir == "W"):
    if (KK > 270 and KK < 360):
        courseByTheWind = str("bajdewind")
        pw = pw1
    elif(KK < 270 and KK > 180):
        courseByTheWind = str("bajdewind")
        pw = - pw1
    elif(KK == 360):
        courseByTheWind = str("polwiatr")
        pw = pw2
    elif(KK == 180):
        courseByTheWind = str("polwiatr")
    elif (KK > 0 and KK < 90):
        courseByTheWind = str("baksztag")
        pw = pw3
    elif (KK > 90 and KK < 180):
        courseByTheWind = str("baksztag")
        pw = -pw3
    elif (KK == 90):
        courseByTheWind = str("fordewind")
        pw = 0
    elif (KK == 270):
        courseByTheWind = str("mordewind")
        pw = 0

KDd = KK + actualDeclination + deviation + pw + pp
print("KK= ", KK)
print("Dewiacja= ", deviation)
print("Deklinacja= ", actualDeclination)
print("Cp = ",cp)
print("Pw= ",pw)
print("Pp= ",pp)
print ("KDd = ",KDd)

print ("Namiar rzeczywisty(1) jest równy: ", NR1)
print ("Namiar rzeczywisty(2) jest równy: ", NR2)


