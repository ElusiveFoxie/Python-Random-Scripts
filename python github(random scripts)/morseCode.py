print ('Text to morse code Converter\n')

def zamiana1(x):
    y = ''
    x = x.lower()
    for i in range(len(x)):
        y += x[i].replace(x[i], morse[normal.index(x[i])])
    return y

def zamiana2(z):
    k = z.split(' ')
    y = ''
    for i in range(len(k)):
        y += k[i].replace(k[i], normal[morse.index(k[i])])
    return(y)

normal = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
          'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z',' ']
morse = ['.-', '-...', '-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--',
         '-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','  ']

z =  input('PRESS 1 for text into morse_code \nPRESS 2 for morse_code into text\nYour choice: ')
if (z == '1'):
    x = input('Put in text: ')
    print(zamiana1(x))
elif(z == '2'):
    x = input('Put in morse code, separate characters with 1 space  e.g.(sos = ... --- ...): ')
    print(zamiana2(x))
else:
    print('Wrong choice')
    z =  input('1 for text into morse_code \n2 for morse_code into text\nYour choice: ')


