print("Program konversi nilai angka ke nilai huruf")
print("="*50)
nilai_uts = float(input("Masukkan nilai UTS (0-100): "))
nilai_uas = float(input("Masukkan nilai UAS (0-100): "))
nilai_tugas = float(input("Masukkan nilai tugas (0-100): "))
#bobot untuk uts, uas, dan tugas adalah 25%, 40%, dan 35%
nilai_akhir = 0.25*nilai_uts + 0.4*nilai_uas + 0.35*nilai_tugas 
if nilai_akhir >= 81:
    print("Nilai akhir yang didapatkan adalah", nilai_akhir, "(A)")
elif nilai_akhir >= 71:
    print("Nilai akhir yang didapatkan adalah", nilai_akhir, "(AB)")
elif nilai_akhir >= 66:
     print("Nilai akhir yang didapatkan adalah", nilai_akhir, "(B)")
else: 
     print("Nilai akhir yang didapatkan adalah", nilai_akhir, "(E)")