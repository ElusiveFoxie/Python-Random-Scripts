x = int(input('Size: '))
def y():
    for i in range(x):
        print(' ---', end='')
    print('', )
def z():
    for i in range(x + 1):
        print('|   ', end='')
    print('', )

for i in range(x):
    y()
    z()
y()
