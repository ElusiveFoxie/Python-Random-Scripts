import pyperclip

file = open('logs.txt', 'a')
file.write(str(pyperclip.paste())+'\n')
file.close()