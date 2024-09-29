print("Program untuk mengurutkan bilangan bulat sesuai dengan input user")
list = []

def urut():
    n = len(list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if mode == 1:  # Ascending
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
            elif mode == 2:  # Descending
                if list[j] < list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
    return list

while True:
    mode = int(input("Pilih metode pengurutan (1: Ascending atau 2: Descending): "))
    if mode in [1, 2]:
        break
    else:
        True

while True:
    angka = int(input("Masukkan bilangan bulat: "))
    list.append(angka)
    urut()
    print(list)
    lanjut = str(input("Masih ada bilangan yang ingin dimasukkan (y/t)? "))
    if lanjut == 'y':
        True
    elif lanjut == 't':
        break
    else:
        print("Tidak valid")
        break
print(list)


