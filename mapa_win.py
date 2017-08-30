import os
import sys
import time
from msvcrt import getch
os.system('cls')
# Komentarz ogólny : liczba wierszy na mapą zawsze musi być równa 10.


def delay_print(s):
    for c in s:
        sys.stdout.write('%s' % c)
        sys.stdout.flush()
        time.sleep(0.03)


def title_screen():
    delay_print("\n ___ _____      _   _  _____ ___ __  __        ___   ___      ___   ___ ___ ___ \n")
    delay_print("/ __|_  / |    /_\ | |/ /_ _| __|  \/  |      | _ ) /_\ \    / /_\ | _ \_ _|_ _|\n")
    delay_print("\__ \/ /| |__ / _ \| ' < | || _|| |\/| |      | _ \/ _ \ \/\/ / _ \|   /| | | | \n")
    delay_print("|___/___|____/_/ \_\_|\_\___|___|_|  |_|      |___/_/ \_\_/\_/_/ \_\_|_\___|___|\n")
    delay_print("\nROGUELIKE EXPERIENCE\n\n")
    print("Press any key to continue")
    input_char = getch()
    os.system('cls')


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
        print("Zródło życia")
    elif position == "?":
        print("\n" * 9)
        print("Niespodzianka - wpadasz do rowu z kolcami zostawionego przez łotrzyków i giniesz.")
    else:
        print("\n" * 9)
        print("Nie mozesz sie tu ruszyc")


def core():
    """ Main loop of the game."""
    print("\n" * 10)
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
        print("'g' - zapis gry, 'l' - legenda lub '0' - wyjście z gry.")
        print("\n ___ _____      _   _  _____ ___ __  __        ___   ___      ___   ___ ___ ___ ")
        print("/ __|_  / |    /_\ | |/ /_ _| __|  \/  |      | _ ) /_\ \    / /_\ | _ \_ _|_ _|")
        print("\__ \/ /| |__ / _ \| ' < | || _|| |\/| |      | _ \/ _ \ \/\/ / _ \|   /| | | | ")
        print("|___/___|____/_/ \_\_|\_\___|___|_|  |_|      |___/_/ \_\_/\_/_/ \_\_|_\___|___|")
        input_char = getch()
        if input_char.upper() == b'W':
            os.system('cls')
            if map_copy[position_horizontal + (position_vertical - 1) * 81] != ".":
                collision(map_copy[position_horizontal + (position_vertical - 1) * 81])
            else:
                print("\n" * 10)
                map_copy[position_horizontal + position_vertical * 81] = "."
                position_vertical -= 1
                map_copy[position_horizontal + position_vertical * 81] = "@"
        elif input_char.upper() == b'S':
            os.system('cls')
            if map_copy[position_horizontal + (position_vertical + 1) * 81] != ".":
                collision(map_copy[position_horizontal + (position_vertical + 1) * 81])
            else:
                print("\n" * 10)
                map_copy[position_horizontal + position_vertical * 81] = "."
                position_vertical += 1
                map_copy[position_horizontal + position_vertical * 81] = "@"
        elif input_char.upper() == b'D':
            os.system('cls')
            if map_copy[(position_horizontal + 1) + position_vertical * 81] != ".":
                collision(map_copy[(position_horizontal + 1) + position_vertical * 81])
            else:
                print("\n" * 10)
                map_copy[position_horizontal + position_vertical * 81] = "."
                position_horizontal += 1
                map_copy[position_horizontal + position_vertical * 81] = "@"
        elif input_char.upper() == b'A':
            os.system('cls')
            if map_copy[(position_horizontal - 1) + position_vertical * 81] != ".":
                collision(map_copy[(position_horizontal - 1) + position_vertical * 81])
            else:
                print("\n" * 10)
                map_copy[position_horizontal + position_vertical * 81] = "."
                position_horizontal -= 1
                map_copy[position_horizontal + position_vertical * 81] = "@"
        elif input_char.upper() == b'E':
            os.system('cls')
            print("\n" * 9)
            print("Tu powinien być ekwipunek")
        elif input_char.upper() == b'Z':
            os.system('cls')
            print("\n" * 9)
            print("Tu powinien być dziennik")
        elif input_char.upper() == b'P':
            os.system('cls')
            print("\n" * 9)
            print("Tu powinien być pomoc")
        elif input_char.upper() == b'G':
            os.system('cls')
            print("\n" * 9)
            print("Tu powinien być zapis gry")
        elif input_char.upper() == b'L':
            os.system('cls')
            print("\n" * 2)
            print("Legenda:\n")
            print("W = Wioska Szwarzwald")
            print("? = Niespodzianka")
            print("M = Most trolla Silnorękiego")
            print("+ = Zródło życia")
            print("G = Gaj Łotrzyków")
            print("N = NPC")
        elif input_char.upper() == b'0':
            os.system('cls')
            print("\nNa pewno? Wciśnij jeszcze raz '0' żeby wyjść z gry, coś innego żeby kontynuować.")
            input_char = getch()
            if input_char.upper() == b'0':
                os.system('cls')
                break
            else:
                os.system('cls')
                print("\n" * 10)
                continue
        else:
            os.system('cls')
            print("\n" * 10)
            continue


def main():
    title_screen()
    core()


main()
