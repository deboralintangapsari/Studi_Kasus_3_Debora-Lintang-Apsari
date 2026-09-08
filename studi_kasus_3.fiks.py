#STUDI KASUS 3 - NIM GANJIL
#Nama : Debora Lintang Apsari 
#Prodi : Sistem Informasi kelas A
#NIM : 2609116011
#SISTEM PEMINJAMAN BUKU PERPUSTAKAAN FAKULTAS TEKNIK

#1. Inisialisasi data
daftar_buku = ("Dasar dasar teknik", "Mekanika teknik", "Dasar Pemrograman", "Material Teknik", "Pemrograman c++", "Termodinamika Teknik", "Panduan Gamtek")
pinjaman = []

# SAPAAN AWAL
print("Selamat datang di sistem peminjaman buku FT")
nama = input("Masukkan nama anda: ").strip()
print("Halo,", nama)

#2. Perulangan Menu
while True : 
    print("\n=======Menu Peminjaman=======")
    print("1. Lihat Daftar Buku")
    print("2. Pinjam Buku")
    print("3. Hapus Pinjaman")
    print("4. Lihat Pinjaman Saya")
    print("5. Selesai")
    print("================================")

    pilihan = input("Masukkan pilihan 1-5 : ").strip()

    #1. Lihat Daftar Buku
    if pilihan == "1": 
        print("\n=======Daftar Buku Tersedia========")
        for i in daftar_buku: 
            print("-", i)
        print("==================================")
        input("Tekan Enter untuk lanjut...")
    
    #2. Pinjam Buku + Validasi
    elif pilihan == "2": 
        print("\n========Daftar Buku Tersedia========")
        for i in daftar_buku:
            print("-", i)
        print("======================================")

        buku_pilih = input("\nMasukkan judul buku yang ingin dipinjam : ").strip()

        daftar_lower = [b.lower() for b in daftar_buku]
        pinjaman_lower = [p.lower() for p in pinjaman]

        if buku_pilih.lower() in daftar_lower:
            if buku_pilih.lower() in pinjaman_lower:
                print("Buku ini sudah kamu pinjam sebelumnya")
            else:
                pinjaman.append(buku_pilih)
                print("Buku berhasil dipinjam")
        else: 
            print("Buku tidak terdaftar")
        input("Tekan Enter untuk lanjut...")

    #3. Hapus Pinjaman
    elif pilihan == "3":
        print("\n========Buku yang sedang dipinjam==========")
        if len(pinjaman) == 0:
            print("Belum ada buku yang dipinjam")
        else:
            for i in pinjaman: 
                print("-", i)
        print("==============================================")

        if len(pinjaman) > 0: 
            buku_hapus = input("\nMasukkan judul buku yang ingin dihapus : ").strip()
            pinjaman_lower = [p.lower() for p in pinjaman]

            if buku_hapus.lower() in pinjaman_lower :
                index = pinjaman_lower.index(buku_hapus.lower())
                pinjaman.pop(index)
                print("Buku berhasil dihapus dari pinjaman")
            else:
                print("Buku tidak ada di list pinjaman kamu")
        input("Tekan Enter untuk lanjut...")

    #4. Lihat Pinjaman 
    elif pilihan == "4":
        print("\n=========Buku yang sedang dipinjam=========")
        if len(pinjaman) == 0:
            print("Belum ada buku yang dipinjam")
        else:
            for i in pinjaman : 
                print("-", i)
        print("==============================================")
        input("Tekan Enter untuk lanjut...")

    #5. Selesai
    elif pilihan == "5":
        print("\n========Terima Kasih", nama, "=========")
        print("Berikut seluruh buku yang anda pinjam : ")
        if len(pinjaman) == 0:
            print("Belum ada buku yang dipinjam")
        else:
            for i in pinjaman : 
                print("-", i)
        print("============================")
        break
    else:
        print("Pilihan tidak valid, silahkan pilih 1-5")