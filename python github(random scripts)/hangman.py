
haslo = input('podaj haslo: ')
x = 0
k = len(haslo)
y = k * '*'

print(y)


while (x < 5 and y!=haslo):
    litera= input('(masz '+str(5 -x)+' prob) podaj litere: ')
    if (litera not in haslo):
        print('zla litera pozostalo: ',5 - x,' prob')
        x += 1
    else:
        for i in range(k):
            if (litera==haslo[i]):
                y = y[0:i]+litera+y[i+1:len(y)]
        print(y)

if (y==haslo):
    print('wygrales')
else:
    print('przegrales, hasło to: ',haslo)
