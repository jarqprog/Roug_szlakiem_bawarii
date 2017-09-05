# Szlakiem Bawarii - plik roboczy Jarka
#!/usr/bin/python3
import os, time, random, math
#from msvcrt import getch

# custom modules:
import mod_display, mod_event, mod_npc
from mod_display import clear_screen, dot_loop, pause
import mod_enemy
import mod_hero 
import mod_items
import mod_save_load




def main():
    clear_screen()
    # set basic variables:
    game_lvl = 1
    add_remove_items_dict = {}

    ######################## HERO CLASS IMPORT TO MAIN: 
    hero = mod_hero.hero_settings()
    hero.attack = mod_hero.attack_points_calc(hero = hero)
    hero.defend = mod_hero.defend_points_calc(hero = hero)
    mod_hero.combat_attribute_default(hero = hero)


    hero.max_armour = mod_hero.amour_max_calc(hero = hero)
    hero.calendar_list = [0, "niedziela", "wieczór"] 



    ### here we can add next hero methods...

    ######################## ENEMY CLASS IMPORT TO MAIN:
    enemy = mod_enemy.enemy_settings(name = None, loc = None, lvl = None, gen = None)
    enemy.attack = mod_enemy.attack_points_calc(enemy = enemy)
    enemy.defend = mod_enemy.defend_points_calc(enemy = enemy)
    enemy.combat_attribute = mod_enemy.combat_attribute_default(enemy = enemy)
    ### here we can add next enemy methods...


    ######################## NPC CLASS IMPORT TO MAIN:
    npc = mod_npc.npc_settings(name = None, loc = None, gen = None)
    enemy.attack = mod_enemy.attack_points_calc(enemy = enemy)
    enemy.defend = mod_enemy.defend_points_calc(enemy = enemy)
    enemy.combat_attribute = mod_enemy.combat_attribute_default(enemy = enemy)







################ TU URUCHAMIAMY FUNKCJE:
    #intro() # tytuł, powitanie, wybór:

    ####### ładowanie gry LUB tworzenie bohatera LUB galeria sław LUB info o nas
    ####### po każdej z tych funkcji odpalamy główną pętlę:

    # ----- tu będzie funkcja do wyświetlania mapy
    hero.attrib_dict = {"siła":4, "zwinność":4, "percepcja":2, "inteligencja":2, "siła woli":1}
    hero.name = "Dobrosław z Legnicy"
    hero.inventory_dict = {"miecz":1}
    hero.dmg_list = [18,20]

####################### MAIN LOOP:
    while True:
        clear_screen()
        mod_display.display_calendar_location(hero = hero) # display short random info :)
        mod_event.event_quest(npc = "Czerwony Kapturek", hero = hero)
        #npc = mod_npc.npc_settings(name = "Czerwony Kapturek", loc = None, gen = None)
        pause()
        mod_display.display_hero_chart(hero)
        pause()
        mod_event.event_fight_spec_enemy(enemy = "Zły Wilk", hero = hero)
        pause()
        mod_display.display_calendar_location(hero = hero)
        mod_event.event_quest(npc = "Czerwony Kapturek", hero = hero)
        pause()










main()



# na koniec głóœnej pętli:
# hero.life_recovery hero.actualLife - odzyskanie życia!
# hero.turn_counter = +1
# zrób przedmioty zaślepki - żeby nie było bugów przy losowaniu :)