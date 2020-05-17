print(' 1 2 3 \n 4 5 6 \n 7 8 9')
tab = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
string = ' ---  ---  ---\n| '+tab[0]+' || '+tab[1]+' || '+tab[2]+' |\n ---  ---  ---\n| '+tab[3]+' || '+tab[4]+' || '+tab[5]+' |\n ---  ---  ---\n| '+tab[6]+' || '+tab[7]+' || '+tab[8]+' |\n ---  ---  ---'

print(string)
print('Cross starts')
x = []
y = []
turn = 'cross'
tura2 = turn + ' : '

while(
#poziom
set([1,2,3]).issubset(set(x) or set(y)) == False and
set([4,5,6]).issubset(set(x) or set(y)) == False and
set([7,8,9]).issubset(set(x) or set(y)) == False and
#pion
set([1,4,7]).issubset(set(x) or set(y)) == False and
set([2,5,8]).issubset(set(x) or set(y)) == False and
set([3,6,9]).issubset(set(x) or set(y)) == False and
#skos
set([1,5,9]).issubset(set(x) or set(y)) == False and
set([3,5,7]).issubset(set(x) or set(y)) == False

):
    if (len(x) == 5):
        break
    else:
        k = int(input(tura2))
        if (k in range(1, 10)):
            if (turn == 'cross' and k not in y + x):
                x.append(k)
                turn = 'circle'
                tura2 = turn + ' : '
                tab[k-1] = 'X'
                string = ' ---  ---  ---\n| ' + tab[0] + ' || ' + tab[1] + ' || ' + tab[2] + ' |\n ---  ---  ---\n| ' + tab[
                    3] + ' || ' + tab[4] + ' || ' + tab[5] + ' |\n ---  ---  ---\n| ' + tab[6] + ' || ' + tab[7] + ' || ' + tab[
                             8] + ' |\n ---  ---  ---'

            elif(turn == 'circle' and k not in y + x):
                y.append(k)
                turn = 'cross'
                tura2 = turn + ' : '
                tab[k - 1] = 'O'
                string = ' ---  ---  ---\n| ' + tab[0] + ' || ' + tab[1] + ' || ' + tab[2] + ' |\n ---  ---  ---\n| ' + tab[
                    3] + ' || ' + tab[4] + ' || ' + tab[5] + ' |\n ---  ---  ---\n| ' + tab[6] + ' || ' + tab[7] + ' || ' + tab[
                             8] + ' |\n ---  ---  ---'
            else:
                print('This field is already taken. Pick up different field.')
            print(string)
        else:
            print('Give number from 1 to 9')


if(
#poziom
set([1,2,3]).issubset(set(x) or set(y)) == False and
set([4,5,6]).issubset(set(x) or set(y)) == False and
set([7,8,9]).issubset(set(x) or set(y)) == False and
#pion
set([1,4,7]).issubset(set(x) or set(y)) == False and
set([2,5,8]).issubset(set(x) or set(y)) == False and
set([3,6,9]).issubset(set(x) or set(y)) == False and
#skos
set([1,5,9]).issubset(set(x) or set(y)) == False and
set([3,5,7]).issubset(set(x) or set(y)) == False
):
    print('----TIE----')
else:
    print('----' + turn + ' LOST----')