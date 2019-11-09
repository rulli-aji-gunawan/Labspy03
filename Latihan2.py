# Menentukan angka terbesar

list = []
# a = int(input("Masukkan bilangan : "))
a = 1

while a > 0:
    if a == 0 :
        break
    a = int (input( "Masukkan bilangan : "))
    list.append(a)

print ("Bilangan terbesar adalah : ", max(list))


