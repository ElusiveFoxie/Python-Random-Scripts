
text = input("text: ").lower()
result = ""

for i in range(len(text)):
    if (ord(text[i]) > 96 and ord(text[i]) < 123):
        result += chr(109 - ord(text[i]) + 110)
    else:
        result += text[i]

print(result)