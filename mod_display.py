#!/usr/bin/python3
# mod_display - custom mod
# includes display in console functions

import os
import math
import random
import time
import sys

# import custom mods
import mod_hero
import mod_enemy
import mod_event
import mod_items

# import getch (avoid problem with windows/ubuntu)
try:
    from msvcrt import getwch as getch

except ImportError:
    def getch():
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


def clear_screen():
    '''
    clear screen - universal for ubuntu/windows platform
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def dot_loop():
    '''
    display animated dot ('.'): . -> .. -> ...
    '''
    for i in ('...'):
        # don't know how tu handle with pep8 in this line
        print(i, end='', flush=True)
        # time.sleep(.2)


def display_hyphen_multiply(multiplier=None):
    '''
    display multiplied hyphen (-----------------)
    '''
    print('-' * multiplier)


def pause():
    '''
    stop game action (for ex. in the middle of fight)
    '''
    print('\n\n(wciśnij dowolny klawisz, by kontynuować..)\n')
    char = getch()


def display_varied_info():
    '''
    function with a list of short messages (mainly to increse playability).
    It random generates message to display from list:
    '''
    info_to_display_list = [
        "Ładny dzień", "Zbiera się na burzę", "Trochę zimno",
        "Mam przeczucie, że coś się wydarzy...",
        "Jest bezpiecznie", "Coś mnie niepokoi w tym miejscu", "Coś tu nie tak",
        "Oby nikt tu na mnie nie czyhał", "Trochę wieje",
        "Mam nadzieję, że zaliczę checkpoint..",
        "Gdzie ten Oblib?", "Ech, Mullog zmarnieje bez obrączki!",
        "Co by tu zrobić?", "Mam złe przeczucie..",
        "Porada: źródło życia na mapce oznaczone jest znakiem '+'",
        "Porada: symbol '?' oznacza zagadkowe zdarzenie - kto wie, co to może być?"
        ]

    random_chance = random.randint(1, 10)
    if random_chance > 7:
        info_to_display = random.choice(info_to_display_list)
    else:
        info_to_display = ''

    return print(info_to_display)


def display_quest_log(hero):
    '''
    display quest log with quests: in progress and already completed
    '''
    clear_screen()

    print('\n'+hero.name+", zadania do wykonania:\n")
    if len(hero.quest_info) > 0:
        for quest_name in hero.quest_info.keys():
            if quest_name not in hero.quest_completed_list:
                # variable used in function below (multiply '-')
                multiplier = 42
                display_hyphen_multiply(multiplier)
                print(quest_name+':')
                for npc_statment in hero.quest_info[quest_name]:
                    print(npc_statment, '\n')

    if len(hero.quest_completed_list) > 0:
        print("\n\nzadania wykonane:\n")
        for quest_name in hero.quest_info.keys():
                if quest_name in hero.quest_completed_list:
                    print(quest_name+'\n')

    pause()


def display_hero_chart(hero):
    """display hero's chart - attributes, inventory items, wearing items"""
    clear_screen()
    # create lists from hero attributes, inventory, weared items,
    # additional attributes:
    attrib_regular_key_list = list(hero.attrib_dict.keys())
    attrib_regular_value_list = list(hero.attrib_dict.values())
    inventory_key_list = list(hero.inventory_dict.keys())
    inventory_value_list = list(hero.inventory_dict.values())
    onbody_key_list = list(hero.onbody_dict.keys())
    onbody_value_list = list(hero.onbody_dict.values())
    # (additional attributes)
    other_key_list = [
        "życie", "doświadczenie", "złoto", "lokalizacja", "atak",
        "obrona", "obrażenia", "pancerz"
        ]
    other_value_list = [
        mod_hero.display_life(hero),
        mod_hero.display_exp(hero),
        mod_hero.display_gold(hero),
        mod_hero.display_location(hero),
        str(hero.attack),
        str(hero.defend),
        mod_hero.display_damage(hero),
        mod_hero.display_armour(hero)
        ]
    # check the most numerous lists:
    # (to properly print chart)
    total_number_of_items = max(
        len(attrib_regular_key_list),
        len(inventory_key_list),
        len(onbody_key_list),
        len(other_key_list)
        )
    # check the longest word in lists:
    # (to properly print chart)
    printing_var = 5  # helps correctly print hero chart
    long_att_key = (max(len(x) for x in attrib_regular_key_list))+printing_var
    long_att_val = (max(len(str(x)) for x in attrib_regular_value_list))
    # if hero inventory isn't empty:
    if len(hero.inventory_dict) > 0:
        long_inv_key = (max(len(x) for x in inventory_key_list))+printing_var
        long_inv_val = (max(len(str(x)) for x in inventory_value_list))
    # in case of empty inventory (safeguard against error):
    else:
        long_inv_key = 1
        long_inv_val = 1
    long_onbody_key = (max(len(x) for x in onbody_key_list))+printing_var
    long_onbody_val = (max(len(x) for x in onbody_value_list))+printing_var
    long_other_key = (max(len(x) for x in other_key_list))+printing_var
    long_other_val = (max(len(x) for x in other_value_list))+printing_var

    # sum_longest_arg is used to print table's head and bottom line (---):
    sum_longest_arg = int(
        long_att_key + long_att_val + long_inv_key + long_inv_val +
        long_onbody_key + long_onbody_val + long_other_key + long_other_val
        )
    # specify variable to print in table's head:
    # hero name, profession, level (exp level)
    printing_var = 0  # helps correctly print hero chart
    h00 = hero.name.ljust(printing_var)
    h01 = hero.proffession.ljust(printing_var)
    h02 = str(hero.level).ljust(printing_var)
    print(
        '\n', h00, "-", h01, h02 +
        ', poziom doświadczenia\n'
        )
    # head: attribs, items in bag, others spec (attack, defend, life, exp..)
    printing_var = 2
    h1 = 'atrybuty:'.rjust(long_att_key+printing_var)
    printing_var = 0
    h2 = 'w torbie:'.rjust(long_att_val+long_inv_key+printing_var)
    printing_var = 1
    h3 = 'na sobie:'.rjust(long_inv_val+long_onbody_key+printing_var)
    h4 = 'pozostałe:'.rjust(long_onbody_val+long_other_key+printing_var)
    print(h1, h2, h3, h4)

    printing_var_head_bottom = 5
    # display '------'
    display_hyphen_multiply(
        multiplier=(sum_longest_arg + printing_var_head_bottom)
        )

    for i in range(int(total_number_of_items)):
        
        # printing attributes (siła, zwinność...):
        # (if one of the columns is shorter, program will print empty string,
        # to not copy same thing):
        try:
            # if quantity of line to print (len) is less then 'i' in loop,
            # program will generate empty string:
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
                otherKeyPrt = str(other_key_list[iother])+':'
                otherValuePrt = str(other_value_list[iother])
        except:
            otherKeyPrt = ""
            otherValuePrt = ""

    # set variables to display table's body:
        p1 = attribKeyPrt.rjust(long_att_key)  # attrib name
        p2 = attribValuePrt.ljust(long_att_val)  # attrib value
        p3 = inventoryKeyPrt.rjust(long_inv_key)  # item name (inventory)
        p4 = inventoryValuePrt.ljust(long_inv_val)  # item quantity (inventory)
        p5 = onbodyKeyPrt.rjust(long_onbody_key)  # body part
        p6 = onbodyValuePrt.ljust(long_onbody_val)  # item on body
        p7 = otherKeyPrt.rjust(long_other_key)  # other spec name
        p8 = otherValuePrt.ljust(long_other_val)  # other spec value
        
        # display table's body:
        print('', p1, p2, p3, p4, p5, p6, p7, p8)
    
    # display table's footer (----):
    display_hyphen_multiply(
        multiplier=(sum_longest_arg+printing_var_head_bottom)
        )


def display_inventory_chart(hero):
    '''
    display inventory chart (items in inventory and onbody hero dicts)
    '''
    pass


def display_shop(hero, items_to_buy):
    '''
    display event shop
    '''
    clear_screen()
    # shop item names to buy (list type)
    items_to_buy_list = [item[0] for item in items_to_buy.values()]
    # hero item names to sell (list type)
    items_to_sell_list = [item for item in hero.inventory_dict.keys()]
    # check lenght of longest item name
    all_list = items_to_buy_list + items_to_sell_list
    printing_var = 8  # variable used in printing below
    # set lenght of longest item name
    longest_word = (max(len(x) for x in all_list))+printing_var
    multiplier = 90  # multiplier used in display_hyphen_multiply function
    shop_margin = 1.2  # item price + 20%
    print(hero.name+", witaj w moim sklepie.\nOto moje towary:\n")
    # SHOP ITEMS (to buy)
    for item in items_to_buy.keys():
        # variable used in printing below:
        # (el_to_pr_.. means 'element to print')
        el_to_pr_1 = item+':'
        el_to_pr_2 = items_to_buy[item][0]  # item name
        el_to_pr_3 = "cena:".rjust(longest_word-len(el_to_pr_2))
        # item price + 20% (string -> float -> integer):
        el_to_pr_4 = str(int(int(items_to_buy[item][1])*shop_margin))
        printing_var = 12
        el_to_pr_5 = "info:".rjust(printing_var - len(el_to_pr_4))
        el_to_pr_6 = items_to_buy[item][2]  # item info
        # display elements:
        print(
            el_to_pr_1, el_to_pr_2, el_to_pr_3,
            el_to_pr_4, el_to_pr_5, el_to_pr_6
            )

    # HERO ITEMS (to sell)
    print("\nPosiadane rzeczy w Twojej torbie:")
    # if hero inventory is empty:
    if len(hero.inventory_dict.keys()) == 0:
        print(
            '\r-torba jest pusta, nie masz niczego na sprzedaż..\
            \nPosiadane złoto:',
            str(hero.gold)+'\n\n\n'
            )
    # if hero has some items in inventory:
    else:
        # display '--------'
        display_hyphen_multiply(multiplier)
        # display items in hero inventory:
        for number, item_name in enumerate(hero.inventory_dict.keys()):
            # set item data:
            item = mod_items.import_item(name=item_name)
            # variable used in printing below:
            el_to_pr_1 = str(number+1)+':'  # item number
            el_to_pr_2 = (
                item_name +
                ' (' +
                str(hero.inventory_dict[item_name]) +
                ')')  # item name + quantity of items in bag (e.g. sword (2))

            el_to_pr_3 = "cena:".rjust(longest_word-len(el_to_pr_2))
            el_to_pr_4 = str(item.price)  # item price
            printing_var = 12
            el_to_pr_5 = "info:".rjust(printing_var - len(el_to_pr_4))
            el_to_pr_6 = str(item.item_info)  # item info

            # display elements:
            print(
                el_to_pr_1, el_to_pr_2, el_to_pr_3,
                el_to_pr_4, el_to_pr_5, el_to_pr_6
                )
        # display info about hero gold:
        print("\nPosiadane złoto:", str(hero.gold)+"\n\n")

    return items_to_buy


def display_player_choice_shop(hero, items_to_buy):
    '''
    player choice system while selling or buying in shop
    '''
    # first element in expression (constant):
    exp_start = ' <-- wybierz '
    # last element in expression (constant):
    exp_end = ", 'w' - wyjście, <enter> - zatwierdza wybór"
    # custom element in expression:
    exp_middle = "'1' - zakup, '2' - sprzedaż"
    expression = exp_start + exp_middle + exp_end
    condition = ('1', '2', 'W')
    user_choice = user_choice_input(condition, expression)

    return user_choice


def shop_hero_buy(hero, items_to_buy):
    '''
    buy item in shop
    '''
    # first element in expression (constant):
    exp_start = ' <-- wybierz '
    # last element in expression (constant):
    exp_end = ", 'w' - wyjście, <enter> - zatwierdza wybór"
    # specify range of player choice (number of items):
    exp_var = str(len(items_to_buy))
    exp_middle = "numer przedmiotu do zakupu (1-" + exp_var + ")"
    expression = exp_start + exp_middle + exp_end
    # condition: item number in range items_to_buy dict or 'W' (exit):
    condition = [str(number+1) for number in range(len(items_to_buy))]+['W']
    user_choice = user_choice_input(condition, expression)
    if user_choice == 'W':

        return user_choice  # break shop loop

    item_number = user_choice  # item (key) in items_to_buy dict
    item_name = items_to_buy[item_number][0]
    shop_margin = 1.2  # item price + 20%
    # final price = item price + 20% (shop margin):
    price = int(int(items_to_buy[item_number][1])*shop_margin)
    if hero.gold < price:  # if hero has not enough gold
        print('\nNie posiadasz wystarczającej ilości złota.\n'), pause()

        return user_choice  # back to loop

    else:  # if hero has enough gold
        print(
            '\nWybrano:', item_name + ', cena:', str(price) +
            ', Twoje złoto:', str(hero.gold)+', czy potwierdzasz?\n\n'
            )
    
        exp_middle = "'t' - tak, 'n' - nie"
        expression = exp_start + exp_middle + exp_end
        condition = ('T', 'N', 'W')
        user_choice = user_choice_input(condition, expression)
        if user_choice == 'N':

            return user_choice

        elif user_choice == 'T':
            hero.gold -= int(price)  # subtract price
            # add item to hero inventory:
            add_remove_items_dict = {item_name: 1}
            mod_hero.inventory_update(hero, add_remove_items_dict)
            display_looted_items(add_remove_items_dict)
            print('Twoja sakwa jest lżejsza, wydałeś', price, 'sztuk złota!\n')
            pause()

            return hero

        else:
            user_choice = 'W'  # exit from shop

            return user_choice


def shop_hero_sell(hero):
    '''
    sell item in shop
    '''
    # hero inventory is empty:
    if len(hero.inventory_dict.keys()) == 0:
        print('\ntorba jest pusta, nie masz niczego na sprzedaż.. \n\n')
        pause()

        return hero

    # hero has items in inventory:
    else:
        exp_start = ' <-- wybierz '  # first element in expression (constant)
        exp_end = ", 'w' - wyjście, <enter> - zatwierdza wybór"
        # specify range of player choice (number of items):
        exp_var = str(len(hero.inventory_dict.keys()))
        exp_middle = "numer przedmiotu do sprzedaży (1-" + exp_var + ")"
        expression = exp_start + exp_middle + exp_end
        # condition: item number in range items_to_buy dict or 'W' (exit):
        condition = (
            [str(num+1) for num in range(len(hero.inventory_dict.keys()))] +
            ['W']
            )
        user_choice = user_choice_input(condition, expression)
        if user_choice == 'W':

            return user_choice  # exit shop

        else:
            # make dict with hero items
            # (key is number, value is list with item attributes:
            # name, price, quantity):
            items_to_sell = mod_items.generate_hero_items_to_sell_dict(hero)
            item_name = items_to_sell[user_choice][0]
            item_price = int(items_to_sell[user_choice][1])
            if item_price == 0:
                print(
                    '\nNie kupię tego, przedmiot',
                    item_name, 'jest dla mnie bezwartościowy.\n'
                    )
                pause()

                return hero  # back to main choice

            # quantity of specified item (user_choice) in hero inventory:
            item_quantity = int(items_to_sell[user_choice][2])
            if item_quantity == 1:
                quantity = '1'  # used in printing at the end of function
                gold_earned = item_price

            else:  # quantity of specified item in hero inventory > 1..
                print('\nJaką ilość chcesz sprzedać?\n')

                exp_var = str(item_quantity)  # quanitity of item limit
                exp_middle = "z przedziału (1-" + exp_var + ")"
                expression = exp_start + exp_middle + exp_end
                # condition is list of item number
                # in range quanitity of item limit or 'W' (exit):
                condition = (
                    [str(num+1) for num in range(item_quantity)] +
                    ['W'])
                user_choice = user_choice_input(condition, expression)

                if user_choice == 'W':  # exit

                    return user_choice  # break shop loop

                else:
                    quantity = user_choice
                    gold_earned = item_price * int(user_choice)

            print(
                '\nWybrano:', item_name +
                ', ilość:', quantity + ', otrzymasz:', str(gold_earned),
                'sztuk złota. Czy powierdzasz?\n\n'
                )
            exp_middle = "'t' - tak, 'n' - nie"
            expression = exp_start + exp_middle + exp_end
            condition = ('T', 'N', 'W')
            user_choice = user_choice_input(condition, expression)
            if user_choice == 'W':
                
                return user_choice  # exit shop

            elif user_choice == 'N':
                
                return user_choice  # back to begining

            else:  # selling is confirmed
                hero.gold += gold_earned
                # remove item to hero inventory:
                add_remove_items_dict = {item_name: -(int(quantity))}
                mod_hero.inventory_update(hero, add_remove_items_dict)
                display_looted_items(add_remove_items_dict)
                print(
                    'Twoja sakwa jest cięższa, przybyło', str(gold_earned),
                    'sztuk złota!\n'
                    )
                pause()

                return hero


def user_choice_input(condition, expression):
    '''
    helper function: take input from user
    display expression, for e.g.:
    'wybierz 1 (kup) lub 2 (sprzedaj) i zatwierdź <enter> ---> '
    condition should be tuple or list
    work in loop - if condition is true, for ex.: condition = ('1', '2')
    ---> break loop and return input
    '''
    user_choice = ''
    # changed na Ania

    while True:
        if os.name != 'nt':  # if not windows
            sys.stdout.write("\033[F")  # Cursor up one line
        user_choice = (input('\t'+expression+'\r')).upper()
        try:
            if user_choice in condition:

                return user_choice.upper()

        except:
            pass  # wonna avoid error info


def display_enemy_vs_hero(hero, enemy=None, attacker=None):
    '''
    display basic info about enemy compared to hero's stats
    '''
    clear_screen()
    mod_enemy.enemy_info(enemy)
    # check what is main enemy attribut in combat

    enemy_dmg = (
        "".join([str(enemy.dmg_list[0]), "-", str(enemy.dmg_list[1])])
        )  # used below in enemy_to_display_list
    printing_var = 2  # variable that helps in printing (used below)
    # make list of attributes names to print in table's head
    # (siła, zwinność, percepcja...):
    head_to_display_list1 = [""]+list(hero.attrib_dict.keys())
    # make list of hero attributes values to print:
    hero_to_display_list1 = [hero.name+':']+list(hero.attrib_dict.values())
    # make list of enemy attributes values to print:
    enem_to_display_list1 = [enemy.name+':']+list(enemy.attrib_dict.values())
    # make list of other attributes names to print in table's head
    # (życie, obrażenia, atak..)
    head_to_display_list2 = [
        "", "życie", "obrażenia", "atak", "obrona", "cecha wiodąca"
        ]
    # make list of hero attributes values to print:
    hero_to_display_list2 = [
        hero.name+':', str(hero.actualLife),
        str(mod_hero.display_damage(hero))] + list(
        [str(hero.attack), str(hero.defend), str(hero.combat_attribute)]
        )
    # make list of enemy attributes values to print:
    enem_to_display_list2 = ([
        enemy.name+':', enemy.actualLife, enemy_dmg] + list(
        [str(enemy.attack), str(enemy.defend), str(enemy.combat_attribute)])
        )
    # search for the longest element in each lists
    # (needed to print nice table with stats):
    long_head = max(len(str(x)) for x in head_to_display_list1)+printing_var
    long_hero = max(len(str(x)) for x in hero_to_display_list1)+printing_var
    long_enem = max(len(str(x)) for x in enem_to_display_list1)+printing_var
    # search for longest of the longest elements in lists:
    longest_arg = max(
        list((int(x)) for x in (long_head, long_hero, long_enem))
        )
    # this part of code helps display_hyphen_multiply function
    # (display ----- in proper lenght):
    printing_var_add = 4  # variable used in printing below
    # search for sum of lenght of element in all lists:
    all_lists = [
        head_to_display_list1 +
        hero_to_display_list1 +
        enem_to_display_list1
        ]

    longest_of_all_lists = (
        max(len(str(x)) for x in all_lists) +
        printing_var + printing_var_add
        )

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

    # prints info about enemy and hero/enemy stats (table form):
    print("\nstatystki:".rjust(longest_arg))
    display_hyphen_multiply(multiplier=longest_of_all_lists)  # display '----'
    for i in range(len(head_to_display_list1)):
        print(
            str(head_to_display_list1[int(i)]).rjust(longest_arg),
            " ", sep='', end='', flush=True)
    print("\r")
    for i in range(len(head_to_display_list1)):
        print(
            str(hero_to_display_list1[int(i)]).rjust(longest_arg),
            " ", sep='', end='', flush=True)
    print("\r")
    for i in range(len(head_to_display_list1)):
        print(
            str(enem_to_display_list1[int(i)]).rjust(longest_arg),
            " ", sep='', end='', flush=True)
    print('\n')
    for i in range(len(head_to_display_list2)):
        print(
            str(head_to_display_list2[int(i)]).rjust(longest_arg),
            " ", sep='', end='', flush=True)
    print("\r")
    for i in range(len(head_to_display_list2)):
        print(
            str(hero_to_display_list2[int(i)]).rjust(longest_arg),
            " ", sep='', end='', flush=True)
    print("\r")
    for i in range(len(head_to_display_list2)):
        print(
            str(enem_to_display_list2[int(i)]).rjust(longest_arg),
            " ", sep='', end='', flush=True)
    print("")
    display_hyphen_multiply(multiplier=longest_of_all_lists)  # display '----'


def calendar(hero):
    '''
    display short info about day, day time using turn counter
    '''
    turn_counter = mod_hero.calendar(hero)

    week_list = [
        "poniedziałek", "wtorek", "środa", "czwartek",
        "piątek", "sobota", "niedziela"
        ]
    day_time_list = ["poranek", "południe", "popołudniu", "wieczór"]
    day = math.floor(turn_counter/4)  # 4 - for four day times
    if turn_counter % 4 == 0:
        day_time = day_time_list[3]
    elif turn_counter % 3 == 0:
        day_time = day_time_list[2]
    elif turn_counter % 2 == 0:
        day_time = day_time_list[1]
    else:
        day_time = day_time_list[0]

    return print(
        "Dzień", str(day) +
        ",", day_time +
        ", jesteś w krainie:",
        mod_hero.display_location(hero) + "."
        )


def display_looted_items(add_remove_items_dict):
    '''
    displays looted/buyed items (from "add_remove_items_dict")
    '''
    time.sleep(.2)
    if len(add_remove_items_dict) > 0:
        print("\nW torbie:")
        multiplier = 30  # variable used in proper printing ------:
        display_hyphen_multiply(multiplier)
        for item in add_remove_items_dict:
            print(item, ":", add_remove_items_dict[item])


def display_calendar_location(hero):
    '''
    display short info about day, day time,
    location, weather info, eventually random npc statement
    '''
    calendar_list = hero.calendar_list
    location = mod_hero.display_location(hero)
    mod_hero.calendar(calendar_list)
    print(
        "dzień:", hero.calendar_list[0], ",", hero.calendar_list[1] +
        ", " + hero.calendar_list[2] + ". Miejsce:", location)
    multiplier = 81  # variable used in proper pronting ------:
    display_hyphen_multiply(multiplier)
    chance_to_random_npc_meet = random.randint(1, 100)
    if chance_to_random_npc_meet <= 80:  # usually display only weather info
        display_varied_info()
    else:
        # sometimes info about friendly NPC thah hero has met:
        mod_event.event_random_npc(hero=hero)

    return calendar_list


def display_NPC_random_speach(npc=None):
    '''
    display short random npc speach (decorational element)
    '''
    speach_to_display = random.choice(npc.speach_list)
    print("Napotkany", npc.name, "do Ciebie:", speach_to_display + "...\r\r")


def display_event_quest(hero, npc=None):
    '''
    display quest info, dialogs, info about quest result
    '''
    # random speach is short npc's 'small talk'
    random_speach = "".join(
            '\n'+npc.name + " do Ciebie: " +
            random.choice(npc.speach_list)
            )
    print(random_speach)
    # if quest is not completed yet:
    if npc.quest_name not in hero.quest_completed_list:
        # display npc's statement associated with quest:
        elements = ''  # stores npc's statments to display
        # element is npc statement connected with quest:
        for element in hero.quest_info[npc.quest_name]:
            if element not in hero.quest_blocked_list:
                # quest_blocked_list stores statement,
                # that have been already used by npc
                elements += '\n'+element
                # block already displayed statements:
                hero.quest_blocked_list.append(element)

        quest_name_to_display = (
            "Zadanie: ", npc.quest_name, " (przywołaj dziennikiem zadań).."
            )
        # quest is not finished:
        if npc.quest_condition not in hero.quest_condition_list:
            # display info about quest and quest log:
            print('\n'+elements)
            print("".join(quest_name_to_display))
        
        # quest is finished:
        else:
            # add quest name to hero quest completed list
            # (block this quest in future):
            hero.quest_completed_list.append(npc.quest_name)
            # display info if quest is completed:
            print('\n'+elements)  # display statement
            print("".join(quest_name_to_display))
            print("\r - wykonane.")
            print(
                "\n\nGratulacje, zdobyto: " + str(npc.xp_reward) +
                " punktów doświadczenia!")
            pause()
            # xp points reward for completion quest:
            hero.actualExp += npc.xp_reward
            items_dict = {}  # create empty dict used below:
            # check if quest condition is related
            # with handing out items (to npc):
            if len(npc.quest_items) > 0:
                # give items to npc
                # (result is items_dict winth negative values)
                items_dict = npc.quest_items
            # if there is extra reward: recieve items from npc inventory:
            add_remove_items_dict = mod_hero.dict_update(
                items_dict, add_remove_items_dict=npc.inventory_dict
                )

            # check if it is some items to remove or add to hero inventory
            if len(add_remove_items_dict) > 0:
                # update inventory:
                mod_hero.inventory_update(hero, add_remove_items_dict)
                # display result:
                display_looted_items(add_remove_items_dict)

    # check if there is special reward for quest:
    # teleport to next level (map),
    # display info about opened portal:
    mod_event.check_if_portal(hero, npc=npc)
    display_info_about_next_map_portal(hero=hero)

    return hero


def display_next_level_promotion(hero):
    '''
    display hero attributes for lvl promotion function
    '''
    # display hero attributes
    for number, (key, value) in enumerate(hero.attrib_dict.items()):
        print(
            str(number+1).ljust(0)+':', key.ljust(0),
            '(aktualna wartość: '+str(value).ljust(0)+')')
    #  player decide, which attribute to increase:
    player_choice = input(
        "\nAwans! Otrzymujesz punkt rozwoju, wybierz numer atrybutu,\
        który chcesz podnieść i zatwierdź <enter>: ")
    display_hyphen_multiply(multiplier=82)

    while True:
        try:
            int(player_choice) in range(1, 5)
            break

        except:
            player_choice = input("podaj numer atrybutu.. ")

    return player_choice


def display_info_about_next_map_portal(hero):
    '''
    check if hero has opened portal to next level
    (success in quest or fight with special enemy)
    display info about portal
    '''
    if hero.location != hero.new_location:
        print(
            '\n\n'+hero.name +
            ", udało Ci się, wkrótce wkroczysz do następnej krainy!\n"
            )


def display_text_from_file(filename=None, color=None):
    '''
    import text from text file, display it
    additional feature is text coloring (if color != None) 
    '''
    # opens file, import data in string format:
    try:
        imported_file = open(filename, encoding="utf-8")
        text_from_file = imported_file.read()
        imported_file.close()
        if color is None:  # color feature not implemented yet
            print('\n'+text_from_file)
            # color feature not implemented yet

    except:
        print('file not found:', filename)


def display_help_chart():
    '''
    work in progress
    '''
    pass






    








    

 