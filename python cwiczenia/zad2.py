'''
x = int(input('podaj liczbe x'))
if (x%2==0 and x%4!=0):
    print ( 'liczba x jest podzielna przez 2')
elif(x%4==0):
    print('liczba x jest podzielna przez 4')
else:
    print('liczba x jest niepodzielna przez 2s')
'''

num = int(input('podaj liczbe num'))
check = int(input('podaj liczbe check'))
z = num/check
if (z%2==0):
    print ('check/num = even number')
else:
    print('check/num = not even number')