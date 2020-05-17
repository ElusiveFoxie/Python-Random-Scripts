a = str(input())
i = 1
k = len(a)

wynik = "wynik to: "

while(i<=k):
    
    b = a[-i]
    wynik = wynik + b
    i += 1
   
k = k[::-1]
print(wynik)