def NWD(x, y):
    if (x == y):
        return x
    elif(x > y and x%y == 0):
        return y
    elif(y > x and y%x == 0):
        return x
    else:
        dzielnikiX = []
        dzielnikiY = []

        for i in range(x):
            if (x % (i + 1) == 0):
                dzielnikiX.append(i + 1)

        for i in range(y):
            if (y % (i + 1) == 0):
                dzielnikiY.append(i + 1)

        if (x > y):
            i = len(dzielnikiX) - 1
            while (i >= 0):
                if (dzielnikiX[i] in dzielnikiY):
                    return dzielnikiX[i]
                else:
                    i -= 1
        else:
            i = len(dzielnikiY) - 1
            while (i >= 0):
                if (dzielnikiY[i] in dzielnikiX):
                    return  dzielnikiY[i]
                else:
                    i -= 1


def NWW(x,y):
    if (x > y):
        if (x % y == 0):
            return x
        else:
            return ((x*y)/NWD(x,y))

    else:
        if (y % x == 0):
            return y
        else:
            return((x * y) / NWD(x, y))


