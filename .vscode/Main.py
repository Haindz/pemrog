def play ():
    main_menu = str(input("start or exit: "))
    if main_menu == "start":
            path1 = str(input("right or left: "))
            import random
            jalur1 = ['right', 'left']
            if path1 == random.choice(jalur1):
                print("benar")
                path2 = str(input("jump or forward: "))
                import random
                jalur2 = ['jump', 'forward']
                if path2 == random.choice(jalur2):
                    print("you did it")
                    play_again = str(input("Play again? [y/n]"))
                    if play_again == "y":
                        play()
                    elif play_again == "n":
                        print("Skill issue")
                        exit()
                    else:
                        print("Tidak valid!")
                        play()
                else:
                    print("you die")
                    play_again = str(input("Play again? [y/n]"))
                    if play_again == "y":
                        play()
                    elif play_again == "n":
                        print("Skill issue")
                        exit()
                    else:
                        print("Tidak valid!")
                        play()
            else:
                print("salah")
                play_again = str(input("Play again? [y/n]"))
                if play_again == "y":
                        play()
                elif play_again == "n":
                        print("Skill issue")
                        exit()
                else:
                     play()
    elif main_menu == "exit":
            print("Skill issue")
            exit()
    else:
        print("tidak valid!")
        play_again = str(input("Play again? [y/n]"))
        if play_again == "y":
            play()
        elif play_again == "n":
            print("Skill issue")
            exit()
        else:
            play()
play()