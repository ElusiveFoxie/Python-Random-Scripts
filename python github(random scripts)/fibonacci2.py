def fibonaci(n):
    x = 1
    y = 1
    wynik = 1
    if (n == 1 or n== 2):
        return wynik
    else:
        for i in range(n-2):
            x = wynik
            wynik = wynik + y
            y = x
        return wynik
