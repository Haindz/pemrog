#NOMOR 1




#NOMOR 2
# start = "BACK HOME"
# actA = ["Minum Segelas Air Putih","Bersih2 Kamar","Mandi Sore", "Makan Malam"]
# actB = ["Adzan Maghrib", "Wudhu", "Sholat Maghrib","Baca Al Qur'an"]
# actC = ["Menunggu Adzan Isya'","Sholat Isya'"]
# actD = ["Belajar","Nugas","Tidur"]
# end = "AYO BANGUN SEKARANG SUDAH PUKUL 03.30"

# where = (input("Kamu mau kemana ? ").upper())
# def actNight():
#     if where == start:
#       print("Assalamua'alaikum, Alhamdulillah sampai rumah dengan selamat.")
#       for a in actA:
#         print(a)
#         while a == "Makan Malam":
#           break
#       for b in actB :
#         print (b)
#         if b == "Baca Al Qur'an":
#             break
#       for c in actC:
#         print(c)
#         if c == "Sholat Isya'":
#             for d in actD:
#                 print(d)
#                 if d == 'Tidur':
#                     break
#     else :
#       print("""Maaf kami belum membuat program selain kegiatan
#     malam hari di Kost/Rumah.""")
    
#     print(end)

# actNight()



#NOMOR 3
# mahasiswa = input("Masukkan nama Mahasiswa/i :")

# skor = []

# for a in range(0,101,1):
#     skor.append(a)

# nilai_uts = int(input("Masukkan skor nilai UTS mahasiswa (0-100) :"))
# if nilai_uts not in skor:
#         while nilai_uts not in skor:
#             print("Skor yang anda masukkan tidak valid")
#             print("Rentang skor yang valid adalah 0 s.d. 100")
#             nilai_uts = int(input("Masukkan skor nilai UTS mahasiswa (0-100) :"))
#             if nilai_uts == skor:
#                 break
# nilai_uas = int(input("Masukkan skor nilai UAS mahasiswa (0-100) :"))
# if nilai_uas not in skor:
#         while nilai_uas not in skor:
#             print("Skor yang anda masukkan tidak valid")
#             print("Rentang skor yang valid adalah 0 s.d. 100")
#             nilai_uas = int(input("Masukkan skor nilai UAS mahasiswa (0-100) :"))
#             if nilai_uas == skor:
#                 break
# nilai_tugas = int(input("Masukkan skor nilai tugas mahasiswa (0-100) :"))
# if nilai_tugas not in skor:
#         while nilai_tugas not in skor:
#             print("Skor yang anda masukkan tidak valid")
#             print("Rentang skor yang valid adalah 0 s.d. 100")
#             nilai_tugas = int(input("Masukkan skor nilai Tugas mahasiswa (0-100) :"))
#             if nilai_tugas == skor:
#                 break

# bobotUTS, bobotUAS, bobotTugas= 40/100, 35/100, 25/100
# uts = nilai_uts * bobotUTS
# uas = nilai_uas * bobotUAS
# tugas = nilai_tugas * bobotTugas

# final = uts + uas + tugas

# print("Mahasiswa/i dengan nama ",mahasiswa,f"mendapat perolehan nilai akhir sebesar {final}")



#NOMOR 4
# kata = input("Masukkan kata: ")
# vokal = "aeiouAEIOU"
# kata_baru = kata.translate(str.maketrans("a", "b", vokal))
# print(kata_baru)



#NOMOR 5
# banyakBlock = int(input("Masukkan jumlah balok yang dimiliki : "))

# def hitungLimas ():
    
#     t = 0
#     sisaBlock = banyakBlock
#     layer = 1

#     while sisaBlock >= layer:
#         sisaBlock -= layer
#         t += 1
#         layer += 1
    
#     return t, sisaBlock

# while True:
#     if banyakBlock <= 0:
#         print("Jumlah balok harus lebih dari 0")
#         continue

#     t, sisaBlock = hitungLimas()
#     print(f"Tinggi piramida adalah {t}")     
#     print(f"Sisa balok adalah {sisaBlock}")
#     break



#NOMOR 6
# tinggi = int(input("Masukkan tinggi segi empat: "))
# lebar = int(input("Masukkan lebar segi empat: "))
# karakter = str(input("Masukkan karakter yang diinginkan: "))
# for i in range(tinggi):
#     print(karakter*lebar)



# tinggi = int(input("Masukkan tinggi segitiga: "))
# while tinggi>0    :
#     print("*"*tinggi)
#     tinggi -= 1



# tinggi = int(input("Masukkan tinggi bangun segi empat: "))
# lebar = int(input("Masukkan lebar segi empat: "))
# karakter = str(input("Masukkan karakter yang diinginkan: "))
# for i in range(tinggi):
#     if i == 0 or i == tinggi-1:
#         print(karakter*lebar)
#     else:
#         print(karakter + " "*(lebar-2) + karakter)