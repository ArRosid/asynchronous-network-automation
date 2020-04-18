# introduction to function

def luas_segitiga(alas,tinggi):
    return 1/2 * alas * tinggi

def luas_persegi(sisi):
    return sisi * sisi

def main():
    print("Selamat datang di Aplikasi saya\nSilahkan pilih: ")
    print("A. Hitung luas segitiga")
    print("B. Hitung luas persegi")
    print("C. exit")
    
    pilihan = input("Masukkan pilihan anda: ")

    if pilihan.lower() == "a":
        alas = int(input("Masukkan alas: "))
        tinggi = int(input("Masukkan tinggi: "))
        result = luas_segitiga(alas, tinggi)
        print("--------------------------")
        print(f"Luas dari segitiga anda adlah {result}")
        print("--------------------------")

    elif pilihan.lower() == "b":
        sisi = int(input("Masukkan sisi: "))
        result = luas_persegi(sisi)
        print("--------------------------")
        print(f"Luas persegi anda adalah {result}")
        print("--------------------------")

    elif pilihan.lower() == "c":
        exit()

    else:
        print("--------------------------")
        print("Pilihan salah")    
        print("--------------------------")


while True:
    main()