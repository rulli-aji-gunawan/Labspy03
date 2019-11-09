# Menampilkan 5 angka random dibawah 0.5
#
# Latihan 1: latihan1.py
# 1. Tampilkan n bilangan acak yang lebih kecil dari 0.5.
# 2. nilai n diisi pada saat runtime
# 3. anda bisa menggunakan kombinasi while dan for untuk menyelesaikannya
# 4. gunakan fungsi random() yang dapat diimport terlebih dahulu

n = int(input ('Masukkan nilai N : '))
import random
urutan = 0

for a in range (n):
    urutan += 1
    print ('data ke : ', urutan ,'=>', random.uniform(0.0, 0.5))

# while i < 0.5:
#     print (i)




