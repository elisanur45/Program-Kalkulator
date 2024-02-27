def tambah(a,b):
    return a + b
def kurang (a,b):
    return a - b
def kali (a,b):
    return a * b
def bagi (a,b):
    if b == 0:
        print("Error! Pembagian dengan nol tidak bisa dilakukan.")
    else:
        return a / b
    
while True:
    print("====Selamat Datang Di Menu Kalkulator sederhana====")
    print("---------------------------------------------------")
    angka1= float(input("Masukan Angka Pertama:"))
    angka2= float(input("Masukan Angka Kedua:"))
    print("---------------------------------------------------")
    print("Pilih Menu Operasi di Bawah ini:")
    print("Hanya diperbolehkan Memilih 1 Menu")
    print("1.Penambahan")
    print("2.Pengurangan")
    print("3.Perkalian")
    print("4.Pembagian")
    print("5.keluar")
    print("--------------------------------------------------")
    pilihan=input("Masukan Menu Operasi Yang Anda Inginkan(1/2/3/4/5):")
    
    if pilihan == '1':
        print("Anda Memilih Menu Penambahan")
        print(angka1, "+" , angka2, "=", tambah(angka1,angka2))
    elif pilihan == '2':
        print("Anda Memilih Menu Pengurangan")
        print(angka1,"-", angka2, "=", kurang(angka1, angka2))
    elif pilihan =='3':
        print("Anda Memilih Menu Perkalian")
        print(angka1,"*", angka2, "=", kali(angka1,angka2))
    elif pilihan  == '4':
        print("Anda Memilih Menu Pembagian")
        print(angka1, "/", angka2, "=",bagi(angka1,angka2))
    elif pilihan == '5':
        print("Terimakasih Telah Menggunakan Program Saya.")
        break
    else:
        print("Input Tidak Valid")