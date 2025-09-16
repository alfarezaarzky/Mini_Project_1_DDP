# Muhammad Rizky Alfa Reza Basyah
# 2509116086
# Sistem Informasi C
# Mini Project 1

data_parkir = []

while True:
    print("---Menu Parkir Kendaraan---")
    print("1. Tambah Data Kendaraan")
    print("2. Lihat Data Kendaraan")
    print("3.Hapus Data Kendaraan")
    pilihan = input("Pilih menu parkir kendaraan: ")

    if pilihan == "1":
        no_plat = input("Masukkan Nomor Plat Kendaraan: ")
        jenis_kendaraan = input("Masukkan jenis kendaraan: ")
        waktu_masuk = input("Masukkan waktu masuk kendaraan: ")
        data = (no_plat, jenis_kendaraan, waktu_masuk)  
        data_parkir.append(data)           
        print("Data Kendaraan Berhasil Ditambahkan")

    elif pilihan == "2":
        print("Daftar Kendaraan Parkir:")
        for no_plat, jenis_kendaraan, waktu_masuk in data_parkir :
            print(f"Nomor_Plat: {no_plat}, Jenis_Kendaraan: {jenis_kendaraan}, Masuk: {waktu_masuk}")

    elif pilihan == "3":
        no_plat = input("Hapus Nomor Plat Kendaraan: ")
        jenis_kendaraan = input("Hapus Jenis Kendaraan : ")
        waktu_masuk = input("Hapus Waktu Masuk Kendaraan: ")
        data = (no_plat, jenis_kendaraan, waktu_masuk)
        data_parkir.remove(data)
        print("data berhasil terhapus")

    else:
        print("Pilihan tidak ada")
