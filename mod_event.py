# mod event contains event functions
# !/usr/bin/python3

import time
import random
import os
import math

# custom modules:
import mod_hero
import mod_enemy
import mod_items
import mod_display
import mod_npc


def priority_test(enemy=None, hero=None):
    '''
    who's attacker, who's defender
    '''
    mod_display.clear_screen()
    mod_display.display_enemy_vs_hero(enemy=enemy, hero=hero, attacker=None)
    # zwinność, percepcja i inteligencja have influence on this test:
    hero_test_stats = (
        int(hero.attrib_dict["zwinność"])
        + int(hero.attrib_dict["percepcja"])
        + int(hero.attrib_dict["inteligencja"]))
    enem_test_stats = (
        int(enemy.attrib_dict["zwinność"])
        + int(enemy.attrib_dict["percepcja"])
        + int(enemy.attrib_dict["inteligencja"]))
    print("\nKto uzyskał inicjatywę? (test inicjatywy)\n")

    while True:
        test_var1 = hero_test_stats + enem_test_stats
        test_var2 = random.randint(1, test_var1)      
        print('\r\r'+hero.name+":", hero_test_stats)
        print('\r\r'+enemy.name+":", test_var2)
        if hero_test_stats > test_var2:
            print("\nRezultat:", end=''), mod_display.dot_loop()
            print("\n\natakuje", hero.name+'!')
            attacker = hero
            break
          
        elif hero_test_stats < test_var2:
            print("\nRezultat:", end=''), mod_display.dot_loop()
            print("\n\natakuje", enemy.name+'!')
            attacker = enemy
            break

    mod_display.pause()
    mod_display.clear_screen()

    return attacker


def win_fight(enemy=None, hero=None):
    print(
        "Zwycięstwo,", enemy.name,
        "został pokonany! Sława i doświadczenie są Twoje,\
        \n...a może jeszcze jakiś łup bitewny?")

    # check if there are some treasures in enemy inventory:
    if len(enemy.treasure_dict) > 0:
        mod_display.pause()
        print("\nTak!\n")
        add_remove_items_dict = enemy.treasure_dict
        # display treasures from enemy inventory:
        mod_display.display_looted_items(add_remove_items_dict)
        mod_hero.inventory_update(hero, add_remove_items_dict)
        mod_display.pause()
    mod_display.clear_screen()
    print("Może coś jeszcze?", end=''), mod_display.dot_loop()
    looted_gold = mod_enemy.enemy_gold_reward(enemy)
    if looted_gold > 0:
        print("\n\nzdobyto", looted_gold, "sztuk złota\n")
        hero.gold += looted_gold
        mod_display.pause()
    time.sleep(.3)
    # and some random generated items:
    mod_items.treasure_generator(
        maxloops=enemy.maxdrop, maxitem_lvl=enemy.maxdrop_lvl,
        item_gen=None, hero=hero
        )
    mod_display.display_info_about_next_map_portal(hero=hero)

    return hero


def counterattack(enemy=None, hero=None, attacker=None, attack=None):
    '''
    part of the fight mechanic (part of fight function) 
    '''
    mod_display.display_enemy_vs_hero(
        enemy=enemy, hero=hero, attacker=attacker
        )
    # attacker = priority_test(enemy = enemy, hero=hero) 
    # define attacker and defender:
    if attacker == hero:
        defender = enemy
    elif attacker == enemy:
        defender = hero

    print("\nkontratak!", end='')
    mod_display.dot_loop()
    counterattack_result = 0
    print(
        '\n'+defender.name, " kontratakuje: rzuca",
        str(defender.attrib_dict[str(defender.combat_attribute)]),
        "razy kością K4:"
        )
    damage = random.randint(defender.dmg_list[0], defender.dmg_list[1])
    for i in range(int(defender.attrib_dict[str(defender.combat_attribute)])):
        counterattack_var = random.randint(1, 4)
        print(
            (str(counterattack_var)), "      ", sep='', end='', flush=True
            ), time.sleep(0.3)
        counterattack_result += counterattack_var
    print("\n\nRezultat:", end=''), mod_display.dot_loop()
    print(
        '\n\n'+defender.name+':', counterattack_result, '+',
        defender.attack, "(atak):", counterattack_result
        + defender.attack
        )
    print(attacker.name+':', attack), time.sleep(0.3)
    if attack < counterattack_result+defender.attack:
        if damage > attacker.actualLife:
            damage = attacker.actualLife
        attacker.actualLife -= damage
        print(
            defender.name, "zadał obrażenia:", attacker.name,
            "stracił", damage, "pkt. życia"
            )
        time.sleep(0.3)
        if defender == hero:
            hero.actualExp += damage
            print(hero.name+", zdobyto doświadczenie:", damage)
            
            return hero.actualExp

        if defender.actualLife < 0:
            defender.actualLife = 0
            combat_end = 1  # break fight loop

            return combat_end

    else:
        print('\n'+attacker.name, "obronił się!")
        attacker_change = 1

        return attacker_change
            

def fight(enemy=None, hero=None, attacker=None):
    '''
    fight mechanic = hit
    '''

    # define attacker and defender:
    if attacker == hero:
        defender = enemy
    elif attacker == enemy:
        defender = hero 

    attacker_change = 0

    attack_result = 0
    defend_result = 0
    print(
        '\n'+attacker.name, "atakuje: rzuca",
        attacker.attrib_dict[str(attacker.combat_attribute)],
        "razy kością K4:"
        )
    for i in range(int(attacker.attrib_dict[str(attacker.combat_attribute)])):
        attack_var = random.randint(1, 4)
        print(
            (str(attack_var)), "      ", sep='', end='', flush=True
            ), time.sleep(0.3)
        attack_result += attack_var
    time.sleep(0.3)
    print(
        '\n'+defender.name, "broni się: rzuca",
        str(defender.attrib_dict["zwinność"]), "razy kością K4:"
        )
    for i in range(int(defender.attrib_dict["zwinność"])):
        defend_var = random.randint(1, 4)
        print(
            (str(attack_var)), "      ", sep='', end='', flush=True
            ), time.sleep(0.3)
        defend_result += defend_var
        
    print("\n\nRezultat:", end=''), mod_display.dot_loop()
    print(
        '\n\n'+attacker.name+':', attack_result, '+',
        attacker.attack, "(atak):", attack_result+attacker.attack
        )
    print(
        defender.name+':', defend_result, '+',
        defender.defend, "(obrona):", defend_result+defender.defend
        )
    if attack_result+attacker.attack <= defend_result+defender.defend:
        print('\n'+defender.name, "obronił się!")
        mod_display.pause()
        attacker_change = 1
        attack = int(attack_result+attacker.attack)
        counterattack(enemy=enemy, hero=hero, attacker=attacker, attack=attack)

        return attacker_change

    else:
        damage = random.randint(attacker.dmg_list[0], attacker.dmg_list[1])
        if damage > defender.actualLife:
            damage = defender.actualLife
        print(
            '\n'+attacker.name, "zadał obrażenia:",
            defender.name, "stracił", damage, "pkt. życia"
            )
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


def event_fight_spec_enemy(enemy=None, hero=None):
    '''
    event == fight with special (quest) enemy
    '''

    # random generate enemy (using filters):
    enemy = mod_enemy.enemy_settings(name=enemy, loc=None, lvl=None, gen=None)
    if enemy.name not in hero.enemy_killed:
        enemy.attack = mod_enemy.attack_points_calc(enemy=enemy)
        enemy.defend = mod_enemy.defend_points_calc(enemy=enemy)
        mod_enemy.combat_attribute_default(enemy=enemy)
        enemy.combat_attribute = mod_enemy.combat_attribute_default(
            enemy=enemy
            )
        # update hero attribute:
        mod_hero.combat_attribute_default(hero=hero)
        mod_hero.attack_points_calc(hero)
        mod_hero.defend_points_calc(hero)
        print("\n\nZaraz, zaraz... Coś się dzieje!\n"), time.sleep(.3)
        print(
            "Szykuj się do walki. Twój przeciwnik to", end=''
            ), mod_display.dot_loop()
        
        print(' ', enemy.name.upper()+'!', '\n')
        mod_display.pause()
        mod_display.clear_screen()
        # fight loop:
        combat_end = 0
        while (
            combat_end == 0 and hero.actualLife > 0
            and enemy.actualLife > 0
            ):
            # initiative test:
            attacker = priority_test(enemy=enemy, hero=hero)
            # define attacker and defender:
            if attacker == hero:
                defender = enemy
            elif attacker == enemy:
                defender = hero

            # if attacker_change == 1:
            # loop is break and repeat initiative test  
            attacker_change = 0
            while True:
                mod_display.display_enemy_vs_hero(
                    enemy=enemy, hero=hero, attacker=attacker
                    )
                attacker_change = fight(
                    enemy=enemy, hero=hero, attacker=attacker
                    )
                mod_display.pause()
                mod_display.clear_screen()
                if hero.actualLife < 1:
                    hero.actualLife = 0
                    combat_end = 1
                    break 
                    
                elif enemy.actualLife < 1:
                    # enemy is dead:
                    enemy.actualLife = 0
                    hero.quest_condition_list.append(enemy.quest_condition)
                    if enemy.genre == "quest":  # quest enemies are unique
                        hero.enemy_killed.append(enemy.name)  # block enemy for future
                    # if it is quest enemy (is either enemy and quest npc):
                    try:
                        # import npc by enemy name (if it is quest enemy):
                        npc = mod_npc.npc_settings(
                            name=enemy.name, loc=None, gen=None
                            )
                        # info in hero attribute, that quest is completed:
                        hero.quest_completed_list.append(npc.quest_name)
                        # update quest info to display:
                        if npc.quest_name not in hero.quest_info.keys():
                            hero.quest_info.update(
                                {npc.quest_name: [enemy.quest_info]}
                                ) 
                        else:
                            hero.quest_info[npc.quest_name][0] += (
                                '\n'+str(enemy.quest_info))
                        # check if there is special reward for quest
                        # (teleport to next level (map))
                        # if True: return updated hero.new_location
                        # (signal to display info about portal)
                        check_if_portal(hero=hero, npc=npc)
                    except:
                        pass  # I just want to ignore potential error

                    if enemy.quest_info:
                        print(enemy.quest_info)  # display statment about quest (element of enemy quest list) 

                    win_fight(enemy, hero)
                    combat_end = 1  # combat_end == 1: break fight loop              
                    break

                elif attacker_change == 1:
                    break

    return hero


def event_fight(enemy=None, hero=None):
    '''
    event == fight with random enemy
    '''
    # random generate enemy (using filters):
    enemy = mod_enemy.enemy_settings(
        name=None, loc=hero.location, lvl=None, gen=None
        )
    enemy.attack = mod_enemy.attack_points_calc(enemy=enemy)
    enemy.defend = mod_enemy.defend_points_calc(enemy=enemy)
    mod_enemy.combat_attribute_default(enemy=enemy)
    enemy.combat_attribute = mod_enemy.combat_attribute_default(enemy=enemy)
    # update hero attrinute:
    mod_hero.combat_attribute_default(hero=hero)
    mod_hero.attack_points_calc(hero)
    mod_hero.defend_points_calc(hero)
    print("\n\nZaraz, zaraz... Coś się dzieje!\n"), time.sleep(.3)
    print("Twój przeciwnik to", end=''), mod_display.dot_loop()
    print(' ', enemy.name.upper()+'!', '\n')
    mod_display.pause()
    mod_display.clear_screen()
    # pętla walki:
    combat_end = 0
    while combat_end == 0 and hero.actualLife > 0 and enemy.actualLife > 0:
        # initiative test:
        attacker = priority_test(enemy=enemy, hero=hero)
        # define attacker and defender:
        if attacker == hero:
            defender = enemy
        elif attacker == enemy:
            defender = hero
        attacker_change = 0
        # if attacker_change == 1,
        # loop is break and we repeat initiative test

        while True:
            mod_display.display_enemy_vs_hero(
                enemy=enemy, hero=hero, attacker=attacker
                )
            attacker_change = fight(enemy=enemy, hero=hero, attacker=attacker)
            mod_display.pause()
            mod_display.clear_screen()
            if hero.actualLife < 1:
                combat_end = 1
                hero.actualLife = 0
                break
            
            elif enemy.actualLife < 1:
                win_fight(enemy=enemy, hero=hero)
                combat_end = 1
                break

            elif attacker_change == 1:
                break
    
    return hero


def event_quest(npc=None, hero=None):
    '''
    event == quest adventure
    it is regular advenure: meet quest npc, displays info about meeting
    '''
    # import (by name) npc data from class npc (mod_npc):
    npc = mod_npc.npc_settings(name=npc, loc=None, gen=None)
    # check if hero has items to finish quest (if it is quest condition):
    mod_hero.check_item_condition_quest(hero=hero, npc=npc)
    # prepare quest npc statement lists (blocked or not?):
    mod_hero.quest(hero=hero, npc=npc)
    # display event:
    mod_display.display_event_quest(hero=hero, npc=npc)

    return hero


def event_npc(npc=None, hero=None):
    '''
    event == meet specified (by name) NPC
    '''
    # summon npc by name:
    npc = mod_npc.npc_settings(name=npc.name, loc=None, gen=None)


def event_question_mark(hero):
    '''
    event == random event when hero on '?' mark on the map
    small chance to win gold, huge chance to fight with random enemy
    '''
    print("\n\nOtwierasz puszczkę Pandory.. Czy Ci się udało?..\n")
    mod_display.pause()
    chance_factor = random.randint(1, 100)
    if chance_factor < 90:
        enemy = mod_enemy.enemy_settings(
            name=None, loc=hero.location, lvl=None, gen=None
            )
        event_fight(enemy=enemy, hero=hero)

    else:
        # looted gold depends on luck, hero level and hero location
        # (higher level, higher location number == more gold to gain)
        looted_gold = random.randint(5, 50)*hero.level*hero.location
        print(
            '\n\n'+hero.name+", udało Ci się! Zdobywasz:",
            looted_gold, "sztuk złota\n"
            )
        mod_display.pause()
   
    return hero
          

def event_random_npc(hero):
    '''
    event == meet random (from hero location) NPC
    call display function to show npc's random statement 
    '''
    # random generate npc (using filters):
    try:
        npc = mod_npc.npc_settings(name=None, loc=hero.location, gen=None)
        mod_display.display_NPC_random_speach(npc=npc)

    except:
        pass  # wonna ignore info about error


def quest_neutral_hostile_npc(hero=None, npc_name=None):
    '''
    event with npc, which can turn into enemy
    during the second meeting
    if hero doesn't fulfill quest condition
    '''
    # first check if NPC not dead already:
    if npc_name not in hero.enemy_killed:
        # check if hero has met npc before, import npc by name:
        npc = mod_npc.npc_settings(name=npc_name, loc=None, gen=None)
        print(npc.quest_items)
        # if hero has npc statement in quest_blocked_list
        # (which stores heard npc statement)..
        # means that hero has met npc before
        if npc.quest_list[0] in hero.quest_blocked_list:
            # check if hero has items to finish quest
            # (if it is quest condition):
            mod_hero.check_item_condition_quest(hero=hero, npc=npc)
            # second meeting without quest condition fulfilled means that
            # NPC transform to enemy:
            if npc.quest_condition not in hero.quest_condition_list:
                # call fight function
                event_fight_spec_enemy(enemy=npc_name, hero=hero)

            # second meeting with npc, but hero..
            # has fulfilled quest condition
            # npc is friendly/neutral:
            else:
                event_quest(npc=npc_name, hero=hero)
                mod_display.pause()

        # it is first meeting with npc, NPC is neutral:
        else:
            event_quest(npc=npc_name, hero=hero)
            mod_display.pause()


def event_well_of_life(hero=None):
    '''
    full life regeneration event (healer)
    '''
    # price is 1 gold for every 1 life point to recover
    price = hero.maxLife - hero.actualLife
    print("Witaj,", hero.name+", jestem uzdrowicielem.")
    if hero.actualLife == hero.maxLife:  # ckeck if hero need 'health care'
        print(
            "\nWidzę, że nie potrzebujesz leczenia! Nie trwoń mojego czasu.."
            )
        mod_display.pause()
    else:
        print("\n\nZa cenę", price, "sztuk złota w pełni Cię uleczę.. ")

        if hero.gold >= price:
            while True:
                player_choice = input(
                    "Jeśli chcesz skorzystać, wpisz 't',\
                    \njeśli nie, wpisz 'n' i zatwierdź <enter> -->"
                    )

                try:
                    if player_choice == 't' or player_choice == 'n':
                        if player_choice == 't':
                            print("Uzupełniono życie!")
                            hero.actualLife = hero.maxLife
                            hero.gold -= price
                            mod_display.pause()
                        elif player_choice == 'n':
                            print("Bywaj zatem!")
                            mod_display.pause()
                        break

                except:
                    pass  # just wonna ignore error

        else:
            print("\n\nNie posiadasz wystarczającej ilości złota..\n")
            mod_display.pause()

        return hero


def event_shop(hero):
    '''
    shop event - display shop, selling and buying
    '''
    # shop items to buy (dict type)
    items_to_buy = mod_items.item_dict_generator(hero, level=None)
    user_choice = ''
    # shop loop, display shop and hero assortment:
    while user_choice != 'W':
        items_to_buy = mod_display.display_shop(hero, items_to_buy)
        user_choice = mod_display.display_player_choice_shop(
            hero, items_to_buy
            )
        if user_choice == 'W':  # quit from shop
            break
        elif user_choice == '1':  # buy option
            user_choice = mod_display.shop_hero_buy(hero, items_to_buy)        
        else:  # sell option
            user_choice = mod_display.shop_hero_sell(hero)
    
    print('')  # empty line (for estetic reason)

    return hero


def check_if_portal(hero=None, npc=None):
    '''
    check if npc or special enemy has attribute
    that opens portal to next location (game map)  
    '''
    if npc.quest_name in hero.quest_completed_list:  # if quest is completed
        # "portal #..." is special reward for quest,
        # it is teleport to nex level (map):
        if "portal 2" in npc.quest_special_reward:
            hero.new_location = 2
        elif "portal 3" in npc.quest_special_reward:
            hero.new_location = 3
        elif "portal 4" in npc.quest_special_reward:
            hero.new_location = 4

    return hero
