import os
import sys
import time
import datetime
import random
import string
os.system('clear')
# Komentarz ogólny : liczba wierszy na mapą zawsze musi być równa 10.


def delay_print(s):
    ''' Spowalnia drukowanie tekstu. '''
    for c in s:
        sys.stdout.write('%s' % c)
        sys.stdout.flush()
        time.sleep(0.004)


def title_screen():
    ''' Zwraca ekran tytułowy. '''
    delay_print("\n ___ _____      _   _  _____ ___ __  __        ___   ___      ___   ___ ___ ___ \n")
    delay_print("/ __|_  / |    /_\ | |/ /_ _| __|  \/  |      | _ ) /_\ \    / /_\ | _ \_ _|_ _|\n")
    delay_print("\__ \/ /| |__ / _ \| ' < | || _|| |\/| |      | _ \/ _ \ \/\/ / _ \|   /| | | | \n")
    delay_print("|___/___|____/_/ \_\_|\_\___|___|_|  |_|      |___/_/ \_\_/\_/_/ \_\_|_\___|___|\n")
    delay_print("\nROGUELIKE EXPERIENCE\n\n")
    print("Wciśnij cokolwiek.")
    input_char = getch()
    os.system('clear')


def character_choice_screen():
    """ Funkcja zwraca atrybuty wybranego bohatera """
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
                print("SIŁA : 5, ZWINNOŚĆ : 2, PERCEPCJA: 1, INTELIGENCJA : 1, SIŁA WOLI : 2")
                print("\nWciśnij 'y' żeby wybrac tego bohatera, wciśnij coś innego żeby wrócić")
                input_char = getch()
                if input_char.upper() == 'Y':
                    return {"KLASA": "WOJOWNIK", "SIŁA": 5, "ZWINNOŚĆ": 2,
                            "PERCEPCJA": 1, "INTELIGENCJA": 1, "SIŁA WOLI": 2}
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
                    return {"KLASA": "ŁOWCA", "SIŁA": 2, "ZWINNOŚĆ": 3,
                            "PERCEPCJA": 3, "INTELIGENCJA": 1, "SIŁA WOLI": 2}
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
                    return {"KLASA": "NINJA", "SIŁA": 1, "ZWINNOŚĆ": 3,
                            "PERCEPCJA": 3, "INTELIGENCJA": 3, "SIŁA WOLI": 1}
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
                    klasa = input("Klasa postaci w której czujesz się najlepiej to: ")
                    klasa = klasa.upper()
                    print("Wybrałeś swoje przeznaczenie. Wciśnij cokolwiek, żeby rozpocząc gre.")
                    input_char = getch()
                    return {"KLASA": klasa, "SIŁA": siła, "ZWINNOŚĆ": zwinność, "PERCEPCJA": percepcja,
                            "INTELIGENCJA": inteligencja, "SIŁA WOLI": siła_woli}
        else:
            continue


def getch():
    ''' Umożliwia input bez entera. '''
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


def hot_warm_cold():
    os.system('clear')
    sekwencja_do_gry = []
    for i in range(3):
        string.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        losowa_liczba = random.choice(range(9))
        losowa_litera1 = random.choice(string.letters)
        losowa_litera2 = random.choice(string.letters)
        losowa_litera3 = random.choice(string.letters)
        wybór_do_gry = [str(losowa_liczba), losowa_litera1, losowa_litera2, losowa_litera3]
    for i in range(3):
        sekwencja_do_gry.append(random.choice(wybór_do_gry))
    while True:
        wybór_trudności = input("\nWybierz poziom trudnośći. 1, 2 lub 3 dla: łatwy, trudny lub życzenie śmierci:")
        if wybór_trudności == "1":
            print("\nMasz 15 prób. Jak zgadniejsz, dostaniesz punkt PERCEPCJI.")
            wybór_trudności = 15
            break
        if wybór_trudności == "2":
            print("\nMasz 10 prób. Jak zgadniejsz, dostaniesz 2 punkty PERCEPCJI.")
            wybór_trudności = 10
            break
        if wybór_trudności == "3":
            print("\nMasz 5 prób. Jak zgadniejsz, dostaniesz 3 punkty PERCEPCJI.")
            wybór_trudności = 5
            break
        else:
            print("\nPOWIEDZIAŁEM 1, 2 lub 3 !!!")
    print("\nPomyślałem o 3 elementowym miksie cyfr i liter. Zgadnij!")
    print("Pamietaj:")
    print("Jak mówie", " " * 5, "to znaczy, że:\n")
    print("Zimno", " " * 9, "nie zgadłeś")
    print("Ciepło", " " * 8, "zgadłeś ale w złych pozycjach")
    print("Gorąco", " " * 8, "co najmniej jeden element jest dobrze i w dobrej pozycji.")
    for i in range(wybór_trudności):
        próba = input("--->")
        próba = list(próba.upper())
        if próba == sekwencja_do_gry:
            print("\nBrawo!!! Dostajesz punkty do PERCEPCJI.\nWciśnij cokolwiek, żeby kontynuować.")
            input_char = getch()
            return wybór_trudności
        else:
            if len(próba) > 3:
                print("Chyba zapomniałeś, że zgadujesz tylko 3 elementy.....")
                continue
            i = 0
            podpowiedzi = []
            for i in range(len(próba)):
                if próba[i] in sekwencja_do_gry:
                    if próba[i] == sekwencja_do_gry[i]:
                        podpowiedzi.append("Gorąco")
                    else:
                        podpowiedzi.append("Ciepło")
                else:
                    podpowiedzi.append("Zimno")
                i += 1
            lista_podpowiedzi = []
            for i in range(podpowiedzi.count("Gorąco")):
                lista_podpowiedzi.append("Gorąco")
            for i in range(podpowiedzi.count("Ciepło")):
                lista_podpowiedzi.append("Ciepło")
            for i in range(podpowiedzi.count("Zimno")):
                lista_podpowiedzi.append("Zimno")
            print(" ".join(lista_podpowiedzi))
            continue
    print("\nNie zgadłeś! Odpowiedz to:", " ".join(sekwencja_do_gry), " .Wciśnij cokolwiek.")
    input_char = getch()
    return 0


def collision(position):
    """ Zwraca zdarzenie w zalezności od tego w co wejdzie bohater. """
    if position == "N":
        print("\n" * 9)
        print("Tutaj NPC powie ci co masz robić dalej.")
    elif position == "W":
        print("\n" * 9)
        print("Trafiłeś do wioski Szwarzwald")
    elif position == "C":
        print("\n" * 6)
        delay_print("Spotykasz troglodyte Mariana. To może oznaczać tylko jedno:\n")
        delay_print("Czas na gre hot and cold. ")
        delay_print("Nacisnij cokolwiek, żeby zacząć.")
        input_char = getch()
        wybór_trudności = hot_warm_cold()
        os.system('cls')
        print("\n" * 10)
        return wybór_trudności
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


def core(atrybuty, start_czasu):
    """ Główna pętla całej gry. """
    # Inicjujemy 2 zmienne potrzebne do ruchów i wyników zdarzeń, input char musi byc string dla funkcji upper().
    wyniki_zdarzeń = None
    input_char = "0"
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
        if input_char.upper() in [b'W', b'S', b'D', b'A']:
            # Wyniki_zdarzeń otrzymujemy tylko po każdym ruchu.
            # 1. Wyniki zdarzeń hot_and_cold.
            if wyniki_zdarzeń == 0:
                atrybuty["PERCEPCJA"] -= 1
            elif wyniki_zdarzeń == 5:
                atrybuty["PERCEPCJA"] += 3
            elif wyniki_zdarzeń == 10:
                atrybuty["PERCEPCJA"] += 2
            elif wyniki_zdarzeń == 15:
                atrybuty["PERCEPCJA"] += 1
        # Reset wyników_zdarzeń.
        wyniki_zdarzeń = None
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
                wyniki_zdarzeń = collision(map_copy[position_horizontal + (position_vertical - 1) * 81])
            else:
                print("\n" * 10)
                map_copy[position_horizontal + position_vertical * 81] = "."
                position_vertical -= 1
                map_copy[position_horizontal + position_vertical * 81] = "@"
        elif input_char.upper() == 'S':
            os.system('clear')
            if map_copy[position_horizontal + (position_vertical + 1) * 81] != ".":
                wyniki_zdarzeń = collision(map_copy[position_horizontal + (position_vertical + 1) * 81])
            else:
                print("\n" * 10)
                map_copy[position_horizontal + position_vertical * 81] = "."
                position_vertical += 1
                map_copy[position_horizontal + position_vertical * 81] = "@"
        elif input_char.upper() == 'D':
            os.system('clear')
            if map_copy[(position_horizontal + 1) + position_vertical * 81] != ".":
                wyniki_zdarzeń = collision(map_copy[(position_horizontal + 1) + position_vertical * 81])
            else:
                print("\n" * 10)
                map_copy[position_horizontal + position_vertical * 81] = "."
                position_horizontal += 1
                map_copy[position_horizontal + position_vertical * 81] = "@"
        elif input_char.upper() == 'A':
            os.system('clear')
            if map_copy[(position_horizontal - 1) + position_vertical * 81] != ".":
                wyniki_zdarzeń = collision(map_copy[(position_horizontal - 1) + position_vertical * 81])
            else:
                print("\n" * 10)
                map_copy[position_horizontal + position_vertical * 81] = "."
                position_horizontal -= 1
                map_copy[position_horizontal + position_vertical * 81] = "@"
        # Akcje bohatera inne niż ruch WSAD.
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
            print("\n")
            print("Legenda:\n")
            print("W = Wioska Szwarzwald")
            print("? = Niespodzianka")
            print("M = Most trolla Silnorękiego")
            print("+ = Zródło życia")
            print("G = Gaj Łotrzyków")
            print("N = NPC")
            print("C = Zimno/ ciepła niespodzianka Mariana.")
        elif input_char.upper() == 'K':
            os.system('clear')
            print("\n" * 8)
            for k, v in atrybuty.items():
                print(k, ":", v)
        elif input_char.upper() == '0':
            # Kończenie gry i wpisywanie na hall of fame.
            os.system('clear')
            print("\nNa pewno? Wciśnij jeszcze raz '0' żeby wyjść z gry, coś innego żeby kontynuować.")
            input_char = getch()
            if input_char.upper() == '0':
                os.system('clear')
                koniec_czasu = datetime.datetime.now()
                # Pozbywamy się mikrosekund.
                czas_gry = (str(koniec_czasu - start_czasu)).split(".")[0]
                # Zsumujmy atrybuty.
                suma_atrybutów = 0
                for value in atrybuty.values():
                    try:
                        suma_atrybutów += int(value)
                    except ValueError:
                        continue
                imię_użytkownika = input("\nWpisz swoje imię: ")
                print("\nGratulacje,", imię_użytkownika, ". Twoje osiągnięcia zostaną zapisane.\n")
                print("ATRYBUTY NA KONIEC: \n")
                # Dopasujmy długość imienia użytkownika do 20.
                if len(imię_użytkownika) > 20:
                    imię_użytkownika = imię_użytkownika[:20]
                imię_użytkownika += " " * (20 - len(imię_użytkownika))
                for k, v in atrybuty.items():
                    print(k, ":", v)
                print("\nCZAS GRY: ", czas_gry, "\nSUMA ATRYBUTÓW: ", suma_atrybutów)
                # Dodaj końcowy wynik do pliku HALL_OF_FAME.
                with open("HALL_OF_FAME.txt", "a", encoding='utf-8') as HALL_OF_FAME:
                    wynik_gracza = [str(suma_atrybutów), str(imię_użytkownika), str(czas_gry),
                                    str(atrybuty["KLASA"])]
                    wynik_gracza = "        ".join(wynik_gracza)
                    HALL_OF_FAME.write(str(wynik_gracza) + "\n")
                    print("\n\nNacisnij cokolwiek")
                    input_char = getch()
                with open("HALL_OF_FAME.txt", "r", encoding='utf-8') as HALL_OF_FAME:
                    os.system('clear')
                    print("\nHALL_OF_FAME:\n")
                    # Odzielamy co 3 żeby było równo.
                    print(" " * 3,  "PUNKTY", " " * 2, "GRACZ", " " * 21, "CZAS", " " * 9, "KLASA\n")
                    HALL_OF_FAME = sorted(HALL_OF_FAME.readlines(), reverse=True)
                    miejsce_na_liście = 1
                    for i in HALL_OF_FAME:
                        print(miejsce_na_liście, ".", "".join(i))
                        miejsce_na_liście += 1
                    print("\n\n\nNacisnij cokolwiek")
                    input_char = getch()
                    os.system('cls')
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
    start_czasu = datetime.datetime.now()
    core(początkowe_atrybuty, start_czasu)


main()
