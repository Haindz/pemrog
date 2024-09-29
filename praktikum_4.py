def menu():
    print("Program untuk konversi panjang")
    print("="*30)
    print("1. kaki \n2. m \n3. mil \n4. km")
    panjang = float(input("Panjang asal: "))
    satuan_asal = str(input("Satuan panjang asal (kaki, m, mil, km): "))
    satuan_tujuan = str(input("Satuan panjang tujuan (kaki, m, mil, km): "))
    if satuan_asal == "kaki" and satuan_tujuan == "kaki":
        print("Hasil konversi dari", panjang, satuan_asal, "adalah", panjang*1, satuan_tujuan)
        coba_lagi()
    elif satuan_asal == "kaki" and satuan_tujuan == "m":
        print("Hasil konversi dari", panjang, satuan_asal, "adalah", panjang*0.3048, satuan_tujuan)
        coba_lagi()
    elif satuan_asal == "kaki" and satuan_tujuan == "mil":
        print("Hasil konversi dari", panjang, satuan_asal, "adalah", panjang/5280, satuan_tujuan)
        coba_lagi()
    elif satuan_asal == "kaki" and satuan_tujuan == "km":
        print("Hasil konversi dari", panjang, satuan_asal, "adalah", panjang/3281, satuan_tujuan)
        coba_lagi()

    elif satuan_asal == "m" and satuan_tujuan == "kaki":
        print("Hasil konversi dari", panjang, satuan_asal, "adalah", panjang*3.28084, satuan_tujuan)
        coba_lagi()
    elif satuan_asal == "m" and satuan_tujuan == "m":
        print("Hasil konversi dari", panjang, satuan_asal, "adalah", panjang*1, satuan_tujuan)
        coba_lagi()
    elif satuan_asal == "m" and satuan_tujuan == "mil":
        print("Hasil konversi dari", panjang, satuan_asal, "adalah", panjang*0.0006, satuan_tujuan)
        coba_lagi()
    elif satuan_asal == "m" and satuan_tujuan == "km":
        print("Hasil konversi dari", panjang, satuan_asal, "adalah", panjang/1000, satuan_tujuan)
        coba_lagi()

    elif satuan_asal == "mil" and satuan_tujuan == "kaki":
        print("Hasil konversi dari", panjang, satuan_asal, "adalah", panjang*5280, satuan_tujuan)
        coba_lagi()
    elif satuan_asal == "mil" and satuan_tujuan == "m":
        print("Hasil konversi dari", panjang, satuan_asal, "adalah", panjang*1609.34, satuan_tujuan)
        coba_lagi()
    elif satuan_asal == "mil" and satuan_tujuan == "mil":
        print("Hasil konversi dari", panjang, satuan_asal, "adalah", panjang*1, satuan_tujuan)
        coba_lagi()
    elif satuan_asal == "mil" and satuan_tujuan == "km":
        print("Hasil konversi dari", panjang, satuan_asal, "adalah", panjang*1.6094, satuan_tujuan)
        coba_lagi()

    elif satuan_asal == "km" and satuan_tujuan == "kaki":
        print("Hasil konversi dari", panjang, satuan_asal, "adalah", panjang*3280.8399, satuan_tujuan)
        coba_lagi()
    elif satuan_asal == "km" and satuan_tujuan == "m":
        print("Hasil konversi dari", panjang, satuan_asal, "adalah", panjang*1000, satuan_tujuan)
        coba_lagi()
    elif satuan_asal == "km" and satuan_tujuan == "mil":
        print("Hasil konversi dari", panjang, satuan_asal, "adalah", panjang*0.6214, satuan_tujuan)
        coba_lagi()
    elif satuan_asal == "km" and satuan_tujuan == "km":
        print("Hasil konversi dari", panjang, satuan_asal, "adalah", panjang/1, satuan_tujuan)
        coba_lagi()
    else:
        print("Tidak valid")
        coba_lagi()

def coba_lagi():
    coba = str(input("Coba lagi? [y/n] "))
    if coba == "y":
        menu()
    elif coba == "n":
        print("Terima kasih sudah mencoba program")
        exit()
    else:
        print("Tidak valid")
        coba_lagi()

menu()