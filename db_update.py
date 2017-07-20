#! /usr/bin/python
# -*- coding:utf-8 -*-

import sqlite3

giris="""
1- ekle
2- sorgula 
3- güncelle
 """
baglanti=sqlite3.connect("ogrenciler.db")
b_cursor=baglanti.cursor()
#b_cursor.execute("""CREATE TABLE ogrenciler(kayit_no INTEGER PRIMARY KEY, ogrenci_no INTEGER, adi VARCHAR(50),soyadi VARCHAR(50),bolum VARCHAR(50)) """)
if baglanti:
    print(" bağlantı başarılı")
else :
    print("bağlantı başarısız")

def ogrenci_ekle(og_no,adi,soyadi,bolum):
    try:
        b_cursor.execute(" INSERT INTO ogrenciler(ogrenci_no,adi,soyadi,bolum) VALUES(?,?,?,?)",(og_no,adi,soyadi,bolum))
        baglanti.commit()
        baglanti.close()
        print("kayit eklendi")
    except sqlite3.Error as e:
        print(str(e))

def kayit_listele():
    veriler=b_cursor.execute("SELECT *FROM ogrenciler")

    print(veriler.fetchall())
    baglanti.commit()
    baglanti.close()

def guncelle(ad,no):
    b_cursor.execute("UPDATE ogrenciler set adi=? where ogrenci_no=?",(ad,no))
    baglanti.commit()
    kayit_listele()




b_cursor.execute("SELECT COUNT(*) from ogrenciler")
kayit_Sayisi=b_cursor.fetchone()
print (kayit_Sayisi)
print(giris)
girilen=input()
if int(girilen)==1:
    no=input("ogrenci no ")
    adi=input("öğrenci adı:")
    soyadi=input("öğrenci soyadı")
    bolum=input("bolumu:")
    ogrenci_ekle(no,adi,soyadi,bolum)
elif int(girilen)==2:
    kayit_listele()
elif int(girilen)==3:
    ad=input("yeni ad")
    ogr_no=input("öğrenci no ")
    guncelle(ad,ogr_no)

