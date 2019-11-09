# Menghitung laba

# Buat program sederhana dengan perulangan: program1.py
# Seorang pengusaha menginvestasikan uangnya untuk memulai usahanya dengan
# modal awal 100 juta, pada bulan pertama dan kedua belum mendapatkan laba. pada
# bulan ketiga baru mulai mendapatkan laba sebesar 1% dan pada bulan ke 5,
# pendapatan meningkat 5%, selanjutnya pada bulan ke 8 mengalami penurunan
# keuntungan sebesar 2%, sehingga laba menjadi 3%. Hitung total keuntungan selama 8
# bulan berjalan usahanya.

investasi = 100000000
bulan = 0
laba = 0
total = 0

for a in range (8):
    bulan += 1
    laba += 1
    if bulan < 3 :
        laba = investasi * 0
    elif bulan < 5 :
        laba = investasi * 0.01
    elif bulan < 8 :
        laba = investasi * 0.05
    else :
        laba = investasi * 0.03
    print ('Laba bulan ke', bulan,'sebesar', laba)
    total = total + laba
print ('Total laba adalah : ', total)
