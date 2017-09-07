
# mod_npc - custom mod, contains npc / quest data
# function npc_settings(name = None, loc = None, lvl = None, gen = None) load specified or random oponent to main

import random, mod_hero, mod_items

################################ NPC class:
class Npc:
   def __init__(self, name, location_list):
        self.name = name
        self.location_list = location_list
        self.inventory_dict = {}
        self.speach_list = []
        ###
        self.map_symbol = ""
        self.shop = None # if true - it's a shop keeper with buy/sell option
        self.npc_quest_list = []
        self.xp_reward = 0
        self.quest_name = ""
        self.quest_condition = ""
        self.quest_special_reward = ""

     

def npc_settings(name = None, loc = None, gen = None):
    '''
    Stores NPC data base. 
    Creates NPC and export to MAIN using specific arguments:
    name = imports by name, for expample: if name = "wilk", function exports object WOLF
    or
    if name (in function arguments) is not specified, enemy is generated by filters:
        location (loc, ex. loc = 2 - second map level),
        enemy level (lvl = 1,2,3...),
        genre (gen, ex. gen = "animal": it will choose between enemies with genre = "animal")
        then export to main 
    '''

    treasure_dict = {} # contains items, that can be gift to hero
    speach_list = [] # contains statments, that can be delivered to hero (if they ar not on hero speach_blocked_list)




############################# REGULAR NPC
    # data in (...) are npc:
    # name, life, level, xp4hero, genre, location (list), attrib_dict, treasure_dict, specials_list, speach_list

    #   wieśniak (name, location_list, inventory_dict, speach_list)
    villager = Npc("wieśniak", [1])
    villager.speach_list = ["Jak się masz?", "Dużo roboty", "Stara mnie pogoniła", "Ide po cebule", "bry, bry",
    "słyszałem o niedźwiedziu, który kradnie rzeczy", "uważaj na wilki i gobliny",
    "podobno leśniczego okradli" ]
    villager.map_symbol = "V"

    villager1 = Npc("garbaty wieśniak", [1]) ############ to do
    villager.speach_list = ["Cieżkie życie!", "Dużo roboty", "Stara mnie pogoniła", "Ide po cebule", "bry, bry",
    "słyszałem o niedźwiedziu, który kradnie rzeczy", "uważaj na wilki i gobliny",
    "podobno leśniczego okradli" ]

    mushrooman = Npc("grzybiarz", [1])
    mushrooman.speach_list = ["Grzybów mało w tym roku", "Znów robaczywe", "Patrz, jaki borowik!",
    "Poszedłbym głębiej w las, ale dużo niedźwiedzi", "Słyszałem, że leśniczy potrzebuje pomocy",
    "podobne gdzieś tu jest bestia, która gada", "strasznie tu czasem", "uważaj na wilki",
    "dużo tu szczurołaków", "podobno dziewczynka w czerwonym kapturze ma problem z babcią"]

    hans = Npc("Hans z wioski", [1])
    hans.speach_list = ["w sąsiedniej krainie moja wioska potrzebuje pomocy - hojnie nagrodzimy",
    "Słyszałem, że leśniczy potrzebuje pomocy", "ponoć jest tu obóz niesłusznie rozbitych",
    "podobne gdzieś tu jest bestia, która gada", "strasznie tu czasem", "uważaj na wilki",
    "dużo tu szczurołaków"]

    gretchel = Npc("Gretchel", [1])
    gretchel.speach_list = ["ładna jestem, co nie? Nie?! Twoja strata!", "(tupie nóżką)", "(puszcza oko)",
    "słyszałam o leśniczym, który potrzebuje pomocy..", "podobno dziewczynka w kapturze ma problem z babcią",
    "dużo tu szczurołaków"]

    
    wrongly_smashed = Npc("Niesłusznie rozbity", [1])
    wrongly_smashed.speach_list = ["Serwus, chodź do naszego obozu, mamy dobry miodzik", "Lecę, mamy dziś spotkanie! ", "Lepiej nam się ostatnio wiedzie! "]


    #   wieśniak (name, location_list, inventory_dict, speach_list)
    villager2 = Npc("wieśniak ze Szwarzwaldu", [2])
    villager.speach_list = ["Uważaj, niebezpiecznie tu!", "Przed nocą trzeba mi w dom..", "Stara mnie pogoniła", "Dużo tu grzybów i trolli..", "bry, bry",
    "Oblib.. nie wiem o nim.., ale kręcił się jakiś karzeł..", "uważaj na trolle!",
    "Moja wioska potrzebuje pomocy.." ]


    villager3 = Npc("wieśniak Hans", [2])
    villager.speach_list = ["Jak się masz?", "Dużo roboty", "Stara mnie pogoniła", "Ide po cebule", "bry, bry",
    "Oblib... tak, poszedł do Dymiącej góry..", "uważaj na wilki i gobliny",
    "Uważaj, przejścia do Dymiącej góry pilnuje straszny Troll Silnorękiego!" ]



    # npc_regular_list contains list with not quest npc to generate and export to main:
    npc_regular_list = [
    
    villager, mushrooman, hans, gretchel, wrongly_smashed, villager1, villager2, villager3

    ]

############################# QUEST NPC

    # Czerowny Kapturek
    redhood = Npc("Czerwony Kapturek", [1])
    redhood.speach_list = ["O, witaj! Co u Ciebie?", "Miło Cię widzieć!"]
    redhood.xp_reward = 50
    redhood.quest_name = "Ratuj Babcię"
    redhood.quest_list = [
        "Możesz mi pomóc? Babcię porwał wilk. Odszukaj go, zwróć Starowinkę, to będę Ci dozgonnie wdzięczna!",
        "Ojejku, jejku, Babcia uratowana! Dziękuję Ci! (całus) ",
        "No co tam?"       
        
    ]
    
    redhood.quest_condition = "Babcia uratowana"
    redhood.inventory_dict = {"diament":1}



    # Leśniczy
    forester = Npc("Leśniczy", [1])
    forester.speach_list = ["O, witaj!", "Miło Cię widzieć", "Co u Ciebie?", "Dużo mam pracy"]
    forester.xp_reward = 100
    forester.quest_name = "Narzędzia pomiarowe"
    forester.quest_list = [
        "Słyszałem o Tobie - może mi pomożesz... Złodziejski Miś ukradł mi narzędzia pomiarowe, nie mogę wykonać swojej pracy. Jeśli mi pomożesz, pokażę Ci drogę do nastęþnej krainy..",
        "Brawo, bardzo Ci dziękuję. Czas na Twoją nagrodę!"    
    ]
    
    forester.quest_condition = "Zdobyto narzędzia pomiarowe"
    forester.inventory_dict = {"diament":1, "liczydło":-1, "lina pomiarowa":-1}
    forester.quest_special_reward = ["portal 2"]


    # obóz Nieszłusznie rozbitych
    wrongly_smashed_camp = Npc
    wrongly_smashed_camp = Npc("Obóz niesłusznie rozbitych", [1])
    wrongly_smashed_camp.speach_list = ["No czołem, czołem!", "Co tam u Ciebie?", "Dobry miodzik mamy, co nie?"]
    wrongly_smashed_camp.xp_reward = 5
    wrongly_smashed_camp.quest_name = "Otrzymałem miodzik!"
    wrongly_smashed_camp.quest_condition = "Zdobyto miodzik"
    wrongly_smashed_camp.inventory_dict = {"miodzik":1}
    wrongly_smashed_camp.quest_list = [
        "Hihi, pewnie chcesz naszego miodzika? A proszę bardzo! ",
        "Więcej miodzika nie mamy.. "
    ]

    # Złodziejski miś
    thievish_bear_quest = Npc("Złodziejski Miś", [1])
    thievish_bear_quest.speach_list = [u"Ten gupi myśliwy Cię przysłał?"]
    thievish_bear_quest.xp_reward = 40
    thievish_bear_quest.quest_name = "Złodziejski Miś"
    thievish_bear_quest.quest_condition = "Zdobyto miodzik"
    thievish_bear_quest.inventory_dict = {"liczydło":1, "lina pomiarowa":1, "miodzik":-1}
    thievish_bear_quest.quest_list = [
        "Chcesz odzyskać fanty dla Leśniczego? Przynieś mi miodzika. Jeśli wrócisz z pustymi rękami, zaatakuję Cię! ",
        "Proszę, oto rzeczy Leśniczego, no idź do niego i nie zawracaj mi głowy więcej.. "]


    # Sołtys
    mayor = Npc("Sołtys", [2])
    mayor.speach_list = ["No, bywaj tu!", "Cieszysz oczy!", "Co u Ciebie?", "Witaj w naszej wiosce", "Uważaj, to niebezpieczna okolica", "Oblib, chyba tu był, poszedł do Dymiącej Góry.."]
    mayor.xp_reward = 300
    mayor.quest_name = "Zabytkowy obraz"
    mayor.quest_list = [
        "Ratuj proszę! Herszt łotrzyków okradł nas, w tym zabytkowy obraz, który wiele dla nas znaczy.. Jeśli go odzyskasz, to damy rubiny, którymi przekupisz Trolla Silnorękiego.. ",
        
        "Dziękuję! Wspaniale. Doprawdy nie wiem, jak Ci dziękować.. A tak, oto Twoja nagroda! Idź, daj to Trollowi, to Cię przepuści.. "    
    ]
    
    mayor.quest_condition = "Zdobyto zabytkowy obraz"
    mayor.inventory_dict = {"rubiny":3, "zabytkowy obraz":-1}



    # Troll Silnoręki
    troll_strong_hand = Npc("Troll Silnoręki", [1])
    troll_strong_hand.speach_list = [u"Chcieć na druga strona dziury? Dać rubiny", "(sapie)", "Śmierć tu znaleźć.. "]
    troll_strong_hand.xp_reward = 800
    troll_strong_hand.quest_name = "Rubiny dla trolla"
    troll_strong_hand.quest_condition = "Zdobyto rubiny"
    troll_strong_hand.inventory_dict = {"rubiny":-3}
    troll_strong_hand.quest_list = [
        "Dać mi trzy rubiny, ja cie puścić. Wrócić bez nich - zginąć marnie, zginąć marnie, tak... ",
        "Ty przejść, ja cie nie zabić teraz.. "]
    troll_strong_hand.quest_special_reward = ["portal 3"]



    # Strażnik portalu
    portal_keeper = Npc("Strażnik portalu", [3])
    portal_keeper.speach_list = ["To niebezpieczna kraina, uważaj na siebie! ", "Co słychać? ",
    "Oblib, oblib... no nie wiem.. ", "Pilnuję portalu.. ", "Mam nadzieję, że skończą się problemy ze skurczybykami.. "]
    portal_keeper.xp_reward = 1000
    portal_keeper.quest_name = "pierścień skurczybyka"
    portal_keeper.quest_list = [
        "Czarownik? Tak, jego siedziba jest za portalem. Chcesz przejść? Pomóż mi ze skurczybykami - nie dają nam spokoju! Przynieś pierścień skurczybyka, to Cię przepuszczę.. ",
        
        "Nie doceniałem Cię - wspaniale, otwieram portal - przejdź proszę! Uważaj jeno na podstępnego czarownika! Masz też coś na drogę.. "    
    ]
    
    portal_keeper.quest_condition = "Zdobyto pierścień skurczybyka"
    portal_keeper.inventory_dict = {"placek śliwkowy":2}
    portal_keeper.quest_special_reward = ["portal 2"]

    # Pustelnik - przełęcz rozpaczy
    hermit = Npc("Pustelnik", [3])
    hermit.speach_list = ["Witaj w mojej pustelni..", "Oblib.. tak, posłuchaj...", "Od wieku żyję tu w samotni..",
    "Uważaj, to straszna kraina..", "Idź do Strażnika portalu, porozmawiaj z nim.. "]
    hermit.xp_reward = 10
    hermit.quest_name = "Oblib.."
    hermit.quest_condition = "Oblib"
    hermit.inventory_dict = {"srebro":1}
    hermit.quest_list = [
        "Tak, karzeł Oblib.. Niestety zginął. Obrączka? Zabił go czarownik, ale to potężna i straszna kreatura.. Idź do Strażnika portalu, on zna drogę..", 
        "I jak, byłeś u Strażnika portalu?.. "]
    




    # npc_quest_list contains list with  QUEST npc to generate and export to main:
    npc_quest_list = [redhood, forester, wrongly_smashed_camp, thievish_bear_quest, mayor,
    troll_strong_hand, portal_keeper, hermit

    ]


    npc_all_list = npc_regular_list + npc_quest_list # npc_all_list contains list of all NPC


    # if NPC name was specified, it will export NPC by given name:
    npc_exported_to_main = ''
    if name != None:
        
        for element in npc_all_list:
            if element.name == name:
                npc_exported_to_main = element

        return npc_exported_to_main


    # if enemy name wasn't specified, it will export random enemy (random using optional filters - level, location, genre):
    else:
        npc_random_list = []
         # temporary helper list
        tmp_lvl = 0 # helps in loop below:
        for element in npc_regular_list:
            if (loc in element.location_list or loc == None):
                npc_random_list.append(element)
        

        # export random npc to main function:
        npc_rnd_exported_to_main = npc_random_list[random.randint(0, len(npc_random_list)-1)]
        
        return npc_rnd_exported_to_main



