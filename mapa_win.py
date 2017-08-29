import os
from msvcrt import getch
os.system('cls')
# Zawsze odstep 10 wierszy !!!
print("\n" * 10)
with open('mapa_wulkan.txt', 'r') as myfile:
    mapa = myfile.read()
mapa = list(mapa)
position_horizontal = 1
position_vertical = 18
lenght_of_the_map_plus_one = 81
map_copy = mapa[:]
map_copy[position_horizontal + position_vertical * 81] = "@"
while True:
    print("".join(map_copy))
    print("Press w, s, d or a to move, e for inventory, z for journal, p for help, g to save game, l to quit:") 
    print("\n/ __||_  /| |     /_\  | |/ /|_ _|| __||  \/  | | _ )  /_\\ \    / //_\  | _ \|_ _||_ _|")
    print("\__ \ / / | |__  / _ \ | ' <  | | | _| | |\/| | | _ \ / _ \\ \/\/ // _ \ |   / | |  | |")
    print("|___//___||____|/_/ \_\|_|\_\|___||___||_|  |_| |___//_/ \_\\_/\_//_/ \_\|_|_\|___||___|")                                                                                      
    input_char = getch()
    if input_char == b'w':
        os.system('cls') 
        if map_copy[position_horizontal + (position_vertical - 1) * 81] != ".":
            print("\n" * 9)
            print("Nie mozesz sie tu ruszyc")
        else:
            print("\n" * 10)
            map_copy[position_horizontal + position_vertical * 81] = "."
            position_vertical -= 1
            map_copy[position_horizontal + position_vertical * 81] = "@"
    elif input_char == b's':
        os.system('cls')
        if map_copy[position_horizontal + (position_vertical + 1) * 81] != ".":
            print("\n" * 9)
            print("Nie mozesz sie tu ruszyc")
        else:
            print("\n" * 10)
            map_copy[position_horizontal + position_vertical * 81] = "."
            position_vertical += 1
            map_copy[position_horizontal + position_vertical * 81] = "@"
    elif input_char == b'd':
        os.system('cls')
        if map_copy[(position_horizontal + 1) + position_vertical * 81] != ".":
            print("\n" * 9)
            print("Nie mozesz sie tu ruszyc")
        else:
            print("\n" * 10)
            map_copy[position_horizontal + position_vertical * 81] = "."
            position_horizontal += 1
            map_copy[position_horizontal + position_vertical * 81] = "@"
    elif input_char == b'a':
        os.system('cls')
        if map_copy[(position_horizontal - 1) + position_vertical * 81] != ".":
            print("\n" * 9)
            print("Nie mozesz sie tu ruszyc")
        else:
            print("\n" * 10)
            map_copy[position_horizontal + position_vertical * 81] = "."
            position_horizontal -= 1
            map_copy[position_horizontal + position_vertical * 81] = "@"
    elif input_char == b'e':
        os.system('cls')
        print("\n" * 9)
        print("Tu powinien być ekwipunek")
    elif input_char == b'z':
        os.system('cls')
        print("\n" * 9)
        print("Tu powinien być dziennik")
    elif input_char == b'p':
        os.system('cls')
        print("\n" * 9)
        print("Tu powinien być pomoc")
    elif input_char == b'g':
        os.system('cls')
        print("\n" * 9)
        print("Tu powinien być zapis gry")
    elif input_char == b'l':
        os.system('cls')
        break
    else:
        continue

