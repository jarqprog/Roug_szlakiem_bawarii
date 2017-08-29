
# mod_varied_info - custom mod, contains enemy data
# function enemy_settings(name = None, loc = None, lvl = None, gen = None) load specified or random oponent to main

import random

################################ Hero's enemies class:
class Enemy:
   def __init__(self, name, life, level, xp4hero, genre, location, attrib_dict, treasure_dict, specials_list, speach_list):
        self.name = name
        self.life = life
        self.level = level
        self.xp4hero = xp4hero
        self.genre = genre
        self.location = location
        self.attrib_dict = attrib_dict
        self.treasure_dict = treasure_dict
        self.specials_list = specials_list
        self.speach_list = speach_list

        # ww. "location" przyjmuje wartość elementów listy (element = lvl mapy)
        # ...w ten sposób decydujemy, czy dany przeciwnik może się pojawić w danyn lvlu

        #Enemy.treasure_dict = {"pos1":i_e_d, "pos2":i_e_d, "pos3":i_e_d, "pos4":i_e_d,"pos5":i_e_d}

def enemy_settings(name = None, loc = None, lvl = None, gen = None):
    # we can do same staf with inventory items :)
    
    '''
    Stores enemies data base. 
    Creates enemy and export to MAIN using specific arguments:
    name = imports by name, for expample: if name = "wilk", function exports object WOLF
    or
    if name (in function arguments) is not specified, enemy is generates by filters:
        location (loc, ex. loc = 2 - second map level),
        enemy level (lvl = 1,2,3...),
        genre (gen, ex. gen = "animal": it will choose between enemies with genre = "animal")
        then export to main 
    '''

    attrib_dict = {} # pusty słownik dla atrybutów przeciwników
    treasure_dict = {} # pusty słownik z miejscem na przedmioty u przeciwników (można to wykorzystać m.in. do "losowania łupu")
    specials_list = [] # pusty słownik z miejscem na cechy specjalne (możemy je wyświetlać w trakcie walki) - domyślnie pusta
    speach_list = [] # zawiera kwestie wypowiadane przez przeciwnika w czasie walki (możemy je losować :) ) - domyślnie pusta

    # data in (...) are enemy:
    # name, life, level, xp4hero, genre, location (list), attrib_dict, treasure_dict, specials_list, speach_list

    #   Wilk
    wolf = Enemy(u"wilk",10, 1, 5, "animal", [1,2,3], attrib_dict, treasure_dict, specials_list, speach_list)
    wolf.attrib_dict = {u"atak":1,"obrona":1, "zwinność":3, "percepcja":3, "inteligencja":1, "siła woli":1, "obrażenia":[1,3]}
    wolf.speach_list = [u"wrrrr"]

    # Goblin
    goblin = Enemy(u"goblin",20, 1, 7, "beast", [1,2,3], attrib_dict, treasure_dict, specials_list, speach_list)
    goblin.attrib_dict = {u"atak":1,"obrona":1, "zwinność":2, "percepcja":2, "inteligencja":1, "siła woli":1, "obrażenia":[1,4]}
    goblin.speach_list = [u"Ja ubić ludzia!", "Ty trup!"]

     # Skurczybyk
    skurczybyk = Enemy(u"skurczybyk",30, 2, 10, "human", [1,2], attrib_dict, treasure_dict, specials_list, speach_list)
    skurczybyk.attrib_dict = {u"atak":2,"obrona":1, "zwinność":2, "percepcja":2, "inteligencja":1, "siła woli":1, "obrażenia":[1,5]}
    skurczybyk.speach_list = [u"Ah, co tam masz w sakiewce?", "Złoto albo śmierć!"]
    skurczybyk.treasure_dict = {u"złoto":random.randint(1,30), "pierścień skurczybyka":1, "nóż":1} # ring for optional quest
    skurczybyk.speach_list = [u"Co tam masz w sakiewce?", "Złoto albo śmierć!", "Kto zadziera ze skurczybykiem, ten frajer!"]
    skurczybyk.specials_list = [u"Straszna menda"]



    #   Miś
    bear = Enemy(u"niedźwiedź",30, 2, 12, "animal", [1,2,3], attrib_dict, treasure_dict, specials_list, speach_list)
    bear.attrib_dict = {u"atak":2,"obrona":2, "zwinność":1, "percepcja":1, "inteligencja":1, "siła woli":1, "obrażenia":[1,4]}
    bear.speach_list = [u"Mrrrrr!", "Wrrrrrr!", "Rgh!"]

    #   Troll (strong opponent)
    troll = Enemy(u"troll", 75, 3, 50, "beast", [2, 3, 4], attrib_dict, treasure_dict, specials_list, speach_list)
    troll.attrib_dict = {u"atak":3,"obrona":4, "zwinność":1, "percepcja":1, "inteligencja":1, "siła woli":2, "obrażenia":[3,6]}
    troll.treasure_dict = {u"złoto":random.randint(1,100), "rubiny":random.randint(0,12)}
    troll.speach_list = [u"U mnie głód! Ty smakowite!", "Ty grube!", "Ty ładne i smaczne!", "Argh!"]
    troll.specials_list = [u"Kamienna skóra", "Niezdara", "Okrótna siła"]

    #   Olbrzym górski
    mountain_giant = Enemy(u"olbrzym górski", 99, 4, 65, "beast", [3, 4], attrib_dict, treasure_dict, specials_list, speach_list)
    mountain_giant.attrib_dict = {u"atak":2,"obrona":2, "zwinność":1, "percepcja":1, "inteligencja":1, "siła woli":2, "obrażenia":[4,8]}
    mountain_giant.treasure_dict = {u"złoto":random.randint(1,100), "diamenty":random.randint(1,3), "olbrzymia maczuga": 1}
    mountain_giant.speach_list = [u"Ty chcieć mi odebrać błyszczące?!", "Twój czerep nada się na ząb!", "(straszny ryk)", "Gnieść, łupić!"]
    mountain_giant.specials_list = [u"Olbrzymia wytrzymałość", "Okrótna siła"]



    #################################### quest/special enemies: - special monsters has Capitalic in names (Zły Miś, Głupi Jaś) 

    #   Zły miś (QUEST in lvl 1)
    bear_special_quest = Enemy("Zły Miś",30, 2, 40, "animal, special" , [2], attrib_dict, treasure_dict, specials_list, speach_list)
    bear_special_quest.attrib_dict = {"atak":3,"obrona":4, "zwinność":1, "percepcja":1, "inteligencja":2, "siła woli":2, "obrażenia":[1,4]}
    bear_special_quest.treasure_dict = {"liczydło":1, "lina pomiarowa":1}
    bear_special_quest.speach_list = [u"Ten gupi myśliwy Cię przysłał? Figa, niczego Ci nie dam!"]
    bear_special_quest.specials_list = [u"Ten miś mówi!", "Na szyi ma linę, a pod ogonem liczydło"]


############## list with all enemies - we use this in functions below:
    # na razie potrzeba ręcznie dopisywać każdego przeciwnika, ale to raczej nie problem
    # mogę po każdym przeciwniku robić list.append, ale nie ma tego tak dużo, żeby kompa obciążać ;)
    enemies_all_list = [wolf, goblin, skurczybyk, bear, bear_special_quest, troll, mountain_giant]


    # if enemy name was specified, it will export enemy by given name:
    enemy_exported_to_main = ''
    if name != None:
        
        for element in enemies_all_list:
            if element.name == name:
                enemy_exported_to_main = element

        return enemy_exported_to_main


    # if enemy name wasn't specified, it will export random enemy (random using optional filters - level, location, genre):
    else:
        enemy_random_list = [] # temporary helper list
        for element in enemies_all_list:        
            if (loc in element.location or loc == None) and (lvl == element.level or lvl == None) and (gen == element.genre or gen == None):
                enemy_random_list.append(element)
        

        # export random enemy to main function:
        enemy_rnd_exported_to_main = enemy_random_list[random.randint(0, len(enemy_random_list)-1)]
        
        return enemy_rnd_exported_to_main
        # loc = None, lvl = None, gen = None


    #   # name, life, level, attrib_dict, treasure_dict, genre, xp4hero, specials, speach, location
    #wolf = Enemy("wilk",10, 1, attrib_dict,treasure_dict,"animal",5,None,"Wrrrrr!",