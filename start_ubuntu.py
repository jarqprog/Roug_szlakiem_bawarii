# Imports from Standard Library
import os
import sys
import time
import datetime
import random
import string
# Imports from user-defined modules.
import mod_hero
import mod_display
import mod_items
import mod_enemy
import mod_event
import mod_items

os.system("clear")


def delay_print(s):
    """ Delays printing. """
    for c in s:
        sys.stdout.write("%s" % c)
        sys.stdout.flush()
        time.sleep(0.004)


def developers():
    """ Returns info about authors screen. """
    print("\x1b[6;31;47m" + "Wciśnij cokolwiek." + "\x1b[0m")
    delay_print("\n\n\n" + "\t" + "Słuchacze CODECOOL'a \n\n\nJarosław Kucharczyk i Łukasz Malko\n\n\n" + "\t" + "PRZEDSTAWIAJĄ:")
    input_char = getch()
    os.system("clear")


def title_screen():
    """ Returns title screen """
    delay_print("\n ___ _____      _   _  _____ ___ __  __        ___   ___      ___   ___ ___ ___ \n")
    delay_print("/ __|_  / |    /_\ | |/ /_ _| __|  \/  |      | _ ) /_\ \    / /_\ | _ \_ _|_ _|\n")
    delay_print("\__ \/ /| |__ / _ \| ' < | || _|| |\/| |      | _ \/ _ \ \/\/ / _ \|   /| | | | \n")
    delay_print("|___/___|____/_/ \_\_|\_\___|___|_|  |_|      |___/_/ \_\_/\_/_/ \_\_|_\___|___|\n")
    delay_print("\nROGUELIKE EXPERIENCE\n\n")
    print("\x1b[6;31;47m" + "Wciśnij cokolwiek." + "\x1b[0m")
    input_char = getch()
    os.system("clear")


def plot():
    """ Returns plot screen."""
    print("\n\n\n\n\n")
    delay_print("\x1b[6;30;43m" + "Dawno, dawno temu w Bawarii...Twój przyjaciel, pustelnik Mullog, został okradziony.\n"
                + "\x1b[0m")
    delay_print("\x1b[6;30;43m" + "Karzeł Oblib zwędził mu drogocenną obrączkę - prezent urodziowy od przyjaciela z młodości.\n"
                + "\x1b[0m")
    delay_print("\x1b[6;30;43m" + "Mullog usycha z żalu, błaga Cię o pomoc.\n" + "\x1b[0m")
    delay_print("\x1b[6;30;43m" + "Wyruszasz zatem, a trop Obliba doprowadza Cię do 'Doliny Łotrzyków'...\n" + "\x1b[0m")
    print("\x1b[6;31;47m" + "Wciśnij cokolwiek." + "\x1b[0m")
    input_char = getch()
    os.system("clear")


def character_choice_screen(hero):
    """ Returns starting attributes. """
    while True:
        os.system("clear")
        print("\x1b[6;30;45m" + "\n _    _       _                                  _             _ " + "\x1b[0m")
        print("\x1b[6;30;45m" + "| |  | |     | |                                | |           (_)" + "\x1b[0m")
        print("\x1b[6;30;45m" + "| |  | |_   _| |__   ___  _ __   _ __   ___  ___| |_ __ _  ___ _ " + "\x1b[0m")
        print("\x1b[6;30;45m" + "| |/\| | | | | '_ \ / _ \| '__| | '_ \ / _ \/ __| __/ _` |/ __| |" + "\x1b[0m")
        print("\x1b[6;30;45m" + "\  /\  / |_| | |_) | (_) | |    | |_) | (_) \__ \ || (_| | (__| |" + "\x1b[0m")
        print("\x1b[6;30;45m" + " \/  \/ \__, |_.__/ \___/|_|    | .__/ \___/|___/\__\__,_|\___|_|" + "\x1b[0m")
        print("\x1b[6;30;45m" + "         __/ |                  | |                              " + "\x1b[0m")
        print("\x1b[6;30;45m" + "        |___/                   |_|                              \n\n" + "\x1b[0m")
        delay_print("Wybierz swoje przeznaczenie:\n")
        delay_print("\x1b[6;30;41m" + "\n1. WOJOWNIK\n" + "\x1b[0m")
        delay_print("\x1b[6;30;42m" + "\n2. ŁOWCA\n" + "\x1b[0m")
        delay_print("\x1b[6;30;44m" + "\n3. NINJA\n" + "\x1b[0m")
        delay_print("\x1b[6;30;43m" + "\n4. STWÓRZ WŁASNĄ POSTAĆ\n" + "\x1b[0m")
        input_char = getch()
        if input_char.upper() == "1":
            os.system("clear")
            with open("1. WOJOWNIK.txt", "r") as myfile:
                picture = myfile.read()
                print(picture)
                print("WOJOWNIK")
                print("ATRYBUTY:")
                print("SIŁA : 5, ZWINNOŚĆ : 2, PERCEPCJA: 1, INTELIGENCJA : 1, SIŁA WOLI : 2")
                print("Wciśnij 'y' żeby wybrac tego bohatera, wciśnij coś innego żeby wrócić")
                input_char = getch()
                if input_char.upper() == "Y":
                    os.system("clear")
                    warrior_attr_dict = {"siła": 5, "zwinność": 2, "percepcja": 1, "inteligencja": 1, "siła woli": 2}
                    hero.attrib_dict.update(warrior_attr_dict)
                    hero.proffession = "Wojownik"
                    return hero
        if input_char.upper() == "2":
            os.system("clear")
            with open("2. ŁOWCA.txt", "r") as myfile:
                picture = myfile.read()
                print(picture)
                print("ŁOWCA")
                print("ATRYBUTY:")
                print("SIŁA : 2, ZWINNOŚĆ : 3, PERCEPCJA: 3, INTELIGENCJA : 1, SIŁA WOLI : 2")
                print("Wciśnij 'y' żeby wybrac tego bohatera, wciśnij coś innego żeby wrócić")
                input_char = getch()
                if input_char.upper() == "Y":
                    os.system("clear")
                    hunter_attr_dict = {"siła": 2, "zwinność": 3, "percepcja": 3, "inteligencja": 3, "siła woli": 2}
                    hero.attrib_dict.update(hunter_attr_dict)
                    hero.proffession = "Łowca"
                    return hero
        if input_char.upper() == "3":
            os.system("clear")
            with open("3. NINJA.txt", "r") as myfile:
                picture = myfile.read()
                print(picture)
                print("NINJA")
                print("ATRYBUTY:")
                print("SIŁA : 1, ZWINNOŚĆ : 3, PERCEPCJA: 3, INTELIGENCJA : 3, SIŁA WOLI : 1")
                print("Wciśnij 'y' żeby wybrac tego bohatera, wciśnij coś innego żeby wrócić")
                input_char = getch()
                if input_char.upper() == "Y":
                    os.system("clear")
                    ninja_attr_dict = {"siła": 1, "zwinność": 3, "percepcja": 3, "inteligencja": 3, "siła woli": 1}
                    hero.attrib_dict.update(ninja_attr_dict)
                    hero.proffession = "Ninja"
                    return hero
        if input_char.upper() == "4":
            os.system("clear")
            with open("4. STWORZONA POSTAĆ.txt", "r") as myfile:
                picture = myfile.read()
                print(picture)
                print("NIEZNAJOMY")
                print("\nATRYBUTY:")
                print("\nSIŁA : 1, ZWINNOŚĆ : 1, PERCEPCJA: 1, INTELIGENCJA : 1, SIŁA WOLI : 1\n\n\n")
                print("To ekran tworzenia postaci. Dostaniesz do rozdysponowanie 6 punktów.")
                print("Wciśnij 'y' żeby stworzyć swoją postać, wciśnij coś innego żeby wrócić.")
                input_char = getch()
                if input_char.upper() == "Y":
                    character_created = create_character(hero)
                    return character_created
        else:
            continue


def create_character(hero):
    """ Returns created character. """
    os.system("clear")
    strenght = 1
    agility = 1
    cognition = 1
    brainpower = 1
    willpower = 1
    points = 6
    while True:
        os.system("clear")
        if points == 0:
            break
        else:
            print("\n\nSIŁA", strenght, "ZWINNOŚĆ", agility, "PERCEPCJA", cognition)
            print("INTELIGENCJA", brainpower, "SIŁA WOLI", willpower)
            print("Masz", points, "punktów atrybutów do rozdysponowania.")
            print("Wciśnij 's', 'z', 'p', 'i', 'w' żeby dodać punkt do atrybutu")
            print("kolejno: siły, zwinności, percepcji, inteligencji, siły woli.")
            input_char = getch()
            if input_char.upper() == "S":
                strenght += 1
                points -= 1
                continue
            if input_char.upper() == "Z":
                agility += 1
                points -= 1
                continue
            if input_char.upper() == "P":
                cognition += 1
                points -= 1
                continue
            if input_char.upper() == "I":
                brainpower += 1
                points -= 1
                continue
            if input_char.upper() == "W":
                willpower += 1
                points -= 1
                continue
            else:
                continue
    print("\n\nSIŁA", strenght, "ZWINNOŚĆ", agility, "PERCEPCJA", cognition)
    print("INTELIGENCJA", brainpower, "SIŁA WOLI", willpower)
    klasa = input("Klasa postaci w której czujesz się najlepiej to: ")
    klasa = klasa.upper()
    print("\x1b[6;30;42m" + "Wybrałeś swoje przeznaczenie. Wciśnij coś i rozpocznij gre!." + "\x1b[0m")
    input_char = getch()
    os.system("clear")
    created_attr_dict = {"siła": strenght, "zwinność": agility, "percepcja": cognition,
                            "inteligencja": brainpower, "siła woli": willpower}
    hero.attrib_dict.update(created_attr_dict)
    hero.proffession = klasa
    return hero
        

def getch():
    """ Returns input without 'enter'. """
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


def controls():
    """ Returns controls screen. """
    print("\n\nHOW-TO-PLAY-SCREEN\nPORUSZASZ SIĘ PO MAPIE UZYWAJĄC W, S, A, D\nZaawansowane sterowanie jest pod mapką.")
    print("\x1b[6;31;47m" + "Wciśnij cokolwiek." + "\x1b[0m")
    input_char = getch()
    os.system("clear")


def hot_warm_cold():
    """ Hot warm cold mini-game. """
    os.system("clear")
    correct_answer = []
    string.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Collecting random choices.
    random_number = random.choice(range(9))
    random_letter1 = random.choice(string.letters)
    random_letter2 = random.choice(string.letters)
    random_letter3 = random.choice(string.letters)
    choices_for_sequence = [str(random_number), random_letter1, random_letter2, random_letter3]
    for e in range(3):
        i = random.choice(choices_for_sequence)
        choices_for_sequence.remove(i)
        correct_answer.append(i)
    # Difficulty choice.
    while True:
        difficulty_choice = input("\nWybierz poziom trudnośći. 1, 2 lub 3 dla: łatwy, trudny lub życzenie śmierci:")
        if difficulty_choice == "1":
            print("\nMasz 15 prób. Jak zgadniejsz, dostaniesz punkt PERCEPCJI.")
            difficulty_choice = 15
            break
        if difficulty_choice == "2":
            print("\nMasz 10 prób. Jak zgadniejsz, dostaniesz 2 punkty PERCEPCJI.")
            difficulty_choice = 10
            break
        if difficulty_choice == "3":
            print("\nMasz 5 prób. Jak zgadniejsz, dostaniesz 3 punkty PERCEPCJI.")
            difficulty_choice = 5
            break
        else:
            print("\nPOWIEDZIAŁEM 1, 2 lub 3 !!!")
    # Give instructions to player.
    print("\nPomyślałem o 3 elementowym miksie cyfr i liter. Zgadnij!")
    print("Pamietaj:")
    print("Jak mówie", " " * 5, "to znaczy, że:\n")
    print("Zimno", " " * 9, "nie zgadłeś")
    print("Ciepło", " " * 8, "zgadłeś ale w złych pozycjach")
    print("Gorąco", " " * 8, "co najmniej jeden element jest dobrze i w dobrej pozycji.")
    for i in range(difficulty_choice):
        # Player takes guess.
        user_guess = input("--->")
        user_guess = list(user_guess.upper())
        if user_guess == correct_answer:
            print("\nBrawo!!! Dostajesz punkty do PERCEPCJI.\nWciśnij cokolwiek, żeby kontynuować.")
            input_char = getch()
            return difficulty_choice
        else:
            if len(user_guess) != 3:
                print("Chyba zapomniałeś, że zgadujesz 3 elementy.....")
                continue
            i = 0
            # Collecting hints for player.
            suggestions = []
            for element in correct_answer:
                if element == user_guess[i]:
                    suggestions.insert(0, "HOT!")
                elif element in user_guess:
                    suggestions.append("WARM!")
                i += 1
            if not suggestions:
                suggestions.append("COLD!")
        print(suggestions)
    print("\nNie zgadłeś! Odpowiedz to:", " ".join(correct_answer),
          " .Ale dostaniesz 1 percepcji za dobre chęci. Wciśnij cokolwiek.")
    input_char = getch()
    difficulty_choice = 0
    return difficulty_choice


def hot_warm_cold_boss(hero, start_time):
    """ Hot warm cold boss mini-game. """
    os.system("clear")
    with open("wizard.txt", "r") as wizard:
        picture = wizard.read()
    print("\x1b[6;30;41m" + picture + "\x1b[0m")
    correct_answer = []
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # Collecting random choices.
    for e in range(3):
        i = random.choice(numbers)
        numbers.remove(i)
        correct_answer.append(i)
    # Give instructions to player.
    print("\nW końcu jestes godny zmierzenia się z moją szaradą !!!")
    print("\nPomyślałem o 3 cyfrowej liczbie. Zgadnij! ALBO GIŃ HAHAHAHAHA !!!!")
    print("\nMasz 15 prób!!!")
    print("Pamietaj:")
    print("Jak mówie", " " * 5, "to znaczy, że:\n")
    print("Zimno", " " * 9, "nie zgadłeś")
    print("Ciepło", " " * 8, "zgadłeś ale w złych pozycjach")
    print("Gorąco", " " * 8, "co najmniej jeden element jest dobrze i w dobrej pozycji.")
    for i in range(15):
        # Player takes guess.
        user_guess = input("--->")
        user_guess = list(user_guess.upper())
        if user_guess == correct_answer:
            print("\nBrawo!!! WYGRAŁEŚ !!! ")
            input_char = getch()
            win_screen(hero, start_time)
        else:
            if len(user_guess) != 3:
                print("Chyba zapomniałeś, że zgadujesz 3 elementy.....")
                continue
            i = 0
            # Collecting hints for player.
            suggestions = []
            for element in correct_answer:
                if element == user_guess[i]:
                    suggestions.insert(0, "HOT!")
                elif element in user_guess:
                    suggestions.append("WARM!")
                i += 1
            if not suggestions:
                suggestions.append("COLD!")
        print(suggestions)
    print("\nNie zgadłeś! Odpowiedz to:", " ".join(correct_answer),
          " . GINIESZ !!!")
    input_char = getch()
    loose_screen(hero, start_time)


def game_events(position, hero, start_time):
    """ Returns event. """
    # ENEMY CLASS IMPORT TO MAIN:
    enemy = mod_enemy.enemy_settings(name=None, loc=None, lvl=None, gen=None)
    enemy.attack = mod_enemy.attack_points_calc(enemy=enemy)
    enemy.defend = mod_enemy.defend_points_calc(enemy=enemy)
    enemy.combat_attribute = mod_enemy.combat_attribute_default(enemy=enemy)
    # 1st level events:
    if position == "M":
        print("\n" * 9)
        print("Trafiłeś NA DZIWNY MIŚ.")
    elif position == "L":
        print("\n" * 9)
        print("Trafiłeś NA LEŚNICZY.")
    elif position == "R":
        print("\n" * 9)
        print("Trafiłeś OBÓZ NIESŁUSZNIE ROZBITYCH.")
    elif position == "D":
        print("\n" * 9)
        print("Trafiłeś NA DOM BABCI.")
    elif position == "Z":
        print("\n" * 9)
        print("Trafiłeś NA ZŁY WILK.")
    elif position == "H":
        print("\n" * 6)
        delay_print("Spotykasz troglodyte Mariana. To może oznaczać tylko jedno:\n")
        delay_print("Czas na gre hot and cold. ")
        delay_print("\x1b[6;31;47m" + "Wciśnij cokolwiek, żeby zacząć." + "\x1b[0m")
        input_char = getch()
        difficulty_choice = hot_warm_cold()
        os.system("clear")
        print("\n" * 10)
        return difficulty_choice
    elif position == "+":
        print("\n" * 9)
        print("żródło życia")
    elif position == "?":
        mod_event.event_fight(enemy=mod_enemy.enemy_settings(name=None, loc=hero.location, lvl=None, gen=None),
                              hero=hero)
        os.system("clear")
        print("\n" * 10)
    # 2nd level events:
    elif position == "N":
        print("\n" * 7)
        print("Zbliza się do Ciebie dziadek NPC i zaczyna radzić:")
        print("'-Na Twoim miejscu udałbym się do wioski na północ, może znajdziec tam pomocna informację, na razie.'")
        print("Dziadek NPC zostaje w pobliżu na wszelki wypadek gdyby musiał tobie powtórzyć co powiedział.")
    elif position == "W":
        print("\n" * 9)
        print("Trafiłeś do wioski Szwarzwald")
    elif position == "G":
        print("\n" * 9)
        print("Trafiłeś do gaju Łotrzyków.")
    elif position == "T":
        print("\n" * 9)
        print("Most pilnowany przez trolla Silnorękiego")
    # 3rd level events:
    elif position == "P":
        print("\n" * 9)
        print("Trafiłeś NA PRZEŁĘCZ ZGUBY.")
    elif position == "S":
        print("\n" * 9)
        print("Trafiłeś NA SZCZYT ROZPACZY.")
    elif position == "F":
        print("\n" * 9)
        print("Trafiłeś NA FASOLOWE POLE.")
    elif position == "C":
        print("\n" * 9)
        print("Trafiłeś NA CHATA PUSTELNIKA.")
    # 4th level events:
    elif position == "B":
        hot_warm_cold_boss(hero = hero, start_time = start_time)
    # For all maps:
    else:
        print("\n" * 9)
        print("\x1b[6;30;41m" + "Nie mozesz sie tu ruszyc" + "\x1b[0m")


def hall_of_fame(hero, start_time):
    """ Exports to and reads from hall of fame.txt."""
    os.system("clear")
    finish_time = datetime.datetime.now()
    # Get rid of microseconds.
    game_time = (str(finish_time - start_time)).split(".")[0]
    # Sum up attributes.
    sum_of_attributes = 0
    for value in hero.attrib_dict.values():
        try:
            sum_of_attributes += int(value)
        except ValueError:
            continue
    user_name = input("\nWpisz swoje prawdziwe imię: ")
    print("\nGratulacje,", user_name, ".Twoje osiągnięcia zostaną zapisane.\n")
    print("ATRYBUTY NA KONIEC: \n")
    # User_name length must = 20.
    user_name = '{:.20}'.format(user_name)
    user_name += " " * (20 - len(user_name))
    for k, v in hero.attrib_dict.items():
        print(k, ":", v)
    print("\nCZAS GRY: ", game_time, "\nSUMA ATRYBUTÓW: ", sum_of_attributes,
            "\nKLASA: ", hero.proffession)
    # Add final results to Hall of Fame.
    with open("HALL_OF_FAME.txt", "a", encoding='utf-8') as HALL_OF_FAME:
        user_score = [str(sum_of_attributes), str(user_name), str(game_time),
                        str(hero.proffession)]
        user_score = "        ".join(user_score)
        HALL_OF_FAME.write(str(user_score) + "\n")
        print("\x1b[6;31;47m" + "Wciśnij cokolwiek." + "\x1b[0m")
        input_char = getch()
    with open("HALL_OF_FAME.txt", "r", encoding='utf-8') as HALL_OF_FAME:
        os.system("clear")
        print("\nHALL_OF_FAME:\n")
        # Use pre-calculated number of spaces to fit the results.
        print(" " * 3,  "PUNKTY", " " * 2, "GRACZ", " " * 21, "CZAS", " " * 9, "KLASA\n")
        HALL_OF_FAME = sorted(HALL_OF_FAME.readlines(), reverse=True)
        list_place = 1
        for i in HALL_OF_FAME:
            # Format list place display to {:04d}.
            print('{:04d}'.format(list_place), ".", "".join(i))
            list_place += 1
        print("\x1b[6;31;47m" + "Wciśnij 'Y' żeby zagrać jeszcze raz, coś innego żeby wyjść." + "\x1b[0m")
        input_char = getch()
        os.system("clear")
        if  input_char.upper() == "Y":
            main()
        else:
            sys.exit()


def win_screen(hero, start_time):
    """ Returns win screen. """
    os.system("clear")
    print("     .--------.")
    print("   .'          '.")
    print("  (   O      O   )")
    print(" :                :")
    print(" |                | ")
    print(" : ',          ,' :")
    print("  (  '-......-'  )")
    print("   '.          .'")
    print("     '-......-'")
    print(" \t\tWYGRAŁEŚ!!!")
    input_char = getch()
    hall_of_fame(hero, start_time)


def loose_screen(hero, start_time):
    """ Returns loose screen. """
    os.system("clear")
    print("     .-......-.")
    print("   .'          '.")
    print("  (   O      O   )")
    print(" :           `    :")
    print(" |                | ")
    print(" :    .------.    :")
    print("  (  '        '  )")
    print("   '.          .'")
    print("     '-......-'")
    print("\t\tPRZEGRAŁEŚ!!!")
    input_char = getch()
    hall_of_fame(hero, start_time)


def set_map(hero, start_time, board):
    """ Prints map. """
    # If nothing else displayed above map - display calendar.
    mod_display.display_calendar_location(hero = hero)
    # General comment - lines above the map always = 10.
    print("\n" * 7)
    with open(board, 'r') as myfile:
        board = myfile.read()
    board = list(board)
    position_horizontal = 1
    position_vertical = 18
    board[position_horizontal + position_vertical * 81] = ("\x1b[6;30;42m" + "@" + "\x1b[0m")
    movement(hero, start_time, board, position_horizontal, position_vertical)

def movement(hero, start_time, board, position_horizontal, position_vertical):
    """ Returns input_char WSAD result. """
    # Initiate non-empty variable for upper() compatibility.
    input_char = "0"
    event_result = None
    while True:
        if input_char.upper() in ["W", "S", "D", "A"]:
            # Event_results for hot_and_cold mini-game.
            if event_result == 0:
                hero.attrib_dict["percepcja"] += 1
            elif event_result == 5:
                hero.attrib_dict["percepcja"] += 4
            elif event_result == 10:
                hero.attrib_dict["percepcja"] += 3
            elif event_result == 15:
                hero.attrib_dict["percepcja"] += 2
        # Event_results value reset.
        event_result = None
        print("".join(board))
        print("\nWciśnij W, S, A, D - poruszanie się, 'e' - karta bohatera, 'z' - dziennik, 'p' - pomoc, ")
        print("'g' - zapis gry, 'l' - legenda, 'k' - atrybuty lub '0' - wyjście z gry.")
        print("\n ___ _____      _   _  _____ ___ __  __        ___   ___      ___   ___ ___ ___ ")
        print("/ __|_  / |    /_\ | |/ /_ _| __|  \/  |      | _ ) /_\ \    / /_\ | _ \_ _|_ _|")
        print("\__ \/ /| |__ / _ \| ' < | || _|| |\/| |      | _ \/ _ \ \/\/ / _ \|   /| | | | ")
        print("|___/___|____/_/ \_\_|\_\___|___|_|  |_|      |___/_/ \_\_/\_/_/ \_\_|_\___|___|")
        input_char = getch()
        # 81 = length of the map.
        if input_char.upper() == "W":
            os.system("clear")
            if board[position_horizontal + (position_vertical - 1) * 81] != ".":
                event_result = game_events(board[position_horizontal + (position_vertical - 1) * 81], hero, start_time)
            else:
                mod_display.display_calendar_location(hero = hero)
                print("\n" * 7)
                board[position_horizontal + position_vertical * 81] = "."
                position_vertical -= 1
                board[position_horizontal + position_vertical * 81] = ("\x1b[6;30;42m" + "@" + "\x1b[0m")
        elif input_char.upper() == "S":
            os.system("clear")
            if board[position_horizontal + (position_vertical + 1) * 81] != ".":
                event_result = game_events(board[position_horizontal + (position_vertical + 1) * 81], hero, start_time)
            else:
                mod_display.display_calendar_location(hero = hero)
                print("\n" * 7)
                board[position_horizontal + position_vertical * 81] = "."
                position_vertical += 1
                board[position_horizontal + position_vertical * 81] = ("\x1b[6;30;42m" + "@" + "\x1b[0m")
        elif input_char.upper() == "D":
            os.system("clear")
            if board[(position_horizontal + 1) + position_vertical * 81] != ".":
                event_result = game_events(board[(position_horizontal + 1) + position_vertical * 81], hero, start_time)
            else:
                mod_display.display_calendar_location(hero = hero)
                print("\n" * 7)
                board[position_horizontal + position_vertical * 81] = "."
                position_horizontal += 1
                board[position_horizontal + position_vertical * 81] = ("\x1b[6;30;42m" + "@" + "\x1b[0m")
        elif input_char.upper() == "A":
            os.system("clear")
            if board[(position_horizontal - 1) + position_vertical * 81] != ".":
                event_result = game_events(board[(position_horizontal - 1) + position_vertical * 81], hero, start_time)
            else:
                mod_display.display_calendar_location(hero = hero)
                print("\n" * 7)
                board[position_horizontal + position_vertical * 81] = "."
                position_horizontal -= 1
                board[position_horizontal + position_vertical * 81] = ("\x1b[6;30;42m" + "@" + "\x1b[0m")
        else:
            input_char_not_movement(hero, start_time, board, input_char, event_result)


def input_char_not_movement(hero, start_time, board, input_char, event_result):
    """ Returns input_char result different than movement. """
    if input_char.upper() == "E":
        mod_display.display_hero_chart(hero=hero)
        print("\x1b[6;31;47m" + "Wciśnij cokolwiek, żeby wyjść." + "\x1b[0m")
        input_char = getch()
        os.system("clear")
        print("\n" * 10)
    elif input_char.upper() == "Z":
        os.system("clear")
        print("\n" * 9)
        print("Tu powinien być dziennik")
    elif input_char.upper() == "P":
        os.system("clear")
        print("\n" * 9)
        print("Tu powinien być pomoc")
    elif input_char.upper() == "G":
        os.system("clear")
        print("\n" * 9)
        print("Tu powinien być zapis gry")
    elif input_char.upper() == "L":
        os.system("clear")
        print("Legenda:\n\n")
        print("B = Boss" + "\t" + "L = Lesniczy" + "\t" + "B = Dom Babci")
        print("O = Obóz niesłusznie rozbitych" + "\t" + "Z = Zły wilk")
        print("W = Wioska Szwarzwald" + "\t" + "M = Dziwny Miś")
        print("? = Niespodzianka - moze fanty, może psikus" + "\t" + "T = Most trolla Silnorękiego")
        print("+ = Zródło życia" + "\t" + "P = Przełęcz zguuuby")
        print("G = Gaj Łotrzyków" + "\t" + "F = Fasolowe pole")
        print("N = Dziadek NPC" + "\t" + "S = Szczyt rozpaczy")
        print("H = Zimno/ciepła niespodzianka Mariana. Prowadzą do zmian w percepcji."
                + "P̶o̶t̶r̶a̶k̶t̶u̶j̶ ̶t̶o̶ ̶j̶a̶k̶o̶ ̶t̶r̶e̶n̶i̶n̶g̶ ̶p̶r̶z̶e̶d̶ ̶b̶o̶s̶s̶e̶m̶. Baw się dobrze!")
    elif input_char.upper() == "K":
        os.system("clear")
        print("\n" * 4)
        print("KLASA: ", hero.proffession)
        print("SIŁA: ", hero.attrib_dict["siła"])
        print("ZWINNOŚĆ: ", hero.attrib_dict["zwinność"])
        print("PERCEPCJA: ", hero.attrib_dict["percepcja"])
        print("INTELIGENCJA: ", hero.attrib_dict["inteligencja"])
        print("SIŁA WOLI: ", hero.attrib_dict["siła woli"])
    elif input_char.upper() == "0":
        os.system("clear")
        print("\nNa pewno? Wciśnij jeszcze raz '0' żeby wyjść z gry, coś innego żeby kontynuować.")
        input_char = getch()
        if input_char.upper() == "0":
            # Game end and hall of fame enlist.
            hall_of_fame(hero, start_time)
        else:
            os.system("clear")
            print("\n" * 10)
            movement(hero, start_time, board)
    else:
        os.system("clear")
        print("\n" * 10)
        movement(hero, start_time, board)

################## mod_hero.hero_life_regeneration(hero) - na koniec pętli.

def main():
    # Hero class import to main:
    hero = mod_hero.hero_settings()
    hero.attack = mod_hero.attack_points_calc(hero=hero)
    hero.defend = mod_hero.defend_points_calc(hero=hero)
    mod_hero.combat_attribute_default(hero=hero)
    hero.max_armour = mod_hero.amour_max_calc(hero=hero)
    # After import:
    developers()
    title_screen()
    plot()
    starting_atributes = character_choice_screen(hero)
    controls()
    start_time = datetime.datetime.now()
    hero.name = input("\x1b[6;30;44m" + "\n\n\nJak Cię zwą?: " + "\x1b[0m")
    os.system("clear")
    set_map(starting_atributes, start_time, "Nawiedzone_zamczysko.txt")

main()

