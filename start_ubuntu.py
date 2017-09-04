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

os.system('clear')


def delay_print(s):
    ''' Delays printing. '''
    for c in s:
        sys.stdout.write('%s' % c)
        sys.stdout.flush()
        time.sleep(0.004)


def developers():
    ''' Returns info about authors screen. '''
    print("Wciśnij cokolwiek!")
    delay_print("\n\n\n     Słuchacze CODECOOL'a \n\n\nJarosław Kucharczyk i Łukasz Malko\n\n\n       PRZEDSTAWIAJĄ:")
    input_char = getch()
    os.system('clear')


def title_screen():
    ''' Returns title screen '''
    delay_print("\n ___ _____      _   _  _____ ___ __  __        ___   ___      ___   ___ ___ ___ \n")
    delay_print("/ __|_  / |    /_\ | |/ /_ _| __|  \/  |      | _ ) /_\ \    / /_\ | _ \_ _|_ _|\n")
    delay_print("\__ \/ /| |__ / _ \| ' < | || _|| |\/| |      | _ \/ _ \ \/\/ / _ \|   /| | | | \n")
    delay_print("|___/___|____/_/ \_\_|\_\___|___|_|  |_|      |___/_/ \_\_/\_/_/ \_\_|_\___|___|\n")
    delay_print("\nROGUELIKE EXPERIENCE\n\n")
    print("Wciśnij cokolwiek.")
    input_char = getch()
    os.system('clear')


def plot():
    ''' Returns plot screen.'''
    delay_print("\n\n\n\n\nDawno, dawno temu w Bawarii...Twój przyjaciel, pustelnik Mullog, został okradziony.\n")
    delay_print("Karzeł Oblib zwędził mu drogocenną obrączkę - prezent urodziowy od przyjaciela z młodości.\n")
    delay_print("Mullog usycha z żalu, błaga Cię o pomoc.\n")
    delay_print("Wyruszasz zatem, a trop Obliba doprowadza Cię do 'Doliny Łotrzyków'...\n")
    print("\n\n\n\n\nWciśnij cokolwiek.")
    input_char = getch()
    os.system('cls')


def character_choice_screen(hero):
    """ Returns hero's starting atributes. """
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
                picture = myfile.read()
                print(picture)
                print("WOJOWNIK")
                print("ATRYBUTY:")
                print("SIŁA : 5, ZWINNOŚĆ : 2, PERCEPCJA: 1, INTELIGENCJA : 1, SIŁA WOLI : 2")
                print("Wciśnij 'y' żeby wybrac tego bohatera, wciśnij coś innego żeby wrócić")
                input_char = getch()
                if input_char.upper() == 'Y':
                    os.system('clear')
                    warrior_attr_dict = {"siła": 5, "zwinność": 2, "percepcja": 1, "inteligencja": 1, "siła woli": 2}
                    hero.attrib_dict.update(warrior_attr_dict)
                    hero.proffession = "Wojownik"
                    return hero
        if input_char.upper() == '2':
            os.system('clear')
            with open('2. ŁOWCA.txt', 'r') as myfile:
                picture = myfile.read()
                print(picture)
                print("ŁOWCA")
                print("ATRYBUTY:")
                print("SIŁA : 2, ZWINNOŚĆ : 3, PERCEPCJA: 3, INTELIGENCJA : 1, SIŁA WOLI : 2")
                print("Wciśnij 'y' żeby wybrac tego bohatera, wciśnij coś innego żeby wrócić")
                input_char = getch()
                if input_char.upper() == 'Y':
                    os.system('clear')
                    hunter_attr_dict = {"siła": 2, "zwinność": 3, "percepcja": 3, "inteligencja": 3, "siła woli": 2}
                    hero.attrib_dict.update(hunter_attr_dict)
                    hero.proffession = "Łowca"
                    return hero
        if input_char.upper() == '3':
            os.system('clear')
            with open('3. NINJA.txt', 'r') as myfile:
                picture = myfile.read()
                print(picture)
                print("NINJA")
                print("ATRYBUTY:")
                print("SIŁA : 1, ZWINNOŚĆ : 3, PERCEPCJA: 3, INTELIGENCJA : 3, SIŁA WOLI : 1")
                print("Wciśnij 'y' żeby wybrac tego bohatera, wciśnij coś innego żeby wrócić")
                input_char = getch()
                if input_char.upper() == 'Y':
                    os.system('clear')
                    ninja_attr_dict = {"siła": 1, "zwinność": 3, "percepcja": 3, "inteligencja": 3, "siła woli": 1}
                    hero.attrib_dict.update(ninja_attr_dict)
                    hero.proffession = "Ninja"
                    return hero
        if input_char.upper() == '4':
            os.system('clear')
            with open('4. STWORZONA POSTAĆ.txt', 'r') as myfile:
                picture = myfile.read()
                print(picture)
                print("NIEZNAJOMY")
                print("\nATRYBUTY:")
                print("\nSIŁA : 1, ZWINNOŚĆ : 1, PERCEPCJA: 1, INTELIGENCJA : 1, SIŁA WOLI : 1\n\n\n")
                print("To ekran tworzenia postaci.")
                print("Wciśnij 'y' żeby stworzyć swoją postać, wciśnij coś innego żeby wrócić.")
                input_char = getch()
                if input_char.upper() == 'Y':
                    os.system('clear')
                    strenght = 1
                    agility = 1
                    cognition = 1
                    brainpower = 1
                    willpower = 1
                    points = 6
                    while True:
                        os.system('clear')
                        if points == 0:
                            break
                        else:
                            print("\n\nSIŁA", strenght, "ZWINNOŚĆ", agility, "PERCEPCJA", cognition)
                            print("INTELIGENCJA", brainpower, "SIŁA WOLI", willpower)
                            print("Masz", points, "punktów atrybutów do rozdysponowania.")
                            print("Wciśnij 's', 'z', 'p', 'i', 'w' żeby dodać punkt do atrybutu")
                            print("kolejno: siły, zwinności, percepcji, inteligencji, siły woli.")
                            input_char = getch()
                            if input_char.upper() == 'S':
                                strenght += 1
                                points -= 1
                                continue
                            if input_char.upper() == 'Z':
                                agility += 1
                                points -= 1
                                continue
                            if input_char.upper() == 'P':
                                cognition += 1
                                points -= 1
                                continue
                            if input_char.upper() == 'I':
                                brainpower += 1
                                points -= 1
                                continue
                            if input_char.upper() == 'W':
                                willpower += 1
                                points -= 1
                                continue
                            else:
                                continue
                    print("\n\nSIŁA", strenght, "ZWINNOŚĆ", agility, "PERCEPCJA", cognition)
                    print("INTELIGENCJA", brainpower, "SIŁA WOLI", willpower)
                    klasa = input("Klasa postaci w której czujesz się najlepiej to: ")
                    klasa = klasa.upper()
                    print("Wybrałeś swoje przeznaczenie. Wciśnij cokolwiek, żeby rozpocząc gre.")
                    input_char = getch()
                    os.system('clear')
                    created_attr_dict = {"siła": strenght, "zwinność": agility, "percepcja": cognition,
                                         "inteligencja": brainpower, "siła woli": willpower}
                    hero.attrib_dict.update(created_attr_dict)
                    hero.proffession = "Cień"
                    return hero
        else:
            continue


def getch():
    ''' Returns input without 'enter'. '''
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
    ''' Returns controls screen. '''
    print("\n\nHOW-TO-PLAY-SCREEN\nPORUSZASZ SIĘ PO MAPIE UZYWAJĄC W, S, A, D\nZaawansowane sterowanie jest pod mapką.")
    print("Wciśnij cokolwiek.")
    input_char = getch()
    os.system('clear')


def hot_warm_cold():
    ''' Hot warm cold mini-game. '''
    os.system('clear')
    correct_answer = []
    string.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    random_number = random.choice(range(9))
    random_letter1 = random.choice(string.letters)
    random_letter2 = random.choice(string.letters)
    random_letter3 = random.choice(string.letters)
    choices_for_sequence = [str(random_number), random_letter1, random_letter2, random_letter3]
    for e in range(3):
        i = random.choice(choices_for_sequence)
        choices_for_sequence.remove(i)
        correct_answer.append(i)
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
    print("\nPomyślałem o 3 elementowym miksie cyfr i liter. Zgadnij!")
    print("Pamietaj:")
    print("Jak mówie", " " * 5, "to znaczy, że:\n")
    print("Zimno", " " * 9, "nie zgadłeś")
    print("Ciepło", " " * 8, "zgadłeś ale w złych pozycjach")
    print("Gorąco", " " * 8, "co najmniej jeden element jest dobrze i w dobrej pozycji.")
    for i in range(difficulty_choice):
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
    return 0


def game_events(position, hero):
    """ Returns event. """
    # ENEMY CLASS IMPORT TO MAIN:
    enemy = mod_enemy.enemy_settings(name=None, loc=None, lvl=None, gen=None)
    enemy.attack = mod_enemy.attack_points_calc(enemy=enemy)
    enemy.defend = mod_enemy.defend_points_calc(enemy=enemy)
    enemy.combat_attribute = mod_enemy.combat_attribute_default(enemy=enemy)
    if position == "N":
        print("\n" * 7)
        print("Zbliza się do Ciebie dziadek NPC i zaczyna radzić:")
        print("'-Na Twoim miejscu udałbym się do wioski na północ, może znajdziec tam pomocna informację, na razie.'")
        print("Dziadek NPC zostaje w pobliżu na wszelki wypadek gdyby musiał tobie powtórzyć co powiedział.")
    elif position == "W":
        print("\n" * 9)
        print("Trafiłeś do wioski Szwarzwald")
    elif position == "C":
        print("\n" * 6)
        delay_print("Spotykasz troglodyte Mariana. To może oznaczać tylko jedno:\n")
        delay_print("Czas na gre hot and cold. ")
        delay_print("Nacisnij cokolwiek, żeby zacząć.")
        input_char = getch()
        difficulty_choice = hot_warm_cold()
        os.system('cls')
        print("\n" * 10)
        return difficulty_choice
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
        mod_event.event_fight(enemy=mod_enemy.enemy_settings(name=None, loc=hero.location, lvl=None, gen=None),
                              hero=hero)
        os.system('clear')
        print("\n" * 10)
    else:
        print("\n" * 9)
        print("Nie mozesz sie tu ruszyc")


def core(hero, start_time):
    """ Major loop of the whole game. """
    # General comment - lines above the map always = 10.
    event_result = None
    # Initiate non-empty variable for upper() compatibility.
    input_char = "0"
    print("\n" * 10)
    with open('mapa_forest.txt', 'r') as myfile:
        board = myfile.read()
    board = list(board)
    position_horizontal = 1
    position_vertical = 18
    lenght_of_the_map_plus_one = 81
    map_copy = board[:]
    map_copy[position_horizontal + position_vertical * 81] = ('\x1b[6;30;42m' + "@" + '\x1b[0m')
    while True:
        if input_char.upper() in [b'W', b'S', b'D', b'A']:
            # Event_results for:
            #           1. Hot_and_cold mini-game.
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
        print("".join(map_copy))
        print("\nWciśnij W, S, A, D - poruszanie się, 'e' - karta bohatera, 'z' - dziennik, 'p' - pomoc, ")
        print("'g' - zapis gry, 'l' - legenda, 'k' - atrybuty lub '0' - wyjście z gry.")
        print("\n ___ _____      _   _  _____ ___ __  __        ___   ___      ___   ___ ___ ___ ")
        print("/ __|_  / |    /_\ | |/ /_ _| __|  \/  |      | _ ) /_\ \    / /_\ | _ \_ _|_ _|")
        print("\__ \/ /| |__ / _ \| ' < | || _|| |\/| |      | _ \/ _ \ \/\/ / _ \|   /| | | | ")
        print("|___/___|____/_/ \_\_|\_\___|___|_|  |_|      |___/_/ \_\_/\_/_/ \_\_|_\___|___|")
        input_char = getch()
        if input_char.upper() == 'W':
            os.system('clear')
            if map_copy[position_horizontal + (position_vertical - 1) * 81] != ".":
                event_result = game_events(map_copy[position_horizontal + (position_vertical - 1) * 81], hero)
            else:
                print("\n" * 10)
                map_copy[position_horizontal + position_vertical * 81] = "."
                position_vertical -= 1
                map_copy[position_horizontal + position_vertical * 81] = ('\x1b[6;30;42m' + "@" + '\x1b[0m')
        elif input_char.upper() == 'S':
            os.system('clear')
            if map_copy[position_horizontal + (position_vertical + 1) * 81] != ".":
                event_result = game_events(map_copy[position_horizontal + (position_vertical + 1) * 81], hero)
            else:
                print("\n" * 10)
                map_copy[position_horizontal + position_vertical * 81] = "."
                position_vertical += 1
                map_copy[position_horizontal + position_vertical * 81] = ('\x1b[6;30;42m' + "@" + '\x1b[0m')
        elif input_char.upper() == 'D':
            os.system('clear')
            if map_copy[(position_horizontal + 1) + position_vertical * 81] != ".":
                event_result = game_events(map_copy[(position_horizontal + 1) + position_vertical * 81], hero)
            else:
                print("\n" * 10)
                map_copy[position_horizontal + position_vertical * 81] = "."
                position_horizontal += 1
                map_copy[position_horizontal + position_vertical * 81] = ('\x1b[6;30;42m' + "@" + '\x1b[0m')
        elif input_char.upper() == 'A':
            os.system('clear')
            if map_copy[(position_horizontal - 1) + position_vertical * 81] != ".":
                event_result = game_events(map_copy[(position_horizontal - 1) + position_vertical * 81], hero)
            else:
                print("\n" * 10)
                map_copy[position_horizontal + position_vertical * 81] = "."
                position_horizontal -= 1
                map_copy[position_horizontal + position_vertical * 81] = ('\x1b[6;30;42m' + "@" + '\x1b[0m')
        # Hero's actions different than WSAD movement.
        elif input_char.upper() == b'E':
            mod_display.display_hero_chart(hero=hero)
            print("\n\n\n\nWcisnij cokolwiek żeby wyjść.")
            input_char = getch()
            os.system('clear')
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
            print("C = Zimno/ ciepła niespodzianka Mariana. Spotkania z nim prowadzą do zmian w percepcji.")
        elif input_char.upper() == 'K':
            os.system('clear')
            print("\n" * 4)
            print("KLASA: ", hero.proffession)
            print("SIŁA: ", hero.attrib_dict["siła"])
            print("ZWINNOŚĆ: ", hero.attrib_dict["zwinność"])
            print("PERCEPCJA: ", hero.attrib_dict["percepcja"])
            print("INTELIGENCJA: ", hero.attrib_dict["inteligencja"])
            print("SIŁA WOLI: ", hero.attrib_dict["siła woli"])
        elif input_char.upper() == '0':
            # Game end and hall of fame enlist.
            os.system('clear')
            print("\nNa pewno? Wciśnij jeszcze raz '0' żeby wyjść z gry, coś innego żeby kontynuować.")
            input_char = getch()
            if input_char.upper() == '0':
                os.system('clear')
                finish_time = datetime.datetime.now()
                # Get rid of microseconds.
                game_time = (str(finish_time - start_time)).split(".")[0]
                # Sum up atributes.
                sum_of_atributes = 0
                for value in hero.attrib_dict.values():
                    try:
                        sum_of_atributes += int(value)
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
                print("\nCZAS GRY: ", game_time, "\nSUMA ATRYBUTÓW: ", sum_of_atributes)
                # Add final results to Hall of Fame.
                with open("HALL_OF_FAME.txt", "a", encoding='utf-8') as HALL_OF_FAME:
                    user_score = [str(sum_of_atributes), str(user_name), str(game_time),
                                  str(hero.profession)]
                    user_score = "        ".join(user_score)
                    HALL_OF_FAME.write(str(user_score) + "\n")
                    print("\n\nNacisnij cokolwiek")
                    input_char = getch()
                with open("HALL_OF_FAME.txt", "r", encoding='utf-8') as HALL_OF_FAME:
                    os.system('clear')
                    print("\nHALL_OF_FAME:\n")
                    # Use '/t' to fit the results.
                    print(" " * 3,  "PUNKTY", " " * 2, "GRACZ", " " * 21, "CZAS", " " * 9, "KLASA\n")
                    HALL_OF_FAME = sorted(HALL_OF_FAME.readlines(), reverse=True)
                    list_place = 1
                    for i in HALL_OF_FAME:
                        print(list_place, ".", "".join(i))
                        list_place += 1
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
    hero.name = input("\n\n\nJak Cię zwą?: ")
    os.system('clear')
    core(starting_atributes, start_time)

main()

