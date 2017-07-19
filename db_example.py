#! usr/bin/python
# -*- coding:utf-8 -*-



import sqlite3

nottt=""" 

   işlem no giriniz:
   1- kayıt ekle 
   2- kayıt getir
  
"""
baglanti=sqlite3.connect("galeri.db")

if(baglanti):
    print("bağlantı başarılı")
else :
    print("bağlantı başarısız")

#kayıt ekleme metodu
def veri_ekle(marka,model):
    try:
        baglanti.cursor()
        baglanti.cursor().execute(" INSERT INTO Suv(Marka,Model) values(?,?)",(marka,model))
        baglanti.commit()
        baglanti.close()
        print("veri eklendi")
    except sqlite3.Error as e :
        print(str(e))
#db_sec.execute("""CREATE TABLE Suv(kayit_no INTEGER PRIMARY KEY, Marka VARCHAR(50) NOT NULL, Model VARCHAR(50) NOT NULL )""")
# select sorgusu
def select():
    veriler=baglanti.cursor().execute("SELECT * from Suv")
    print(veriler.fetchall())
    baglanti.commit()
    baglanti.close()


print(nottt)
islem_no=int(input())
if islem_no==1:

   mrk=input("marka:")
   mdl=input("model:")
   veri_ekle(mrk,mdl)
elif islem_no==2:
    select()

