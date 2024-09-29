print("Program untuk mengurutkan bilangan bulat sesuai dengan input user")
mode = int(input("Pilih metode pengurutan (1: Ascending atau 2: Descending): "))
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

if mode in [1, 2]: 
    angka = int(input("Masukkan bilangan bulat: "))
    list = [angka]
    print(list)
    lanjut = str(input("Masih ada bilangan yang ingin dimasukkan (y/t)? "))
    while True:
        if lanjut == 'y':
            angka = int(input("Masukkan bilangan bulat: "))
            list.append(angka)
            urut()
            print(list)
            lanjut = str(input("Masih ada bilangan yang ingin dimasukkan (y/t)? "))
            if lanjut == 'y':
                True
            elif lanjut =='t':
                urut()
                print(list)
                break
            else:
                print("MASUKKAN JAWABAN YANG SESUAI!!!")
                exit()
        elif lanjut == 't':
            urut()
            print(list)
            break
        else:
            print("MASUKKAN JAWABAN YANG SESUAI!!!")
            exit()
else: 
    print("MASUKKAN JAWABAN YANG VALID!!!")