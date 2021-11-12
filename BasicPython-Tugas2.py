nama=["Fawwaz","John"]
telp=["08123456789 ","08987654321"]

def menu1():
    for i in range(len(nama)):
        print("Data ke-",i+1)
        print("Nama :",str(nama[i]))
        print("Nomor Telpon : ",str(telp[i]))
        print("\b")

def menu2():
    nama.append(input("Masukan nama : "))
    telp.append(input("Masukan Nomor Telp : "))
    print("Kontak berhasil ditambahkan")
    ulangi()

def menuawal():
    print("Selamat Datang!")
    print("\b")
    print("\b")
    print("--- Menu ---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    print("\b")
    pilihan()

def ulangi():
    lagi=str(input("Mau menambahkan data lagi (Y/N)?"))
    if lagi =="Y":
        menu2()
    elif lagi=="N":
        print("Program selesai, sampai jumpa! ")
    else:
        print("pilihan salah-balik ke Menu Awal")
        menuawal()

def pilihan():
    pilih=int(input("Masukan Nomor Pilihan Anda : "))

    if pilih==1:
        menu1()
    elif pilih==2:
        menu2()
        
    elif pilih==3:
        print("Program selesai, sampai jumpa! ")
    else:
        print("mohon pilih 1-3")



menuawal()



