# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 15:33:54 2022

@author: 071670
"""

nilai_absen = int(input("Nilai Absen ="))
nilai_tugas = int(input("Nilai Tugas ="))
nilai_uts = int(input("Nilai UTS ="))
nilai_uas = int(input("Nilai UAS ="))
Nilai_Akhir = (nilai_absen *0.1) + (nilai_tugas*0.2)+ (nilai_uts*0.3)+(nilai_uas*0.4)

if Nilai_Akhir >= 80 <=100:
    print ("A")
elif Nilai_Akhir >= 70 < 80:
    print() ("B")
elif Nilai_Akhir >= 60 < 70 :
    print ("C")
elif Nilai_Akhir >= 50 < 60 :
    print ("D")
else:
    print ("E")
    