list = []
x = input('podaj wartosc listy ')

while(x != 'exit'):
    list.append(x)
    x = input('podaj wartosc listy ')

def new():
    listnew = []
    listnew.append(list[0])
    listnew.append(list[-1])
    print(listnew)

new()