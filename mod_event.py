# mod event contains event functions
#!/usr/bin/python3

import time, random, os, math
import mod_hero, mod_enemy, mod_items, mod_display
from mod_display import dot_loop, pause, clear_screen



def priority_test(enemy = None, hero = None):
    '''
    who's attacker, who's defender
    '''
    clear_screen()
    mod_display.display_enemy_vs_hero(enemy = enemy, hero = hero, attacker = None)
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
    clear_screen()

    return attacker


def win_fight(enemy = None, hero = None):
    print("Zwycięstwo,", enemy.name, "został pokonany! Sława i doświadczenie są Twoje, ...a może jeszcze jakiś łup bitewny?")
    if len(enemy.treasure_dict) > 0: # check if there are some treasures in enemy inventory
        mod_display.dot_loop()
        time.sleep(1)
        print("\nTak!\n")
        add_remove_items_dict = enemy.treasure_dict
        mod_display.display_looted_items(add_remove_items_dict) # display treasures from enemy inventory
        mod_hero.inventory_update(hero, add_remove_items_dict)

    clear_screen()
    print("Może coś jeszcze?", end=''), dot_loop()
    pause()
    # and some random generated items:
    mod_items.treasure_generator(maxloops = enemy.maxdrop, maxitem_lvl = enemy.maxdrop_lvl, item_gen = None, hero = hero)
    mod_display.display_hero_chart(hero=hero)
    pause()
    return hero

def rip(enemy = None, hero = None):
    print("Po heroicznej walce świat zapłakał,", enemy.name, "zabił bohatera o imieniu", hero.name+". RIP,", hero.name+"!")
    mod_display.display_hero_chart(hero = hero)
    pause()
    clear_screen()
    mod_display.game_over(hero = hero)

def counterattack(enemy = None, hero = None, attacker = None, attack = None):
    '''
    part of the fight mechanic (part of fight function) 
    '''
    mod_display.display_enemy_vs_hero(enemy = enemy, hero = hero, attacker = attacker)
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

def event_fight_spec_enemy(enemy = None, hero = None):
    '''
    event == fight with random enemy
    '''
    # random generate enemy (using filters):
    enemy = mod_enemy.enemy_settings(name = enemy, loc = None, lvl = None, gen = None)
    enemy.attack = mod_enemy.attack_points_calc(enemy = enemy)
    enemy.defend = mod_enemy.defend_points_calc(enemy = enemy)
    mod_enemy.combat_attribute_default(enemy = enemy)
    enemy.combat_attribute = mod_enemy.combat_attribute_default(enemy = enemy)
    # update hero attrinute:
    mod_hero.combat_attribute_default(hero = hero)
    print("\n\nZaraz, zaraz... Coś się dzieje!\n"), time.sleep(.3)
    print("Twój przeciwnik to", end=''), dot_loop()
    
    print(' ',enemy.name.upper()+'!','\n')
    pause()
    clear_screen()
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
            mod_display.display_enemy_vs_hero(enemy = enemy, hero = hero, attacker = attacker)
            attacker_change = fight(enemy = enemy, hero = hero, attacker = attacker)
            pause()
            clear_screen()
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



def event_fight(enemy = None, hero = None):
    '''
    event == fight with random enemy
    '''
    # random generate enemy (using filters):
    enemy = mod_enemy.enemy_settings(name = None, loc = hero.location, lvl = None, gen = None)
    enemy.attack = mod_enemy.attack_points_calc(enemy = enemy)
    enemy.defend = mod_enemy.defend_points_calc(enemy = enemy)
    mod_enemy.combat_attribute_default(enemy = enemy)
    enemy.combat_attribute = mod_enemy.combat_attribute_default(enemy = enemy)
    # update hero attrinute:
    mod_hero.combat_attribute_default(hero = hero)
    print("\n\nZaraz, zaraz... Coś się dzieje!\n"), time.sleep(.3)
    print("Twój przeciwnik to", end=''), dot_loop()
    
    print(' ',enemy.name.upper()+'!','\n')
    pause()
    clear_screen()
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
            mod_display.display_enemy_vs_hero(enemy = enemy, hero = hero, attacker = attacker)
            attacker_change = fight(enemy = enemy, hero = hero, attacker = attacker)
            pause()
            clear_screen()
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
    p = 1
    while p < 3:
        mod_display.display_hero_chart(hero = hero)
        event = input("Jeśli chcesz walki, napisz: walka lub  po prostu naciśnij 'enter', żeby polosować itemy do ekwipunku ")
        if event == "walka":
            mod_display.display_varied_info()    
            # załóżmy, że wylosowany został event z przeciwnikiem:
            event_fight(enemy = None, hero = hero)
            
        else:
            print("No to pogenerujemy przemioty dla zabawy...")
            # mamy mało itemów, więc filtry wyłączyłem
            mod_items.treasure_generator(maxloops = 20, maxitem_lvl = None, item_gen = None, hero = hero)
        p += 1
    
    
    return hero.inventory_dict
