# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 15:18:48 2022

@author: 071670
"""

harga_buku = int(input ("masukan harga buku ="))
jumlah_beli = int(input("masukan jumlah beli buku="))
uang = int(input("masukan jumlah uang anda ="))
totalbelanja = harga_buku * jumlah_beli


if uang > totalbelanja:
    print ("dapat piring") ; print ("dapat sendok")
elif uang < totalbelanja:
    print ("dapat gelas")
else:
    print("gak dapat apa-apa")  