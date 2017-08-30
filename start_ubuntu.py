import os
import sys
import time
os.system('clear')
# Komentarz ogólny : liczba wierszy na mapą zawsze musi być równa 10.


def delay_print(s):
    for c in s:
        sys.stdout.write('%s' % c)
        sys.stdout.flush()
        time.sleep(0.02)


def title_screen():
    delay_print("\n ___ _____      _   _  _____ ___ __  __        ___   ___      ___   ___ ___ ___ \n")
    delay_print("/ __|_  / |    /_\ | |/ /_ _| __|  \/  |      | _ ) /_\ \    / /_\ | _ \_ _|_ _|\n")
    delay_print("\__ \/ /| |__ / _ \| ' < | || _|| |\/| |      | _ \/ _ \ \/\/ / _ \|   /| | | | \n")
    delay_print("|___/___|____/_/ \_\_|\_\___|___|_|  |_|      |___/_/ \_\_/\_/_/ \_\_|_\___|___|\n")
    delay_print("\nROGUELIKE EXPERIENCE\n\n")
    print("Wciśnij cokolwiek.")
    input_char = getch()
    os.system('clear')


def character_choice_screen():
    while True:
        os.system('clear')
        print("\n _    _       _                                  _             _ ")
        print("| |  | |     | |                                | |           (_)")
        print("| |  | |_   _| |__   ___  _ __   _ __   ___  ___| |_ __ _  ___ _ ")
        print("| |/\| | | | | '_ \ / _ \| '__| | '_ \ / _ \/ __| __/ _` |/ __| |")
        print("\  /\  / |_| | |_) | (_) | |    | |_) | (_) \__ \ || (_| | (__| |")
        print(" \/  \/ \__, |_.__/ \___/|_|    | .__/ \___/|___/\__\__,_|\___|_|")
        print("         __/ |                  | |                              ")
        print("        |___/                   |_|                              \n\n")
        delay_print("Wybierz swoje przeznaczenie:\n")
        delay_print("\n1. WOJOWNIK\n")
        delay_print("\n2. ŁOWCA\n")
        delay_print("\n3. NINJA\n")
        delay_print("\n4. STWÓRZ WŁASNĄ POSTAĆ\n")
        input_char = getch()
        if input_char.upper() == '1':
            os.system('clear')
            with open('1. WOJOWNIK.txt', 'r') as myfile:
                postać = myfile.read()
                print(postać)
                print("WOJOWNIK")
                print("\nATRYBUTY:")
                print("SIŁA : 4, ZWINNOŚĆ : 2, PERCEPCJA: 1, INTELIGENCJA : 1, SIŁA WOLI : 2")
                print("\nWciśnij 'y' żeby wybrac tego bohatera, wciśnij coś innego żeby wrócić")
                input_char = getch()
                if input_char.upper() == 'Y':
                    return {"SIŁA": 4, "ZWINNOŚĆ": 2, "PERCEPCJA": 1, "INTELIGENCJA": 1, "SIŁA WOLI": 2}
        if input_char.upper() == '2':
            os.system('clear')
            with open('2. ŁOWCA.txt', 'r') as myfile:
                postać = myfile.read()
                print(postać)
                print("ŁOWCA")
                print("\nATRYBUTY:")
                print("SIŁA : 2, ZWINNOŚĆ : 3, PERCEPCJA: 3, INTELIGENCJA : 1, SIŁA WOLI : 2")
                print("\nWciśnij 'y' żeby wybrac tego bohatera, wciśnij coś innego żeby wrócić")
                input_char = getch()
                if input_char.upper() == 'Y':
                    return {"SIŁA": 2, "ZWINNOŚĆ": 3, "PERCEPCJA": 3, "INTELIGENCJA": 1, "SIŁA WOLI": 2}
        if input_char.upper() == '3':
            os.system('clear')
            with open('3. NINJA.txt', 'r') as myfile:
                postać = myfile.read()
                print(postać)
                print("NINJA")
                print("\nATRYBUTY:")
                print("SIŁA : 1, ZWINNOŚĆ : 3, PERCEPCJA: 3, INTELIGENCJA : 3, SIŁA WOLI : 1")
                print("\nWciśnij 'y' żeby wybrac tego bohatera, wciśnij coś innego żeby wrócić")
                input_char = getch()
                if input_char.upper() == 'Y':
                    return {"SIŁA": 1, "ZWINNOŚĆ": 3, "PERCEPCJA": 3, "INTELIGENCJA": 3, "SIŁA WOLI": 1}
        if input_char.upper() == '4':
            os.system('clear')
            with open('4. STWORZONA POSTAĆ.txt', 'r') as myfile:
                postać = myfile.read()
                print(postać)
                print("NIEZNAJOMY")
                print("\nATRYBUTY:")
                print("\nSIŁA : 1, ZWINNOŚĆ : 1, PERCEPCJA: 1, INTELIGENCJA : 1, SIŁA WOLI : 1\n\n\n")
                print("To ekran tworzenia postaci.")
                print("Wciśnij 'y' żeby stworzyć swoją postać, wciśnij coś innego żeby wrócić.")
                input_char = getch()
                if input_char.upper() == 'Y':
                    os.system('clear')
                    siła = 1
                    zwinność = 1
                    percepcja = 1
                    inteligencja = 1
                    siła_woli = 1
                    punkty = 6
                    while True:
                        if punkty == 0:
                            break
                        else:
                            print("\n\nSIŁA", siła, "ZWINNOŚĆ", zwinność, "PERCEPCJA", percepcja)
                            print("INTELIGENCJA", inteligencja, "SIŁA WOLI", siła_woli)
                            print("Masz", punkty, "punktów atrybutów do rozdysponowania.")
                            print("Wciśnij 's', 'z', 'p', 'i', 'w' żeby dodać punkt do atrybutu")
                            print("kolejno: siły, zwinności, percepcji, inteligencji, siły woli.")
                            input_char = getch()
                            if input_char.upper() == 'S':
                                siła += 1
                                punkty -= 1
                                continue
                            if input_char.upper() == 'Z':
                                zwinność += 1
                                punkty -= 1
                                continue
                            if input_char.upper() == 'P':
                                percepcja += 1
                                punkty -= 1
                                continue
                            if input_char.upper() == 'I':
                                inteligencja += 1
                                punkty -= 1
                                continue
                            if input_char.upper() == 'W':
                                siła_woli += 1
                                punkty -= 1
                                continue
                            else:
                                continue
                    print("\n\nSIŁA", siła, "ZWINNOŚĆ", zwinność, "PERCEPCJA", percepcja)
                    print("INTELIGENCJA", inteligencja, "SIŁA WOLI", siła_woli)
                    print("Wybrałeś swoje przeznaczenie. Wciśnij cokolwiek, żeby rozpocząc gre.")
                    input_char = getch()
                    return {"SIŁA": siła, "ZWINNOŚĆ": zwinność, "PERCEPCJA": percepcja, "INTELIGENCJA": inteligencja,
                            "SIŁA WOLI": siła_woli}
        else:
            continue


def getch():
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def collision(position):
    """ Returns message depending on what hero touches. """
    if position == "N":
        print("\n" * 9)
        print("Tutaj NPC powie ci co masz robić dalej.")
    elif position == "W":
        print("\n" * 9)
        print("Trafiłeś do wioski Szwarzwald")
    elif position == "G":
        print("\n" * 9)
        print("Trafiłeś do gaju Łotrzyków.")
    elif position == "M":
        print("\n" * 9)
        print("Most pilnowany przez trolla Silnorękiego")
    elif position == "+":
        print("\n" * 9)
        print("żródło życia")
    elif position == "?":
        print("\n" * 9)
        print("Niespodzianka - wpadasz do rowu z kolcami zostawionego przez łotrzyków i giniesz.")
    else:
        print("\n" * 9)
        print("Nie mozesz sie tu ruszyc")


def core(start_atrybuty):
    """ Main loop of the game."""
    with open('mapa_forest.txt', 'r') as myfile:
        mapa = myfile.read()
    mapa = list(mapa)
    position_horizontal = 1
    position_vertical = 18
    lenght_of_the_map_plus_one = 81
    map_copy = mapa[:]
    map_copy[position_horizontal + position_vertical * 81] = "@"
    while True:
        print("".join(map_copy))
        print("\nWciśnij W, S, A, D - poruszanie się, 'e' - ekwipunek, 'z' - dziennik, 'p' - pomoc, ")
        print("'g' - zapis gry, 'l' - legenda, 'k' - atrybuty lub '0' - wyjście z gry.")
        print("\n ___ _____      _   _  _____ ___ __  __        ___   ___      ___   ___ ___ ___ ")
        print("/ __|_  / |    /_\ | |/ /_ _| __|  \/  |      | _ ) /_\ \    / /_\ | _ \_ _|_ _|")
        print("\__ \/ /| |__ / _ \| ' < | || _|| |\/| |      | _ \/ _ \ \/\/ / _ \|   /| | | | ")
        print("|___/___|____/_/ \_\_|\_\___|___|_|  |_|      |___/_/ \_\_/\_/_/ \_\_|_\___|___|")
        input_char = getch()
        if input_char.upper() == 'W':
            os.system('clear')
            if map_copy[position_horizontal + (position_vertical - 1) * 81] != ".":
                collision(map_copy[position_horizontal + (position_vertical - 1) * 81])
            else:
                print("\n" * 10)
                map_copy[position_horizontal + position_vertical * 81] = "."
                position_vertical -= 1
                map_copy[position_horizontal + position_vertical * 81] = "@"
        elif input_char.upper() == 'S':
            os.system('clear')
            if map_copy[position_horizontal + (position_vertical + 1) * 81] != ".":
                collision(map_copy[position_horizontal + (position_vertical + 1) * 81])
            else:
                print("\n" * 10)
                map_copy[position_horizontal + position_vertical * 81] = "."
                position_vertical += 1
                map_copy[position_horizontal + position_vertical * 81] = "@"
        elif input_char.upper() == 'D':
            os.system('clear')
            if map_copy[(position_horizontal + 1) + position_vertical * 81] != ".":
                collision(map_copy[(position_horizontal + 1) + position_vertical * 81])
            else:
                print("\n" * 10)
                map_copy[position_horizontal + position_vertical * 81] = "."
                position_horizontal += 1
                map_copy[position_horizontal + position_vertical * 81] = "@"
        elif input_char.upper() == 'A':
            os.system('clear')
            if map_copy[(position_horizontal - 1) + position_vertical * 81] != ".":
                collision(map_copy[(position_horizontal - 1) + position_vertical * 81])
            else:
                print("\n" * 10)
                map_copy[position_horizontal + position_vertical * 81] = "."
                position_horizontal -= 1
                map_copy[position_horizontal + position_vertical * 81] = "@"
        elif input_char.upper() == 'E':
            os.system('clear')
            print("\n" * 9)
            print("Tu powinien być ekwipunek")
        elif input_char.upper() == 'Z':
            os.system('clear')
            print("\n" * 9)
            print("Tu powinien być dziennik")
        elif input_char.upper() == 'P':
            os.system('clear')
            print("\n" * 9)
            print("Tu powinien być pomoc")
        elif input_char.upper() == 'G':
            os.system('clear')
            print("\n" * 9)
            print("Tu powinien być zapis gry")
        elif input_char.upper() == 'L':
            os.system('clear')
            print("\n" * 2)
            print("Legenda:\n")
            print("W = Wioska Szwarzwald")
            print("? = Niespodzianka")
            print("M = Most trolla Silnorękiego")
            print("+ = Zródło życia")
            print("G = Gaj Łotrzyków")
            print("N = NPC")
        elif input_char.upper() == 'K':
            os.system('clear')
            print("\n" * 9)
            print(start_atrybuty)
        elif input_char.upper() == '0':
            os.system('clear')
            print("\nNa pewno? Wciśnij jeszcze raz '0' żeby wyjść z gry, coś innego żeby kontynuować.")
            input_char = getch()
            if input_char.upper() == '0':
                os.system('clear')
                break
            else:
                os.system('clear')
                print("\n" * 10)
                continue
        else:
            os.system('clear')
            print("\n" * 10)
            continue


def main():
    title_screen()
    początkowe_atrybuty = character_choice_screen()
    os.system('clear')
    core(początkowe_atrybuty)


main()
