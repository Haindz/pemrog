# Program untuk konversi panjang
print("Program untuk konversi panjang")
print("==============================")
print("1. Kaki")
print("2. Meter")
print("3. Mil")
print("4. Kilometer")

# Input nilai panjang dan satuan asal serta tujuan
panjang_asal = float(input("Derajat panjang asal: "))
satuan_asal = int(input("Satuan panjang asal (1/2/3/4): "))
satuan_tujuan = int(input("Satuan panjang tujuan (1/2/3/4): "))

# Fungsi konversi dari satuan asal ke meter (sebagai satuan standar)
def konversi_ke_meter(panjang, satuan):
    if satuan == 1:  # Kaki
        return panjang * 0.3048
    elif satuan == 2:  # Meter
        return panjang
    elif satuan == 3:  # Mil
        return panjang * 1609.34
    elif satuan == 4:  # Kilometer
        return panjang * 1000

# Fungsi konversi dari meter ke satuan tujuan
def konversi_dari_meter(panjang_meter, satuan):
    if satuan == 1:  # Kaki
        return panjang_meter / 0.3048
    elif satuan == 2:  # Meter
        return panjang_meter
    elif satuan == 3:  # Mil
        return panjang_meter / 1609.34
    elif satuan == 4:  # Kilometer
        return panjang_meter / 1000

# Konversi panjang
panjang_dalam_meter = konversi_ke_meter(panjang_asal, satuan_asal)
panjang_konversi = konversi_dari_meter(panjang_dalam_meter, satuan_tujuan)

# Output hasil konversi
satuan_list = ['Kaki', 'Meter', 'Mil', 'Kilometer']
print(f"Hasil konversi dari {panjang_asal} {satuan_list[satuan_asal - 1]} adalah", end=" ") 
print(f"{panjang_konversi:.4f} {satuan_list[satuan_tujuan - 1]}")
