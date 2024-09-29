def main_menu():
    menu = str(input("Start/Exit: "))
    if menu == "start":
        play()
    elif menu == "exit":
        exit()
    else:
        print("Tidak Valid")
        main_menu()

def play_again():
    playAgain = str(input("Main lagi? [y/t]"))
    if playAgain == "y":
        play()
    elif playAgain == "t":
        print("Skill Issue")
        exit()
    else:
        print("Y/T")
        play_again()

def play():
    print("Kamu dan ibumu sedang menuju ke rumah tengah malam. \nIbumu mulai merasa terganggu karena kamu mengganggunya dan memutuskan untuk mengeluarkanmu dari mobil! \nSekarang kamu harus bertahan di sana.\n")
    print("kamu melihat ibumu pergi dan sadar ada mobil yang akan lewat.")
    print("a. Lari dan bersembunyi di belakang pohon. \nb. Pergi ke tengah jalan dan berteriak minta tolong.")
    level1 = str(input("Kamu memutuskan untuk: "))
    if level1 == "a":
        print("Pengendara itu pergi dan kamu mulai berkeliling.\n")
        print("Kamu berjalan beberapa saat dan mulai lapar. \nKemudian kamu melihat ada beberapa berry.")
        print("a. Makan berry itu. \nb. Tidak memedulikannya.")
        level2 = str(input("Apa yang akan kamu lakukan? "))
        if level2 == "a":
            print("Berry-berry itu sangat beracun! Kamu memakannya dan langsung tewas di tempat!")
            play_again()
        elif level2 == "b":
            print("Kamu tetap kelaparan tapi bisa kamu tahan.\n")
            print("Kamu mendengar ada sebuah suara!")
            print("a. Memanjat pohon. \nb. Tetap diam di tempat. \nc. Melanjutkan apa yang kamu lakukan.")
            level3 = str(input("Apa yang kamu lakukan? "))
            if level3 == "a":
                print("Saat kamu memanjat pohon, kamu menggapai sebuah ranting yang rapuh dan kamu terjatuh. \nDUAAAGGG!!! Kepalamu membentur batu besar dan membunuhmu!")
                play_again()
            elif level3 == "b":
                print("Suara itu berhenti dan kamu mulai berjalan lagi. \nSuara itu berasal dari seseorang dan kamu melihatnya pergi. \n")
                print("Kamu mulai lelah dan melihat ada 3 tempat yang kamu pikir bisa kamu gunakan untuk tidur.")
                print("a. Di antara 2 batu besar. \nb. Di atas pohon. \nc. Di tempat terbuka.")
                level4 = str(input("Kamu memutuskan untuk tidur di? "))
                if level4 == "a":
                    print("Tidak ada yang bisa melihatmu. \n")
                    print("Ketika kamu hampir terlelap, kamu bimbang untuk mematikan senter atau tidak.")
                    print("a. Tidak mematikan senter. \nb. Matikan senter")
                    level5 = str(input("Kamu memutuskan untuk..."))
                    if level5 == "a":
                        print("Ada orang yang lewat dan melihatmu. Dia menghampirimu dan mengira bahwa kamu sakit parah. \nJadi dia menembakmu.")
                        play_again()
                    elif level5 == "b":
                        print("Kamu memiliki malam yang buruk, tapi setidaknya kamu selamat.")
                        print("Kamu lapar dan melihat ada beberapa berry dengan warna yang berbeda.")
                        print("a. Hijau. \nb. Biru. \nc. Merah.")
                        level6 = str(input("Kamu memakan berry yang berwarna..."))
                        if level6 == "a":
                            print("Mereka beracun dan kamu mati.")
                            play_again()
                        elif level6 == "b":
                            print("Mereka beracun dan kamu mati.")
                            play_again()
                        elif level6 == "c":
                            print("Pilihan yang bagus. Berry ini tidak beracun dan kamu memakannya dengan lahap. \n")
                            print("Saat kamu makan, kamu melihat mobil ibumu dan dia sedang menunggumu di dalam mobil.")
                            print("a. Pergi menghampirinya. \nb. Mengacuhkannya.")
                            level7 = str(input("Kamu memutuskan untuk? "))
                            if level7 == "a":
                                print("Kamu masuk ke dalam mobil dan pergi pulang. Ibumu tidak percaya kamu masih hidup.")
                                print("Selamat kamu telah bertahan hidup. \n")
                                print("Terima kasih telah memainkan game saya :)")
                                play_again()
                            elif level7 == "b":
                                print("Ibumu marah dan pergi meninggalkanmu dan tidak pernah kembali lagi. Kamu mati setelah beberapa hari.")
                                play_again()
                        else:
                            print("Hanya ada pilihan a, b, atau c di sepanjang permainan!")
                            play_again()
                    else:
                        print("Hanya ada pilihan a, b, atau c di sepanjang permainan!")
                        play_again()
                elif level4 == "b":
                    print("Saat kamu memanjat pohon, kakimu terpeleset dan DUUAAAGGGGGG!!! Jantungmu tertusuk batang pohon!")
                    play_again()
                elif level4 == "c":
                    print("Seorang kanibal melihatmu. Dia membunuhmu dan memakanmu!")
                    play_again()
                else:
                    print("Hanya ada pilihan a, b, atau c di sepanjang permainan!")
                    play_again()
            elif level3 == "c":
                print("Sesaat setelah kamu berbalik, kamu sadar bahwa itu adalah orang yang membuat suara. \nDia menikammu dengan pisau dan meninggalkanmu mati.")
                play_again()
            else:
                print("Hanya ada pilihan a, b, atau c di sepanjang permainan!")
                play_again()
        else:
            print("Hanya ada pilihan a, b, atau c di sepanjang permainan!")
            play_again()
    elif level1 == "b":
        print("Pengendara itu tidak peduli dan tetap melaju dan memutuskan untuk menabrakmu!")
        play_again()
    else:
        print("Hanya ada pilihan a, b, atau c di sepanjang permainan!")
        play_again()

main_menu()