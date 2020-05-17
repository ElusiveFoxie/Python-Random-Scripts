a = []
b = []
x = input('(write: exit to stop) podaj wartość: ')
while (x != 'exit'):
    a.append(int(x))
    x = input('(write: exit to stop) podaj wartość: ')
'''
for i in range(len(a)):
    if (int(a[i])%2==0):
        b.append(a[i])
'''

b = [number for number in a if number % 2 == 0]
print(a)
print(b)