# mod_varied_info - custom mod, contains list of short messages to random display in main:

import os, math
import random, time
import mod_hero 
import mod_enemy


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def dot_loop():
    '''
    display animated dot ('.'): . -> .. -> ... 
    '''

    for i in ('...'):        
        print(i, end='', flush=True)
        time.sleep(.2)

def pause():
    '''
    stop game action (for ex. in the middle of fight)
    '''
    pause = 0 # reset pause variable
    pause = input("\n\nWciśnij <enter>, żeby kontynuować...\n\n") # temporary - we need here glitch
    if pause == str("q") and ("Q"): exit()

def display_varied_info():
    '''
    function with a list of short messages (mainly to increse playability). It random generates message to display from list:
    '''
    info_to_display_list = [
    "Zapowiada się piękny dzień", "Zbiera się na burzę", "Noc była chłodna, ale poranek słoneczny i ciepły",
    "Mam przeczucie, że coś się wydarzy",
    "Jest bezpiecznie",



    "Porada: sklep na mapce oznaczony jest literką 'S'", "Porada: symbol '?' oznacza zagadkowe zdarzenie - kto wie, co to może być?"

    ]


    info_to_display = info_to_display_list[random.randint(0, len(info_to_display_list)-1)]

    return print(info_to_display, end=''), dot_loop()


def display_hero_chart(hero = None):
    """display hero's chart - attributes, inventory items, wearing items"""
    clear_screen() # czyści ekran
    #################### ATTRIBUTES ############################
    # przekształca słownniki z atrybutami bohatera na listy kluczy i wartości:
    attrib_regular_key_list = list(hero.attrib_dict.keys())
    attrib_regular_value_list = list(hero.attrib_dict.values())

    #################### INVENTORY ############################
    # przekształca słownik ekwipunku bohatera na listy kluczy i wartości:
    inventory_key_list = list(hero.inventory_dict.keys())
    inventory_value_list = list(hero.inventory_dict.values())

    #################### ON-BODY ############################
    # przedmioty noszone na sobie
    # przekształcenie kluczy i wartości słownka w listy
    onbody_key_list = list(hero.onbody_dict.keys())
    onbody_value_list = list(hero.onbody_dict.values())


    #################### OTHERS: life, exp, gold, location ############################
    other_key_list = ["życie", "doświadczenie", "złoto", "lokalizacja", "atak", "obrona", "obrażenia", "pancerz" ]
    # other_value_list element from functions:
    other_value_list = [mod_hero.display_life(hero = hero),
    mod_hero.display_exp(hero = hero),
    mod_hero.display_gold(hero = hero),
    mod_hero.display_location(hero = hero),
    str(hero.attack),
    str(hero.defend),
    mod_hero.display_damage(hero = hero),
    mod_hero.display_armour(hero = hero)
    ]

    # sprawdza najdłuższy ciąg w listach kluczy atrybutów/ekwipunku/na sobie
    # (pomoże to odpowiednio wydrukować tabelkę):
    total_number_of_items = max(len(attrib_regular_key_list),len(inventory_key_list),len(onbody_key_list),len(other_key_list))
    inventory_key_list.append("") # add to avoid error with "max" below
    inventory_value_list.append("") # add to avoid error with "max" below
    
    # sprawdza najdłuższy wyraz wśród list atrybutów/umiejętności/ekwipunku/rzeczy na sobie - tworzy zmienne użyte przy druku tabeli:
    printing_var = 10 #helps correctly print hero chart
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
    h00 = hero.name.ljust(printing_var)
    h01 = hero.proffession.ljust(printing_var)

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
        
        # printing attributes (siła, zwinność...):
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

def display_enemy_vs_hero(enemy = None, hero = None, attacker = None):
    '''
    display basic info about enemy compared to hero's stats 
    '''
    clear_screen()
    mod_enemy.enemy_info(enemy = enemy)
    # check what is main enemy attribut in combat
    enemy.combat_attribute = mod_enemy.combat_attribute_default(enemy = enemy)

    enemy_dmg = "".join([str(enemy.dmg_list[0]),"-", str(enemy.dmg_list[1])]) # used below in enemy_to_display_list
    printing_var = 2 # variable that helps in printing (used below)
    # check max lenght of hero name and enemy name (which of them is longer) - used below in printing:
    longest_name_lenght = max(len(str(x)) for x in (hero.name,enemy.name))
    # make list of attributes names to print in table's head (siła, zwinność, percepcja...):
    head_to_display_list1 = [""]+list(hero.attrib_dict.keys())
    # make list of hero attributes values to print:
    hero_to_display_list1 = [hero.name+':']+list(hero.attrib_dict.values())
    # make list of enemy attributes values to print:
    enem_to_display_list1 = [enemy.name+':']+list(enemy.attrib_dict.values())
    # make list of other attributes names to print in table's head (życie, obrażenia, atak..)
    head_to_display_list2 = ["", "życie", "obrażenia", "atak", "obrona", "gł. cecha"]
    # make list of hero attributes values to print:
    hero_to_display_list2 = [hero.name+':', str(hero.actualLife), str(mod_hero.display_damage(hero = hero))]+list([str(hero.attack), str(hero.defend), str(hero.combat_attribute)])
    # make list of enemy attributes values to print:
    enem_to_display_list2 = [enemy.name+':', enemy.actualLife, enemy_dmg]+list([str(enemy.attack), str(enemy.defend), str(enemy.combat_attribute)])
    # search for the longest element in each lists (needed to print nice table with stats):

    long_head = max(len(str(x)) for x in head_to_display_list1)+printing_var
    long_hero = max(len(str(x)) for x in hero_to_display_list1)+printing_var
    long_enem = max(len(str(x)) for x in enem_to_display_list1)+printing_var
    # search for longest of the longest elements in lists:
    longest_arg = max(list((int(x)) for x in (long_head,long_hero,long_enem)))

    # attacker is first to display:
    if attacker == hero:
        defender = enemy
        attacker_list1 = hero_to_display_list1
        defender_list1 = enem_to_display_list1
        attacker_list2 = hero_to_display_list2
        defender_list2 = enem_to_display_list2
    else: 
        defender = hero
        attacker_list1 = enem_to_display_list1
        defender_list1 = hero_to_display_list1
        attacker_list2 = enem_to_display_list2
        defender_list2 = hero_to_display_list2


    # for ex.:
    # display_enemy(enemy = enemy_settings(name = None, loc = hero.location, lvl = None, gen = None))

    # prints info about enemy and hero/enemy stats:
    print("\nstatystki:".rjust(longest_arg))
    for i in range(len(head_to_display_list1)): print(str(head_to_display_list1[int(i)]).rjust(longest_arg)," ", sep='', end='', flush=True)
    print("\r")
    for i in range(len(head_to_display_list1)): print(str(hero_to_display_list1[int(i)]).rjust(longest_arg)," ", sep='', end='', flush=True)
    print("\r")
    for i in range(len(head_to_display_list1)): print(str(enem_to_display_list1[int(i)]).rjust(longest_arg)," ", sep='', end='', flush=True)
    print('\n')
    for i in range(len(head_to_display_list2)): print(str(head_to_display_list2[int(i)]).rjust(longest_arg)," ", sep='', end='', flush=True)
    print("\r")
    for i in range(len(head_to_display_list2)): print(str(hero_to_display_list2[int(i)]).rjust(longest_arg)," ", sep='', end='', flush=True)
    print("\r")
    for i in range(len(head_to_display_list2)): print(str(enem_to_display_list2[int(i)]).rjust(longest_arg)," ", sep='', end='', flush=True)
    print("\n\n")

def calendar(hero = None):
    '''
    display short info about day, day time using turn counter
    '''
    turn_counter = mod_hero.calendar(hero = hero)

    week_list = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"]
    day_time_list = ["poranek", "południe", "popołudniu", "wieczór"]
    day = math.floor(turn_counter/4)
    
    #4 # for four day times (morning, noon...)
    if turn_counter % 4 == 0:
        day_time = day_time_list[3]
    elif turn_counter % 3 == 0:
        day_time = day_time_list[2]
    elif turn_counter % 2 == 0:
        day_time = day_time_list[1]
    else:
        day_time = day_time_list[0]
    
    return print("Dzień", str(day)+",", day_time+", jesteś w krainie:", mod_hero.display_location(hero = hero)+".")

    



def credits_display():
    clear_screen()

    print('''
    
    SZLAKIEM BAWARII

    Autorzy:

    Łukasz Malko
    Jarosław Kucharczyk

    
    ''')

    pause()



def hof_display(): #ładuje z pliku tekstowego hof.txt
    clear_screen()
    print("Galeria sław (HOF) - do zrobienia")




def game_over(hero = None): # todo!!!!!!!!!!!!!!!!!!
    
    print("game over")
    pause()



def display_looted_items(add_remove_items_dict):
    '''
    displays looted/buyed items (from "add_remove_items_dict")
    '''
    total_number_of_items = 0
    print("\nDodano do torby:\n")
    for item in add_remove_items_dict:
        print(item,": ", add_remove_items_dict[item],"; ", sep='', end='', flush=True) #prints in line (place economy)
        total_number_of_items += int(add_remove_items_dict[item])
    pause()

