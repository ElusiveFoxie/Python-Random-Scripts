
def IsPrime(x):
    y = 2
    while (y != x ):
        if(x % y == 0 or x == 1):
            return False
            break
        else:
            y += 1
    return True

def PiFunction(x):

    pierwsze = []
    z = 1

    while (z <= x):
        if(IsPrime(z) == True):
            pierwsze.append(z)
            z += 1
        else:
            z += 1

    return len(pierwsze)


print(PiFunction(50000))


