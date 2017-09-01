# Szlakiem Bawarii - plik roboczy Jarka
#!/usr/bin/python3
import os, time, random, math
#from msvcrt import getch

# custom modules:
from mod_varied_info import display_varied_info
import mod_enemy
from mod_enemy import enemy_settings, attack_points_calc, defend_points_calc

import mod_hero 
from mod_hero import hero_settings, exp_nextlvl, display_exp, display_life, display_gold, display_location, display_damage
from mod_hero import attack_points_calc, defend_points_calc

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
    pause = input("\n\nWciśnij <enter>, żeby kontynuować...\n\n") # temporary - we need here glitch
    if pause == str("q") and ("Q"): exit()


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

def inventory_update(hero, add_remove_items_dict):
    '''
    add or remove items from hero's inventory
    '''

    hero.inventory_dict.update(add_remove_items_dict)

    temp_dict = {} # temporary inventory dict
    for item in hero.inventory_dict:
        # if inventory key value is < 1 (empty position), remove item from inventory:
        if hero.inventory_dict[item] > 0:
            temp_dict.update({item:hero.inventory_dict[item]})
    
    hero.inventory_dict = temp_dict

    return hero.inventory_dict
    
def treasure_generator(maxloops = None, maxitem_lvl = None, item_gen = None, hero = None):
    '''
    generates list with random items, maxloops - max number of generated items,
    maxitem_lvl = max item level (from "items Class") that is allowed (if None - filter is off)
    item_gen = allowed item genre from "items Class" (ex. "weapon", if None - filter is off)
    '''
    if maxloops != 0:
    
        treasure_list = []
        if maxitem_lvl == None: maxitem_lvl = 1
        if maxloops == None: maxloops = 1
        if maxloops > 0:        
            for i in range(random.randint(1, maxloops)):
                random_level = random.randint(1, maxitem_lvl) # randomly generates item level for each loop
                generated_item = items_settings(name = None, loc = None, lvl = random_level, gen = item_gen, hero = None)
                treasure_list.append(generated_item.name)
        
        # transform treasure list to dict:
        # then update hero's inventory:
        add_remove_items_dict = items_list_to_dict(treasure_list)
        inventory_update(hero, add_remove_items_dict)
        display_hero_chart(hero = hero)

        display_looted_items(add_remove_items_dict)
        time.sleep(0.3) # temporary!!!!!!



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


    ########################## Battle functions:
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
    hero_to_display_list2 = [hero.name+':', str(hero.actualLife), str(display_damage(hero = hero))]+list([str(hero.attack), str(hero.defend), str(hero.combat_attribute)])
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
    for i in range(len(head_to_display_list1)): print(str(attacker_list1[int(i)]).rjust(longest_arg)," ", sep='', end='', flush=True)
    print("\r")
    for i in range(len(head_to_display_list1)): print(str(defender_list1[int(i)]).rjust(longest_arg)," ", sep='', end='', flush=True)
    print('\n')
    for i in range(len(head_to_display_list2)): print(str(head_to_display_list2[int(i)]).rjust(longest_arg)," ", sep='', end='', flush=True)
    print("\r")
    for i in range(len(head_to_display_list2)): print(str(attacker_list2[int(i)]).rjust(longest_arg)," ", sep='', end='', flush=True)
    print("\r")
    for i in range(len(head_to_display_list2)): print(str(defender_list2[int(i)]).rjust(longest_arg)," ", sep='', end='', flush=True)
    print("\n\n")

    return attacker


def priority_test(enemy = None, hero = None):
    '''
    who's attacker, who's defender
    '''
    display_enemy_vs_hero(enemy = enemy, hero = hero, attacker = None)
    # zwinność, percepcja i inteligencja have influence on this test:
    hero_test_stats = (int(hero.attrib_dict["zwinność"])+int(hero.attrib_dict["percepcja"])+
    int(hero.attrib_dict["inteligencja"]))
    enem_test_stats = (int(enemy.attrib_dict["zwinność"])+int(enemy.attrib_dict["percepcja"])+int(enemy.attrib_dict["inteligencja"]))
    print("Kto uzyskał inicjatywę? (test inicjatywy)\n")
    while True:
        test_var1 = hero_test_stats + enem_test_stats
        test_var2 = random.randint(1,test_var1)      
        print('\r\r'+hero.name+":", hero_test_stats)
        print('\r\r'+enemy.name+":", test_var2)
        if hero_test_stats > test_var2:
            print("\nRezultat:", end=''), dot_loop()
            print("\n\natakuje",hero.name+'!')
            attacker = hero
            break
          
        elif hero_test_stats < test_var2:
            print("\nRezultat:", end=''), dot_loop()
            print("\n\natakuje",enemy.name+'!')
            attacker = enemy
            break

    pause()

    return attacker


def game_over(hero = None): # todo!!!!!!!!!!!!!!!!!!
    
    print("game over")

def rip(enemy = None, hero = None):
    print("Po heroicznej walce świat zapłakał,", enemy.name, "zabił bohatera o imieniu", hero.name+". RIP,", hero.name+"!")
    display_hero_chart(hero = hero)
    pause()
    game_over(hero = hero) 

def win_fight(enemy = None, hero = None):
    print(hero.name,"Zwycięstwo!")
    if len(enemy.treasure_dict) > 0: # check if there are some treasures in enemy inventory
        add_remove_items_dict = enemy.treasure_dict
        display_looted_items(add_remove_items_dict) # display treasures from enemy inventory
        inventory_update(hero, add_remove_items_dict)
    pause()
    print("Może coś jeszcze?", end=''), dot_loop()

    # and some random generated items:
    treasure_generator(maxloops = enemy.maxdrop, maxitem_lvl = enemy.maxdrop_lvl, item_gen = None, hero = hero)
    display_hero_chart(hero=hero)
    pause()

def counterattack(enemy = None, hero = None, attacker = None, attack = None):
    '''
    part of the fight mechanic (part of fight function) 
    '''
    display_enemy_vs_hero(enemy = enemy, hero = hero, attacker = attacker)
    #attacker = priority_test(enemy = enemy, hero = hero) 
    # define attacker and defender:
    if attacker == hero: defender = enemy
    elif attacker == enemy: defender = hero

    print("\nkontratak!", end='')
    dot_loop()
    counterattack_result = 0
    print('\n'+defender.name, " kontratakuje: rzuca",str(defender.attrib_dict[str(defender.combat_attribute)]),"razy kością K4:")
    damage = random.randint(defender.dmg_list[0], defender.dmg_list[1])
    for i in range(int(defender.attrib_dict[str(defender.combat_attribute)])):
        counterattack_var = random.randint(1,4)
        print((str(counterattack_var)),"      ", sep='', end='', flush=True), time.sleep(0.3)
        counterattack_result += counterattack_var
    print("\n\nRezultat:", end=''), dot_loop()
    print('\n\n'+defender.name+':',counterattack_result,'+',defender.attack,"(atak):", counterattack_result+defender.attack)
    print(attacker.name+':', attack), time.sleep(0.3)
    if attack < counterattack_result+defender.attack:
        attacker.actualLife -= damage
        print(defender.name, "zadał obrażenia:", attacker.name, "stracił", damage, "pkt. życia")
        time.sleep(0.3)
        if defender == hero:
            hero.actualExp += damage
            print(hero.name+", zdobyto doświadczenie:", damage)
            
            return hero.actualExp


        if defender.actualLife < 0:
            defender.actualLife = 0
            combat_end = 1
            return combat_end


    else:
        print('\n'+attacker.name, "obronił się!")
        attacker_change = 1
        return attacker_change
            
            

def fight(enemy = None, hero = None, attacker = None):
    '''
    fight mechanic = hit
    '''

    # define attacker and defender:
    if attacker == hero: defender = enemy
    elif attacker == enemy: defender = hero 

    attacker_change = 0

    attack_result = 0
    defend_result = 0
    print(attacker.name, "atakuje: rzuca",attacker.attrib_dict[str(attacker.combat_attribute)],"razy kością K4:")
    for i in range(int(attacker.attrib_dict[str(attacker.combat_attribute)])):
        attack_var = random.randint(1,4)
        print((str(attack_var)),"      ", sep='', end='', flush=True), time.sleep(0.3)
        attack_result += attack_var
    time.sleep(0.3)
    print('\n'+defender.name, "broni się: rzuca",str(defender.attrib_dict["zwinność"]),"razy kością K4:")
    for i in range(int(defender.attrib_dict["zwinność"])):
        defend_var = random.randint(1,4)
        print((str(attack_var)),"      ", sep='', end='', flush=True), time.sleep(0.3)
        defend_result += defend_var
        
    print("\n\nRezultat:", end=''), dot_loop()
    print('\n\n'+attacker.name+':',attack_result,'+',attacker.attack,"(atak):", attack_result+attacker.attack)
    print(defender.name+':',defend_result,'+',defender.defend,"(obrona):", defend_result+defender.defend)
    if attack_result+attacker.attack <= defend_result+defender.defend:
        print('\n'+defender.name, "obronił się!")
        pause()
        attacker_change = 1
        #attacker = priority_test(enemy = enemy, hero = hero)
        #if float(defend_result+defender.defend) > (float(attack_result+attacker.attack)*1.2):
        attack = int(attack_result+attacker.attack)
        counterattack(enemy = enemy, hero = hero, attacker = attacker, attack = attack)
        return attacker_change

    else:
        damage = random.randint(attacker.dmg_list[0], attacker.dmg_list[1])
        print('\n'+attacker.name, "zadał obrażenia:", defender.name, "stracił", damage, "pkt. życia")
        time.sleep(0.3)
        defender.actualLife -= damage
        if attacker == hero:
            hero.actualExp += damage
            print(hero.name+", zdobyto doświadczenie:", damage)
        if defender.actualLife < 0:
            defender.actualLife = 0
            combat_end = 1
            time.sleep(0.3)
            return combat_end

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
    other_value_list = [display_life(hero = hero),
    display_exp(hero = hero),
    display_gold(hero = hero),
    display_location(hero = hero),
    str(hero.attack),
    str(hero.defend),
    display_damage(hero = hero),
    mod_hero.display_armour(hero = hero)
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



def map_maker(hero_position_h, hero_position_v): # usunąłem pętlę - będzie w głównej pętli raczej - obgadamy 
    '''
    displays map + implement hero movement
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

def event_fight(enemy = None, hero = None):
    '''
    event == fight with random enemy
    '''
    # random generate enemy (using filters):
    enemy = enemy_settings(name = None, loc = hero.location, lvl = None, gen = None)
    enemy.attack = mod_enemy.attack_points_calc(enemy = enemy)
    enemy.defend = mod_enemy.defend_points_calc(enemy = enemy)
    mod_enemy.combat_attribute_default(enemy = enemy)
    enemy.combat_attribute = mod_enemy.combat_attribute_default(enemy = enemy)
    # update hero attrinute:
    mod_hero.combat_attribute_default(hero = hero)
    print("\n\nZaraz, zaraz... Coś się dzieje!\n"), time.sleep(2)
    print("Twój przeciwnik to", end=''), dot_loop()
    
    print(' ',enemy.name.upper()+'!','\n')
    pause()
    # pętla walki:
    combat_end = 0
    while combat_end == 0 and hero.actualLife > 0 and enemy.actualLife > 0:
        # initiative test:
        attacker = priority_test(enemy = enemy, hero = hero)
        # define attacker and defender:
        if attacker == hero: defender = enemy
        elif attacker == enemy: defender = hero  
        attacker_change = 0 # if 1 = loop is break and we repeat initiative test
        while True:
            #clear_screen()
            display_enemy_vs_hero(enemy = enemy, hero = hero, attacker = attacker)
            attacker_change = fight(enemy = enemy, hero = hero, attacker = attacker)
            pause()
            if hero.actualLife < 1:
                rip(enemy = enemy, hero = hero)
                combat_end = 1
                break
            elif enemy.actualLife < 1:
                win_fight(enemy = enemy, hero = hero)
                combat_end = 1
                break
            elif attacker_change == 1:
                break


def event_choose(hero = None, location = None):
    '''
    Depends on the event refers to specific event function
    '''
    ### tymczasowo mamy tylko walkę i zabawę z przedmiotami ;)
    while True:
        display_hero_chart(hero = hero)
        event = input("Jeśli chcesz walki, napisz: walka ")
        if event == "walka":
            display_varied_info()    
            # załóżmy, że wylosowany został event z przeciwnikiem:
            event_fight(enemy = None, hero = hero)
            
        else:
            print("No to pogenerujemy przemioty dla zabawy...")
            # mamy mało itemów, więc filtry wyłączyłem
            treasure_generator(maxloops = 20, maxitem_lvl = None, item_gen = None, hero = hero)




def main():
    clear_screen()
    # set basic variables:
    game_lvl = 1
    add_remove_items_dict = {}

    ######################## HERO CLASS IMPORT TO MAIN: 
    hero = hero_settings()
    hero.attack = mod_hero.attack_points_calc(hero = hero)
    hero.defend = mod_hero.defend_points_calc(hero = hero)
    mod_hero.combat_attribute_default(hero = hero)


    hero.max_armour = mod_hero.amour_max_calc(hero = hero)
    #hero.combat_attribute = mod_hero.combat_attribute_default(hero = hero)

    ### here we can add next hero methods...

    ######################## ENEMY CLASS IMPORT TO MAIN:
    enemy = enemy_settings(name = None, loc = None, lvl = None, gen = None)
    enemy.attack = mod_enemy.attack_points_calc(enemy = enemy)
    enemy.defend = mod_enemy.defend_points_calc(enemy = enemy)
    enemy.combat_attribute = mod_enemy.combat_attribute_default(enemy = enemy)
    ### here we can add next enemy methods...







################ TU URUCHAMIAMY FUNKCJE:
    #intro() # tytuł, powitanie, wybór:

    ####### ładowanie gry LUB tworzenie bohatera LUB galeria sław LUB info o nas
    ####### po każdej z tych funkcji odpalamy główną pętlę:




    '''
    roboczo wstawiam parę rzeczy dla bohatera - pomijamy na razie tworzenie bohatera lub załadowanie z save'a
    '''
    ################## inventory_dict keep only names and values of items (without deep specyfication)
    hero.inventory_dict = {"nóż":1,"placki":50, "resztki mapy":1} #placki będzie można sprzedać albo nakarmić głodnego (quest)
    ################################ show active items on Hero:
    hero.onbody_dict = {u'głowa':'skórzany hełm','szyja':'','tors':'skórzany kaftan','lewa ręka':'','prawa ręka':'maczuga','palec':'','kieszeń':'sok z gumijagód'}
    ################################ przykładowy bohater (odpalenie funkcji hero_crea )
    hero_position_h, hero_position_v = 13, 1 # sets character_player start position (horisontal/vertical)

    # zabawmy się ;) Pętla, żeby wyjść wpisz 'q', jak Cię zapyta o wpisanie enter
    
    event_choose(hero = hero, location = hero.location)





 
    
    
    '''
    # ----- tu będzie funkcja do wyświetlania mapy
    '''


    '''
####################### MAIN LOOP:
    while hero.attrib_additional_dict["życie"] > 0:
        clear_screen()
        display_hero_chart(hero = None)
        display_varied_info() # display short random info :)
        map_maker(hero_position_h, hero_position_v)
        hero_coordinates_position_list = map_maker(hero_position_h, hero_position_v)
        hero_position_h, hero_position_v = hero_coordinates_position_list[0] , hero_coordinates_position_list[1] # update hero's position
    '''
        
    '''

    ###### zabawa z generowaniem przedmiotów (import do main - według nazwy lub filtrów - tak jak z wrogami :) )
    imported_item = items_settings(name = None, loc = hero.location, lvl = None, gen = None, hero = None)

    

    treasure_generator(maxloops = 20, maxitem_lvl = None, item_gen = None, hero = hero) # mamy mało itemów, więc filtry wyłączyłem




    '''







main()




