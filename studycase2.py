# Muhammad Rizky Alfa Reza Basyah
# NIM 2509116086
# Sistem Informasi C
# Studycase2


jumlah_roda = int(input ("Masukkan jumlah roda : "))

if jumlah_roda == 2:
    a = input("Apakah memiliki pedal ?(y/n) :")
    if a == "y":
        print("Sepeda")
    elif   a == "n" :
        print("Motor")    
    else :
        print("Input hanya menggunakan y/n")

elif jumlah_roda == 4:
    b = input("Apakah digunakan untuk mengangkat barang ?(y/n)")
    if b == "y":
        print("Mobil Pick Up")

    elif b == "n":
        b = input("Apakah digunakan untuk mengangkut orang ?(t/f)")
    if b == "t" :
        print("Mobil Penumpang")
    elif b == "f" :
        print("Tipe mobil lainnya")    
    
else :
    print("Kendaraan tidak terdaftar")       
