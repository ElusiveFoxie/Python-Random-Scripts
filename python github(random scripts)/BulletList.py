import pyperclip
text = pyperclip.paste()

text = text.split('\n')
str = ""
for i in range(len(text)):
    str += "*" + text[i] + "\n"

pyperclip.copy(str)





