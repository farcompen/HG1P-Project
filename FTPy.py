#! /usr/bin/python
# -*- coding:utf-8 -*-

import ftplib
import getpass
giris="""
        FTPy 2017 
        Faruk GÜNGÖR
        

"""
import sys

def dosya_indir(ftp,dosya_adi):
    try:
         print("bekleyiniz")
         dosya=open(dosya_adi,'wb')
         ftp.retrbinary('RETR %s'%dosya_adi,dosya.write)

    except ftplib.all_errors as e :
        print(str(e))

ftp_host=input(" ftp adres or host ip  :")
ftp=ftplib.FTP(ftp_host)
username=input(" kullanıcı adı :")
password=getpass.getpass(" Password :")
ftp.login(username,password)
print("*"*50)
print("Sunucudaki dosyalar / files on Server \n")

ftp.dir()
print("*"*50)
filename=input("indirilecek dosya adı:")
dosya_indir(ftp,filename)
ftp.quit()