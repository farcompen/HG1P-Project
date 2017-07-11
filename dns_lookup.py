#! /usr/bin/python
#-*- coding:utf-8 -*-

import socket

adress=input("dns sorgusu yapılacak adresi giriniz. örn: google.com : ")
nslookup=socket.gethostbyname(adress)
print("dns: ")
print(nslookup)