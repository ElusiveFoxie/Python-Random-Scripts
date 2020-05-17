import random
print('Welcome to the Cows and Bulls Game')
liczba = []

cb = [0, 0]
for i in range(4):
    liczba.append(str(random.randint(0, 9)))

print(liczba)
while(cb[0] != 4):

    liczba2 = []
    guess2 = []
    cb = [0, 0]
    guess = input('Enter a number: ')
    guess = list(guess)

    for i in range (4):
        if (guess[i] == liczba[i]):
            cb[0] += 1
        elif (guess[i] != liczba[i]):
            liczba2.append(liczba[i])
            guess2.append(guess[i])

    l = len(liczba2)

    for i in range(l):
        for k in range(l):
            if (guess2[i] == liczba2[k]):
                cb[1] += 1
                break

    print(cb[0], ' cows ', cb[1], ' bulls ')

print ('U won, password was: ',liczba)



