import re

upperRegex = re.compile(r'[A-Z]')
lowerRegex = re.compile(r'[a-z]')
digitRegex = re.compile(r'[0-9]')
specialRegex = re.compile(r'[!@#$%^&*_=]')

x = input("Password: ")
y = "Your password doesn\'t contain at least: "
if (len(x)<8):
    print('Your password isn\'t at least 8 characters long!')
if (upperRegex.search(x) == None):
    print(y,'1 uppercase letter!')
if (lowerRegex.search(x) == None):
    print(y,'1 lowercase letter!')
if (digitRegex.search(x) == None):
    print(y,'1 digit!')
if (specialRegex.search(x) == None):
    print(y,'1 special character!')
else:
    print("Your password is strong enough :)")


