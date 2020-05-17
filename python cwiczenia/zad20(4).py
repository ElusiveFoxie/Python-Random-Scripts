x = [1,2,3,4,14,20,46,99]
y = int(input('podaj wartosc do sprawdzenia: '))

def sprawdz(x,y):
    mid = (0 + len(x)) // 2
    if (x[mid] == y):
        print(True)
    else:
        if(y > x[mid]):
            mid



    for i in range(len(x)):
        if (y == x[i]):
            print(True)
            break
        elif (y != x[i] and i ==len(x)-1):
            print (False)


sprawdz(x,y)