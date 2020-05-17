print('Press 1 for rock, 2 for scissors, 3 for paper')

while True:

    x = int(input('player 1: '))
    y = int(input('player 2: '))
    dif = x - y

    while(x == y):
        x = str(input('player 1: '))
        y = str(input('player 2: '))

    if dif in [-1, 2]:
        print('player 1 wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break

    else:
        print('player 2 wins.')

        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break

