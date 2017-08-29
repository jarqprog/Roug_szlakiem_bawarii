# Szlakiem Bawarii - plik roboczy Jarka
import os, time, random  
#from msvcrt import getch

# custom modules:
from mod_varied_info import display_varied_info
import mod_enemy
from mod_enemy import enemy_settings
import mod_hero 
from mod_hero import hero_settings, exp_nextlvl, display_exp, display_life, display_gold, display_location, display_damage
import mod_items
from mod_items import items_settings

os.system('cls' if os.name == 'nt' else 'clear')

def intro():
    """display title, player choose between new game / load game / credits / HOF"""
    intro_choice = ''
    while True:
        clear_screen() # to zamienimy funkcją systemową (na razie nie działa pod windowsem, więc zostawiam tak..)
        # to poniżej proponuję zrobić funkcją, by z pliku tekstowego pobierał ten tekst:
        print(u"\n"*2,"***Szkakiem Bawarii***") # tu powinna być załadowana grafika strony tytułowej
        print(u"\n"*5,"""
        wciśnij:\n
        \t"n" by stworzyć nową grę
        \t"w" by wczytać grę zapisaną grę
        \t"a" by wyświetlić informację o autorach
        \t"g" by zobaczyć Galerię sław
        \t"k" by kontynuować.. 
        """)
        intro_choice = input("...")
        print(intro_choice)
        if intro_choice == "N" or intro_choice == "n":
            hero_creation()
            break
        elif intro_choice == "W" or intro_choice == "w":
            load_game()
            break
        elif intro_choice == "A" or intro_choice == "a":
            credits_display()
            break
        elif intro_choice == "G" or intro_choice == "g":
            hof_display()
            break
        elif intro_choice == "K" or intro_choice == "k": #tymczasowo, do testów
            break

######################### funkcje do zrobienia:
def hero_creation():
    clear_screen()
    print("tworzenie bohatera - do zrobienia") # to ja bym zrobił


def load_game():
    clear_screen()
    print("wczytanie gry - do zrobienia")


def credits_display():
    clear_screen()
    print("info o autorach - do zrobienia")


def hof_display(): #ładuje z pliku tekstowego hof.txt
    clear_screen()
    print("Galeria sław (HOF) - do zrobienia")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def items_list_to_dict(items_to_add):
    '''
    transform list of items to dictionary (used to update hero's inventory dict)
    '''
    items_dict = {}
    for item in items_to_add:
        if item in items_dict:
            items_dict[item] += 1
        else:
            items_dict[item] = 1
        
    return items_dict

def inventory_update(player_character, add_remove_items_dict):
    '''
    add or remove items from hero's inventory
    '''

    player_character.inventory_dict.update(add_remove_items_dict)

    temp_dict = {} # temporary inventory dict
    for item in player_character.inventory_dict:
        # if inventory key value is < 1 (empty position), remove item from inventory:
        if player_character.inventory_dict[item] > 0:
            temp_dict.update({item:player_character.inventory_dict[item]})
    
    player_character.inventory_dict = temp_dict

    return player_character.inventory_dict
    
def treasure_generator(maxloops = None, maxitem_lvl = None, item_gen = None, player_character = None):
    '''
    generates list with random items, maxloops - max number of generated items,
    maxitem_lvl = max item level (from "items Class") that is allowed (if None - filter is off)
    item_gen = allowed item genre from "items Class" (ex. "weapon", if None - filter is off)
    '''
    treasure_list = []
    if maxitem_lvl == None: maxitem_lvl = 1
    if maxloops == None: maxloops = 1
    if maxloops > 0:        
        for i in range(random.randint(1, maxloops)):
            random_level = random.randint(1, maxitem_lvl) # randomly generates item level for each loop
            generated_item = items_settings(name = None, loc = None, lvl = random_level, gen = item_gen, player_character = None)
            treasure_list.append(generated_item.name)

    else:
        random_level = random_level = random.randint(1, maxitem_lvl)
        generated_item = items_settings(name = None, loc = None, lvl = random_level, gen = item_gen, player_character = None)
        treasure_list.append(generated_item.name)

    # transform treasure list to dict:
    # then update hero's inventory:
    add_remove_items_dict = items_list_to_dict(treasure_list)
    inventory_update(player_character, add_remove_items_dict)
    display_hero_chart(player_character)

    display_looted_items(add_remove_items_dict)
    time.sleep(2) # temporary!!!!!!



def display_looted_items(add_remove_items_dict):
    '''
    displays looted/buyed items (from "add_remove_items_dict")
    '''
    total_number_of_items = 0
    print("\nDodano do torby:\n")
    for item in add_remove_items_dict:
        print(add_remove_items_dict[item],item)
        total_number_of_items += int(add_remove_items_dict[item])


def display_hero_chart(player_character):
    """display hero's chart - attributes, inventory items, wearing items"""
    clear_screen() # czyści ekran
    #################### ATTRIBUTES ############################
    # przekształca słownniki z atrybutami bohatera na listy kluczy i wartości:
    attrib_regular_key_list = list(player_character.attrib_regular_dict.keys())
    attrib_regular_value_list = list(player_character.attrib_regular_dict.values())

    #################### INVENTORY ############################
    # przekształca słownik ekwipunku bohatera na listy kluczy i wartości:
    inventory_key_list = list(player_character.inventory_dict.keys())
    inventory_value_list = list(player_character.inventory_dict.values())

    #################### ON-BODY ############################
    # przedmioty noszone na sobie
    # przekształcenie kluczy i wartości słownka w listy
    onbody_key_list = list(player_character.onbody_dict.keys())
    onbody_value_list = list(player_character.onbody_dict.values())


    #################### OTHERS: life, exp, gold, location ############################
    other_key_list = ["życie", "doświadczenie", "obrażenia", "złoto", "lokalizacja"]
    # other_value_list element from functions:
    other_value_list = [display_life(player_character),
    display_exp(player_character),
    display_damage(player_character),
    display_gold(player_character),
    display_location(player_character)
    ]

    # sprawdza najdłuższy ciąg w listach kluczy atrybutów/ekwipunku/na sobie
    # (pomoże to odpowiednio wydrukować tabelkę):
    total_number_of_items = max(len(attrib_regular_key_list),len(inventory_key_list),len(onbody_key_list),len(other_key_list))
    inventory_key_list.append("") # add to avoid error with "max" below
    inventory_value_list.append("") # add to avoid error with "max" below
    
    # sprawdza najdłuższy wyraz wśród list atrybutów/umiejętności/ekwipunku/rzeczy na sobie - tworzy zmienne użyte przy druku tabeli:
    printing_var = 3 #helps correctly print hero chart
    long_att_key = (max(len(x) for x in attrib_regular_key_list))+printing_var # longest attributes key
    long_att_val = (max(len(str(x)) for x in attrib_regular_value_list)) # longest attributes value
    long_inv_key = (max(len(x) for x in inventory_key_list))+printing_var # longest inventory key
    long_inv_val = (max(len(str(x)) for x in inventory_value_list)) # longest inventory value
    long_onbody_key = (max(len(x) for x in onbody_key_list))+printing_var # longest onbody key
    long_onbody_val = (max(len(x) for x in onbody_value_list))+printing_var # longest onbody value
    long_other_key = (max(len(x) for x in other_key_list))+printing_var # longest onbody key
    long_other_val = (max(len(x) for x in other_value_list))+printing_var # longest onbody value

    inventory_key_list.remove("") # remove - it's no longer needed
    inventory_value_list.remove("") # remove - it's no longer needed
    
    sum_longest_arg = int(long_att_key+long_att_val+long_inv_key+long_inv_val
    +long_onbody_key+long_onbody_val+long_other_key+long_other_val)
    
    # ta część kodu rysuje tabelę:
    # zmienne do nagłówka: attrib_additional_dict = ,"doświadczenie":24, "poziom doświadczenia":1, "złoto":2 }
    printing_var = 0 #helps correctly print hero chart
    h00 = player_character.name.ljust(printing_var)
    h01 = player_character.proffession.ljust(printing_var)

    printing_var = 2 #helps correctly print hero chart
    h1 = 'atrybuty:'.rjust(long_att_key+printing_var)
    printing_var = 0
    h2 = 'w torbie:'.rjust(long_att_val+long_inv_key+printing_var)
    printing_var = 1
    h3 = 'na sobie:'.rjust(long_inv_val+long_onbody_key+printing_var)
    h4 = 'pozostałe:'.rjust(long_onbody_val+long_other_key+printing_var)
    print(u'\n',h00,"-",h01,'\n')
    print(h1,h2,h3,h4)
    printing_var_head_bottom = 5 #helps correctly print hero chart
    print("-"*(sum_longest_arg+printing_var_head_bottom))

    for i in range(int(total_number_of_items)) :
        
        # printing attributes (atak, obrona...):
        try:
            int(len(attrib_regular_key_list)) >= i         
            if int(len(attrib_regular_key_list)) >= i:
                iattrib = int(i)
                attribKeyPrt = str(attrib_regular_key_list[iattrib])+':'
                attribValuePrt = str(attrib_regular_value_list[iattrib])
        except:
            attribKeyPrt = ""
            attribValuePrt = ""
        try:
            int(len(inventory_key_list)) >= i         
            if int(len(inventory_key_list)) >= i:
                iinventory = int(i)
                inventoryKeyPrt = str(inventory_key_list[iinventory])+':'
                inventoryValuePrt = str(inventory_value_list[iinventory])
        except:
            inventoryKeyPrt = ""
            inventoryValuePrt = ""
        try:
            int(len(onbody_key_list)) >= i         
            if int(len(onbody_key_list)) >= i:
                ionbody = int(i)
                onbodyKeyPrt = str(onbody_key_list[ionbody])+':'
                onbodyValuePrt = str(onbody_value_list[ionbody])
        except:
            onbodyKeyPrt = ""
            onbodyValuePrt = ""
        try:
            int(len(other_key_list)) >= i         
            if int(len(other_key_list)) >= i:
                iother = int(i)
                otherKeyPrt = str(other_key_list[ionbody])+':'
                otherValuePrt = str(other_value_list[ionbody])
        except:
            otherKeyPrt = ""
            otherValuePrt = ""
    # zmienne przeznaczone do druku poniżej, wprowadzone dla czyletności linii z 'print'
        p1 = attribKeyPrt.rjust(long_att_key)
        p2 = attribValuePrt.ljust(long_att_val)
        p3 = inventoryKeyPrt.rjust(long_inv_key)
        p4 = inventoryValuePrt.ljust(long_inv_val)
        p5 = onbodyKeyPrt.rjust(long_onbody_key)
        p6 = onbodyValuePrt.ljust(long_onbody_val)
        p7 = otherKeyPrt.rjust(long_other_key)
        p8 = otherValuePrt.ljust(long_other_val)



        # wnętrze tabeli
        print(u'',p1,p2,p3,p4,p5,p6,p7,p8)
    # stopka tabeli
    print("-"*(sum_longest_arg+printing_var_head_bottom))



def map_maker(hero_position_h, hero_position_v): # usunąłem pętlę - będzie w głównej pętli raczej - obgadamy 
    '''
    displays map + implement player_character movement
    '''

    with open('mapa.txt', 'r') as myfile:
        mapa = myfile.read()
    mapa = list(mapa)
    position_horizontal = hero_position_h
    position_vertical = hero_position_v
    lenght_of_the_map_plus_one = 61
    map_copy = mapa[:]
    map_copy[position_horizontal + position_vertical * 61] = "@"
    print("".join(map_copy))
    print("Press w, s, d or a:")
    input_char = getch()
    if input_char == b'w': 
        map_copy[position_horizontal + position_vertical * 61] = "."
        position_vertical -= 1
        map_copy[position_horizontal + position_vertical * 61] = "@"
    elif input_char == b's': 
        map_copy[position_horizontal + position_vertical * 61] = "."
        position_vertical += 1
        map_copy[position_horizontal + position_vertical * 61] = "@"
    elif input_char == b'd': 
        map_copy[position_horizontal + position_vertical * 61] = "."
        position_horizontal += 1
        map_copy[position_horizontal + position_vertical * 61] = "@"
    elif input_char == b'a': 
        map_copy[position_horizontal + position_vertical * 61] = "."
        position_horizontal -= 1
        map_copy[position_horizontal + position_vertical * 61] = "@"
    
    clear_screen()
     
    hero_coordinates_position_list = [position_horizontal, position_vertical] # hero coordinates to export to main:

    return hero_coordinates_position_list


def main():
    clear_screen()
    # ustawia nam podstawowe zmienne:
    game_lvl = 1
    add_remove_items_dict = {}

    # importuje nam Postać do głównej funkcji (w procesie tworzenie postaci lub ładowawnia gry nastapi update postaci):
    player_character = hero_settings()


################ TU URUCHAMIAMY FUNKCJE:
    #intro() # tytuł, powitanie, wybór:

    ####### ładowanie gry LUB tworzenie bohatera LUB galeria sław LUB info o nas
    ####### po każdej z tych funkcji odpalamy główną pętlę:
    '''
    roboczo wstawiam parę rzeczy dla bohatera - pomijamy na razie tworzenie bohatera lub załadowanie z save'a
    '''

    player_character.attrib_regular_dict = {"atak":30,"obrona":2, "zwinność":1, "percepcja":1, "inteligencja":1, "siła woli":2}
    player_character.attrib_additional_dict = {"życie":13, "pełne życie":30, "doświadczenie":24, "poziom doświadczenia":1,"doświadczenie":12, "pkt do następnego poziomu": 30, "złoto":2 } 
    ################## inventory_dict keep only names and values of items (without deep specyfication)
    player_character.inventory_dict = {"nóż":1,"placki":50, "resztki mapy":1} #placki będzie można sprzedać albo nakarmić głodnego (quest)
    ################################ show active items on Hero:
    player_character.onbody_dict = {u'głowa':'skórzany hełm','szyja':'','tors':'skórzany kaftan','lewa ręka':'','prawa ręka':'maczuga','palec':'','kieszeń':'sok z gumijagód'}
    ################################ przykładowy bohater (odpalenie funkcji hero_crea )
    hero_position_h, hero_position_v = 13, 1 # sets character_player start position (horisontal/vertical)


    player_character.location = 1
    player_character.level = 2
    player_character.actualLife -= 20
    player_character.actualExp += 10
    player_character.actualLife -=20
    
    display_hero_chart(player_character) #### tmp

    ###### zabawa z generowaniem przedmiotów (import do main - według nazwy lub filtrów - tak jak z wrogami :) )
    '''imported_item = items_settings(name = "hełm", loc = None, lvl = None, gen = None, player_character = None)
    print(imported_item.name,imported_item.body_list,imported_item.price)
    imported_item = items_settings(name = None, loc = None, lvl = 3, gen = None, player_character = None)
    print(imported_item.name,imported_item.body_list,imported_item.price)
    imported_item = items_settings(name = None, loc = None, lvl = 1, gen = "quest", player_character = None)
    print(imported_item.name,imported_item.body_list,imported_item.price)
    '''
    pausa = input("wpisz cokolwiek, by kontynuować, będziemy generować skarb :D")
    treasure_generator(maxloops = 20, maxitem_lvl = None, item_gen = None, player_character = player_character) # mamy mało itemów, więc filtry wyłączyłem


    display_hero_chart(player_character)


    # ----- tu będzie funkcja do wyświetlania mapy
    '''
####################### MAIN LOOP:
    while player_character.attrib_additional_dict["życie"] > 0:
        clear_screen()
        display_hero_chart(player_character)
        display_varied_info() # display short random info :)
        map_maker(hero_position_h, hero_position_v)
        hero_coordinates_position_list = map_maker(hero_position_h, hero_position_v)
        hero_position_h, hero_position_v = hero_coordinates_position_list[0] , hero_coordinates_position_list[1] # update hero's position
    '''
        








main()




