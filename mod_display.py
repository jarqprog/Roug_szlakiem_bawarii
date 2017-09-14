# mod_varied_info - custom mod, contains list of short messages to random display in main:

import os, math
import random, time
import mod_hero 
import mod_enemy, mod_npc, mod_event, mod_items


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def dot_loop():
    '''
    display animated dot ('.'): . -> .. -> ... 
    '''

    for i in ('...'):        
        print(i, end='', flush=True)
        time.sleep(.2)

def display_hyphen_multiply(multiplier=None):
    '''
    display multiplied hyphen (-----------------)
    '''
    print('-' * multiplier)



def pause():
    '''
    stop game action (for ex. in the middle of fight)
    '''

    if os.name == 'nt': # if windows
        pause = input("\n\n" + "Wciśnij enter żeby kontynuować" + "\n",) # temporary - we need here glitch
    
    else: # if linux
        pause = input("\n\n"+"\x1b[6;31;47m" + "Wciśnij enter żeby kontynuować" + "\x1b[0m"+"\n",)

def display_varied_info():
    '''
    function with a list of short messages (mainly to increse playability). It random generates message to display from list:
    '''
    info_to_display_list = [
    "Ładny dzień", "Zbiera się na burzę", "Trochę zimno",
    "Mam przeczucie, że coś się wydarzy...",
    "Jest bezpiecznie", "Coś mnie niepokoi w tym miejscu", "Coś tu nie tak",
    "Oby nikt tu na mnie nie czyhał", "Trochę wieje", "Mam nadzieję, że zaliczę checkpoint..",
    "Gdzie ten Oblib?", "Ech, Mullog zmarnieje bez obrączki!", "Co by tu zrobić?", "Mam złe przeczucie..",
    "Porada: źródło życia na mapce oznaczone jest znakiem '+'",
    "Porada: symbol '?' oznacza zagadkowe zdarzenie - kto wie, co to może być?"
    
    ]

    random_chanse = random.randint(1,10)
    if random_chanse > 7:
        info_to_display = random.choice(info_to_display_list) # randomly display element of list #info_to_display_list[random.randint(0, len(info_to_display_list)-1)]
    else:
        info_to_display = ''

    return print(info_to_display)


def display_quest_log(hero=None):

    clear_screen()

    print('\n'+hero.name+", zadania do wykonania:\n")
    if len(hero.quest_info) > 0:
        for quest_name in hero.quest_info.keys():
            if quest_name not in hero.quest_completed_list:
                display_hyphen_multiply(multiplier = 42)
                print(quest_name+':')
                for npc_statment in hero.quest_info[quest_name]:
                    print(npc_statment,'\n')

    if len(hero.quest_completed_list) > 0:
        print("\n\nzadania wykonane:\n")
        for quest_name in hero.quest_info.keys():
                if quest_name in hero.quest_completed_list:
                    display_hyphen_multiply(multiplier = 42)
                    print(quest_name+':')
                    for npc_statment in hero.quest_info[quest_name]:
                        print(npc_statment,'\n')
        

    dot_loop()
    pause()


def display_hero_chart(hero=None):
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

    mod_hero.attack_points_calc(hero)
    mod_hero.defend_points_calc(hero)


    #################### OTHERS: life, exp, gold, location ############################
    other_key_list = ["życie", "doświadczenie", "złoto", "lokalizacja", "atak", "obrona", "obrażenia", "pancerz"]
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
    printing_var = 5 #helps correctly print hero chart
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
    # to print in head: hero name, profession, level (exp level)
    printing_var = 0 #helps correctly print hero chart
    h00 = hero.name.ljust(printing_var)
    h01 = hero.proffession.ljust(printing_var)
    h02 = str(hero.level).ljust(printing_var)

    printing_var = 2 #helps correctly print hero chart
    h1 = 'atrybuty:'.rjust(long_att_key+printing_var)
    printing_var = 0
    h2 = 'w torbie:'.rjust(long_att_val+long_inv_key+printing_var)
    printing_var = 1
    h3 = 'na sobie:'.rjust(long_inv_val+long_onbody_key+printing_var)
    h4 = 'pozostałe:'.rjust(long_onbody_val+long_other_key+printing_var)
    print(u'\n',h00,"-",h01, h02, 'poziom doświadczenia','\n') # hero name, profession, level
    print(h1,h2,h3,h4) # head: attribs, items in bag, others spec (attack, defend, life, exp..)
    printing_var_head_bottom = 5 #helps correctly print hero chart
    display_hyphen_multiply(multiplier = (sum_longest_arg+printing_var_head_bottom))

    for i in range(int(total_number_of_items)) :
        
        # printing attributes (siła, zwinność...):
        # (if one of the columns is shorter, program will print empty string, to not copy same thing):
        try:
            # if quantity of line to print (len) is less then 'i' in loop, program will generate empty string:
            int(len(attrib_regular_key_list)) >= i 
            if int(len(attrib_regular_key_list)) >= i:
                iattrib = int(i)
                attribKeyPrt = str(attrib_regular_key_list[iattrib])+':'
                attribValuePrt = str(attrib_regular_value_list[iattrib])
        except:
            attribKeyPrt = "" # empty string
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
                otherKeyPrt = str(other_key_list[iother])+':'
                otherValuePrt = str(other_value_list[iother])
        except:
            otherKeyPrt = ""
            otherValuePrt = ""

    # variables used to display table:
        p1 = attribKeyPrt.rjust(long_att_key) # attrib name
        p2 = attribValuePrt.ljust(long_att_val) # attrib value
        p3 = inventoryKeyPrt.rjust(long_inv_key) # item in inventory - name
        p4 = inventoryValuePrt.ljust(long_inv_val) # item in inventory - quantity
        p5 = onbodyKeyPrt.rjust(long_onbody_key) # body part
        p6 = onbodyValuePrt.ljust(long_onbody_val) # item on body
        p7 = otherKeyPrt.rjust(long_other_key) # other spec name
        p8 = otherValuePrt.ljust(long_other_val) # other spec value

        # body of table:
        print(u'',p1,p2,p3,p4,p5,p6,p7,p8)
    # footer of table:
    display_hyphen_multiply(multiplier = (sum_longest_arg+printing_var_head_bottom))


def display_shop(hero=None):
    '''
    display event shop
    '''
    clear_screen()
    items_to_buy = mod_items.item_dict_generator(hero, level = None) # shop items to buy (dict type)

    items_to_buy_list = [item.name for item in items_to_buy.keys()] # shop item names to buy (list type)
    items_to_sell_list = [item for item in hero.inventory_dict.keys()] # hero item names to sell (list type)
    # check lenght of longest item name
    all_list = items_to_buy_list + items_to_sell_list
    printing_var = 5 # variable used in printing below
    longest_word = (max(len(x) for x in all_list))+printing_var # # set lenght of longest item name
    multiplier = 90 # variable used in proper printing ------ ('display_hyphen_multiply' function):

    while True:
        print(hero.name,", witaj w moim sklepie. Oto mój asortyment:")       
        display_hyphen_multiply(multiplier)
        items_to_buy_list = []
        # display shop assortment:
        for number, item in enumerate(items_to_buy.keys()):
            items_to_buy_list.append(item.name)

            # variable used in printing below:
            el_to_pr_1 = str(number+1)+':' # el_to_pr_1 means 'element to print'
            el_to_pr_2 = item.name # item name
            el_to_pr_3 = "cena:".rjust(longest_word-len(el_to_pr_2))
            el_to_pr_4 = str(item.price)
            printing_var = 12
            el_to_pr_5 = "info:".rjust(printing_var - len(el_to_pr_4))
            el_to_pr_6 = str(item.item_info)

            print(el_to_pr_1, el_to_pr_2, el_to_pr_3, el_to_pr_4, el_to_pr_5, el_to_pr_6)


        print("\nPosiadane rzeczy w Twojej torbie:")
        display_hyphen_multiply(multiplier)
        # display items in hero inventory:
        printing_var = 7
        for number, item_name in enumerate(hero.inventory_dict.keys()):
            # set item data:
            item = mod_items.items_settings(name=item_name, loc=None, lvl=None, gen=None, hero=None, all=None)  
            # variable used in printing below:
            el_to_pr_1 = str(number+1)+':' # el_to_pr_1 means 'element to print'
            el_to_pr_2 = item.name + ' ('+str(hero.inventory_dict[item_name])+')' # item name + quantity of items in bag
            el_to_pr_3 = "cena:".rjust(longest_word-len(el_to_pr_2))
            el_to_pr_4 = str(item.price)
            printing_var = 12
            el_to_pr_5 = "info:".rjust(printing_var - len(el_to_pr_4))
            el_to_pr_6 = str(item.item_info)

            print(el_to_pr_1, el_to_pr_2, el_to_pr_3, el_to_pr_4, el_to_pr_5, el_to_pr_6)


        print("\nPosiadane złoto:",str(hero.gold)+"\n")

        expression = 'wybierz 1 (kup) lub 2 (sprzedaj) i zatwierdź <enter> ---> '
        condition = ('1', '2')
        user_choice = user_choice_input(condition, expression)
        if user_choice == '1':
            expression = 'wybierz numer przedmiotu do zakupu i zatwierdź <enter>: --> '
            condition = str((range(len(items_to_buy_list))))
            user_choice = user_choice_input(condition, expression)


        else:
            expression = 'wybierz numer przedmiotu do sprzedania i zatwierdź <enter>: --> '
            condition = str((range(len(hero.inventory_dict))))
            user_choice = user_choice_input(condition, expression)
        


        break

        '''
        choice_sell_buy = input("\nJeśli chcesz kupić, wybierz 1, jeśli sprzedać, wybierz 2 (i zatwierdź <enter>): --> ")
        while True:
            try:
                choice_sell_buy == '1' or choice_sell_buy == '2'
                break
            except:
                choice_sell_buy = input("Wybierz 1 (kup) lub 2 (sprzedaj) i potwierdź <enter> --> ")
        
        if choice_sell_buy == '1':
            choice_buy_item = input("\nWybierz numer przedmiotu do zakupu i zatwierdź <enter>: --> ")
            while True:
                try:
                    if int(choice_buy_item) <= len(items_to_buy_list):
                        break
                    else:
                        choice_buy_item = input("\nNie ma takiego przedmiotu, wybierz ponownie numer i zatwierdź <enter>: --> ")
                    
                    

                except:
                    choice_buy_item = input("\nNie ma takiego przedmiotu, wybierz ponownie numer i zatwierdź <enter>: --> ")
  
            while True:
                try:
                    choice_sell_buy == '1' or choice_sell_buy == '2'
                    break
                except:
                    choice_sell_buy = input("Wybierz 1 (kup) lub 2 (sprzedaj) i potwierdź <enter> --> ")
            '''

def user_choice_input(condition=None, expression=None):
    '''
    helper function: take input from user 
    display expression, for ex. 'wybierz 1 (kup) lub 2 (sprzedaj) i zatwierdź <enter> ---> '
    work in loop - if condition is true, for ex.: condition = ('1', '2')
    ---> break loop and return input
    '''
    user_choice = input(expression)
    while True:
        try:
            if user_choice in condition:
                break
            else:
                user_choice = input(expression)

        except:
            print(expression)

    return user_choice
        

def display_enemy_vs_hero(enemy=None, hero=None, attacker=None):
    '''
    display basic info about enemy compared to hero's stats 
    '''
    clear_screen()
    mod_hero.attack_points_calc(hero)
    mod_hero.defend_points_calc(hero)
    mod_enemy.enemy_info(enemy=enemy)
    # check what is main enemy attribut in combat
    enemy.combat_attribute = mod_enemy.combat_attribute_default(enemy=enemy)

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

    # this part of code helps display_hyphen_multiply function (display ----- in proper lenght):
    printing_var_add = 4 # variable used in printing below
    # search for sum of lenght of element in all lists:
    all_lists = [head_to_display_list1 + hero_to_display_list1 + enem_to_display_list1]
    longest_of_all_lists = max(len(str(x)) for x in all_lists) + printing_var + printing_var_add
    
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

    # prints info about enemy and hero/enemy stats (table form):
    print("\nstatystki:".rjust(longest_arg))
    display_hyphen_multiply(multiplier=longest_of_all_lists) # display ------
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
    print("")
    display_hyphen_multiply(multiplier=longest_of_all_lists) # display ------


def calendar(hero=None):
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



def display_looted_items(add_remove_items_dict):
    '''
    displays looted/buyed items (from "add_remove_items_dict")
    '''
    total_number_of_items = 0
    print("\nDodano do torby:")
    multiplier = 30 # variable used in proper pronting ------:
    display_hyphen_multiply(multiplier)
    for item in add_remove_items_dict:
        print(item,": ", add_remove_items_dict[item],"; ", sep='', end='', flush=True) #prints in line (place economy)
        total_number_of_items += int(add_remove_items_dict[item])


def display_calendar_location(hero=None):
    '''
    display short info about day, day time, location, weather info, eventually random npc statement
    '''
    calendar_list = hero.calendar_list
    location = mod_hero.display_location(hero)
    mod_hero.calendar(calendar_list)
    print("dzień:", hero.calendar_list[0], ",", hero.calendar_list[1] +", "+ hero.calendar_list[2] +". Miejsce:", location)
    multiplier = 90 # variable used in proper pronting ------:
    display_hyphen_multiply(multiplier)
    display_varied_info()
    chance_to_random_npc_meet = random.randint(1,100)
    if chance_to_random_npc_meet > 80:
        mod_event.event_random_npc(hero=hero)
    else:
        print("")
 
    return calendar_list


def display_NPC_random_speach(npc=None):
    '''
    display short random npc speach (decorational element)
    '''
    speach_to_display = random.choice(npc.speach_list)
    print("Napotkany", npc.name, "do Ciebie:", speach_to_display + "...\r\r")


def display_event_quest(npc=None, hero=None):
    '''
    display quest info, dialogs, info about quest result
    '''
    random_speach = "".join('\n'+npc.name + " do Ciebie: " + str(npc.speach_list[random.randint(0,len(npc.speach_list)-1)]))
    print(random_speach)
    if npc.quest_name not in hero.quest_completed_list:

        for element in hero.quest_info[npc.quest_name]:
            if element not in hero.quest_blocked_list:
                if npc.quest_condition in hero.quest_condition_list:
                    info_to_display = (element +". Gratulacje, zdobyto: "+ str(npc.xp_reward)+" punktów doświadczenia! ")
                    hero.actualExp += npc.xp_reward
                    hero.quest_completed_list.append(npc.quest_name)
                    if "portal 2" in npc.quest_special_reward:
                        hero.new_location = 2
                    elif "portal 3" in npc.quest_special_reward:
                        hero.new_location = 3
                    elif "portal 4" in npc.quest_special_reward:
                        hero.new_location = 4

                else:             
                    info_to_display = element

                quest_name_to_display = "Zadanie: ", npc.quest_name, " (przywołaj dziennikiem zadań).."                    
                print('\n'+info_to_display)
                print("".join(quest_name_to_display))
                if len(npc.inventory_dict) > 0 and npc.quest_condition in hero.quest_condition_list:
                    print("\r - wykonane.")
                    add_remove_items_dict = npc.inventory_dict
                    mod_hero.inventory_update(hero, add_remove_items_dict)                     
                    display_looted_items(add_remove_items_dict)
                
                break

    return hero, npc


def display_next_level_promotion(hero=None):
    '''
    display hero attributes for lvl promotion function
    '''           

    number = 1
    for key, value in hero.attrib_dict.items():
        print(str(number).ljust(0)+':',key.ljust(0),'(aktualna wartość: '+str(value).ljust(0)+')')
        number += 1
    
    player_choice = input("\nAwans! Otrzymujesz punkt rozwoju, wybierz numer atrybutu, który chcesz podnieść i zatwierdź <enter>: ") 
    display_hyphen_multiply(multiplier=82)
    while True:
        try: 
            int(player_choice) in range(1, 5)
            break

        except:
            player_choice = input("podaj numer atrybutu.. ")
    
    return player_choice







    

 