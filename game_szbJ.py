# Szlakiem Bawarii - plik roboczy Jarka
import os, time, random  

os.system('cls' if os.name == 'nt' else 'clear')

################################ Hero class:
class Hero:
    def __init__(self, name, proffession, attrib_regular_dict, attrib_additional_dict, inventory_dict, onbody_dict):
        self.name = name
        self.proffession = proffession
        self.attrib_regular_dict = attrib_regular_dict
        self.attrib_additional_dict = attrib_additional_dict
        self.inventory_dict = inventory_dict
        self.onbody_dict = onbody_dict

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

class Inv_items:
    '''
    muszę dodać:
    diamenty
    rubiny
    pierścień skurczybyka
    nóż


    '''
    pass  

def hero_setting(): # BOHATER - inicjacja zmiennych ############################## 
    attrib_regular_dict = {"atak":3,"obrona":2, "zwinność":1, "percepcja":1, "inteligencja":1, "siła woli":2}
    attrib_additional_dict = {"życie":13, "pełne życie":30, "doświadczenie":24, "poziom doświadczenia":1,"doświadczenie":12, "pkt do następnego poziomu": 30, "złoto":2 }
    wolek_zbozowy = {u"name":"strzała","value":18,"info":"pocisk do łuku","price":1,"weight":2}
    i_e_d = {} # inventory empty dict (pusty słownik przedmiotu w inventory) = używany, jeśli pozycja w inventory jest pusta:
    # i# - pozycja w inventory
    placek_sliwkowy = {u"name":"placek śliwkowy","related":"jedzenie","value":2,"info":"zjedz mnie","cena":2,"waga":1}
    wolek_zbozowy = {u"name":"wołek zbożowy","related":"robak","value":10,"info":"jestem szkodnikiem","cena":0,"waga":0}   
    inventory_dict = {u"i1":placek_sliwkowy,"i2":wolek_zbozowy,"i3":i_e_d,"i4":i_e_d,"i5":i_e_d,"i6":i_e_d,"i7":i_e_d,"i8":i_e_d,"i9":i_e_d,"i10":i_e_d,"i11":i_e_d,"i12":i_e_d,"i13":i_e_d,"i14":i_e_d,"i15":i_e_d,"i16":i_e_d,"i17":i_e_d,"i18":i_e_d,"i19":i_e_d,"i20":i_e_d}
    ################################ show active items on Hero:
    onbody_dict = {u'głowa':'skórzany hełm','szyja':'','tors':'skórzany kaftan','lewa ręka':'','prawa ręka':'maczuga','palec':'','kieszeń':'sok z gumijagód'}
    ################################ przykładowy bohater (odpalenie funkcji hero_crea )
    player_character = Hero("Rabarbar","Zbójcerz", attrib_regular_dict, attrib_additional_dict, inventory_dict, onbody_dict)

    
    return player_character


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

    else:
        enemy_random_list = []
        for element in enemies_all_list:        
            if (loc in element.location or loc == None) and (lvl == element.level or lvl == None) and (gen == element.genre or gen == None):
                enemy_random_list.append(element)
        

        # export random enemy to main function:
        enemy_rnd_exported_to_main = enemy_random_list[random.randint(0, len(enemy_random_list)-1)]
        
        return enemy_rnd_exported_to_main
        # loc = None, lvl = None, gen = None


    #   # name, life, level, attrib_dict, treasure_dict, genre, xp4hero, specials, speach, location
    #wolf = Enemy("wilk",10, 1, attrib_dict,treasure_dict,"animal",5,None,"Wrrrrr!",

def enemy_random_choice(Enemy, game_lvl = None):  # PRZECIWNICY - inicjacja zmiennych ##############################

    attrib_dict = {} # pusty słownik dla atrybutów przeciwników
    treasure_dict = {} # pusty słownik z miejscem na przedmioty u przeciwników (można to wykorzystać m.in. do "losowania łupu")
    # (self, name, life, dmg, attrib_dict, treasure_dict, genre, xp4hero, specials, speach, location)
    wolf = Enemy("wilk",10, 3, attrib_dict,treasure_dict,"animal",5,None,"Wrrrrr!",4)
    wolf.attrib_dict = {"atak":3,"obrona":2, "zwinność":1, "percepcja":1, "inteligencja":1, "siła woli":2, "obrażenia":[1,3]}  
    #dog = Enemy("pies",1,1,1,2,"animal",5,1,None,"Hau!")
    #bear = Enemy("niedźwiedź",2,1,3,30,"animal",15,2,None,"Mrrrrrruummm!")
    troll = Enemy("troll",80,[3,6],attrib_dict,treasure_dict,"beast",15,"Kamienna skóra - trolla ciężko ubić","Co Ty chcieć?!")
    troll.attrib_dict = {"atak":3,"obrona":2, "zwinność":1, "percepcja":1, "inteligencja":1, "siła woli":2, "obrażenia":[1,3]}
    troll.treasure_dict = {"złoto":(random.randint(1,100)), "rubiny":(random.randint(0,12))}

    if game_lvl == 2:
        return troll
    elif game_lvl == 1:
        return wolf
    else:
        return dog



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


def prints_hero_attributes(player_character):
    print(player_character.name)
    print(player_character.attrib_regular_dict)
    print(player_character.inventory_dict)
    print(player_character.onbody_dict)


def prints_enemy_attributes(Enemy = None): # dla testów
    if Enemy.genre == "animal" :
        print("Jestem zwierzakiem, nie zabijajcie mnie! Jestem",enemy.name,"!")
    else:
        print("Zginiesz, głupcze!")

    if Enemy.life_point < 20 :
        print("Mam niską wytrzymałość!")
    else:
        print("Nie jestem taki słaby!")
    Enemy = troll
    print(Enemy.speach, Enemy.specials)

def display_hero_chart(player_character): #### todo
    """wyświetla kartę bohatera"""
    # przekształca słownniki z atrybutami bohatera na listy kluczy i wartości:
    attrib_regular_key_list = list(player_character.attrib_regular_dict.keys())
    attrib_regular_value_list = list(player_character.attrib_regular_dict.values())
    attrib_additional_key_list = list(player_character.attrib_additional_dict.keys())
    attrib_additional_value_list = list(player_character.attrib_additional_dict.values())
    #################### Ekwipunek do wyświetlenia ############################
    i_e_d = {}
    inventory_key_list = []
    inventory_value_list = []
    for item in player_character.inventory_dict:
        if player_character.inventory_dict[item] != i_e_d:
            inventory_key_list.append(player_character.inventory_dict[item]["name"])
            inventory_value_list.append(player_character.inventory_dict[item]["value"])
    
    # przedmioty noszone na sobie
    # przekształcenie kluczy i wartości słownka w listy
    onbody_key_list = list(player_character.onbody_dict.keys())
    onbody_value_list = list(player_character.onbody_dict.values())
    clear_screen() # czyści ekran:
    # rysowanie tabeli dla danych z czterech słowników (atrybutów/umiejętności/ekwipunku/rzeczy noszonych na sobie)
    # sprawdza najdłuższy ciąg w listach kluczy atrybutów/umiejętności/ekwipunku/na sobie
    # (pomoże to odpowiednio wydrukować tabelkę):
    total_number_of_items = max(len(attrib_regular_key_list),len(inventory_key_list),len(onbody_key_list))
    # sprawdza najdłuższy wyraz wśród list atrybutów/umiejętności/ekwipunku/rzeczy na sobie - tworzy zmienne użyte przy druku tabeli:
    attrib_regular_longest_arg = (max(len(x) for x in attrib_regular_key_list))+5
    inventory_longest_arg = (max(len(x) for x in inventory_key_list))+5
    onbody_key_longest_arg = (max(len(x) for x in onbody_key_list))+5
    onbody_value_longest_arg = (max(len(x) for x in onbody_value_list))+5
    sum_longest_arg = int(attrib_regular_longest_arg+inventory_longest_arg+onbody_key_longest_arg+onbody_value_longest_arg)
    # ta część kodu rysuje tabelę:
    # zmienne do nagłówka: attrib_additional_dict = ,"doświadczenie":24, "poziom doświadczenia":1, "złoto":2 }
    h00 = player_character.name.ljust(10)
    h01 = player_character.proffession.ljust(10)
    h02 = player_character.attrib_additional_dict["poziom doświadczenia"]
    h03 = player_character.attrib_additional_dict["życie"]
    h04 = player_character.attrib_additional_dict["pełne życie"]
    h05 = player_character.attrib_additional_dict["doświadczenie"]
    h06 = player_character.attrib_additional_dict["pkt do następnego poziomu"] 
    h1 = 'atrybuty:'.rjust(attrib_regular_longest_arg+5)
    h2 = 'w torbie:'.rjust(inventory_longest_arg+10)
    h3 = 'na sobie:'.rjust(onbody_key_longest_arg+9)
    print(u'\n\n','Karta postaci:\n\n',"imię:",h00,"klasa:",h01,'\tżycie:',h02,"/",h03,"\tdoświadczenie:",h05,"/",h06,'\n')
    print(h1,h2,h3)
    print("-"*(sum_longest_arg+30))
    for i in range(int(total_number_of_items)) :
        try:
            int(len(attrib_regular_key_list)) >= i         
            if int(len(attrib_regular_key_list)) >= i:
                iattrib = int(i)
                attribKeyPrt = str(attrib_regular_key_list[iattrib])
                attribValuePrt = str(attrib_regular_value_list[iattrib])
        except:
            attribKeyPrt = ""
            attribValuePrt = ""
        try: #zmień nazwy!!!
            int(len(attrib_additional_key_list)) >= i         
            if int(len(attrib_additional_key_list)) >= i:
                iskills = int(i)
                skillsKeyPrt = str(attrib_additional_key_list[iskills])
                skillsValuePrt = str(attrib_additional_value_list[iskills])
        except:
            skillsKeyPrt = ""
            skillsValuePrt = ""
        try:
            int(len(inventory_key_list)) >= i         
            if int(len(inventory_key_list)) >= i:
                iinventory = int(i)
                inventoryKeyPrt = str(inventory_key_list[iinventory])
                inventoryValuePrt = str(inventory_value_list[iinventory])
        except:
            inventoryKeyPrt = ""
            inventoryValuePrt = ""
        try:
            int(len(onbody_key_list)) >= i         
            if int(len(onbody_key_list)) >= i:
                ionbody = int(i)
                onbodyKeyPrt = str(onbody_key_list[ionbody])
                onbodyValuePrt = str(onbody_value_list[ionbody])
        except:
            onbodyKeyPrt = ""
            onbodyValuePrt = ""
    # zmienne przeznaczone do druku poniżej, wprowadzone dla czyletności linii z 'print'
        #longest_arg = 10
        p1 = attribKeyPrt.rjust(attrib_regular_longest_arg)
        p2 = attribValuePrt.ljust(4)
        p3 = '' #tmp
        p4 = skillsValuePrt.ljust(4)
        p5 = inventoryKeyPrt.rjust(inventory_longest_arg)
        p6 = inventoryValuePrt.ljust(4)
        p7 = onbodyKeyPrt.rjust(onbody_key_longest_arg)
        p8 = onbodyValuePrt.ljust(onbody_value_longest_arg)
    # wnętrze tabeli
        print(u'| ',p1,u':',p2,u'| ',p5,u':',p6,u'|',p7,u':',p8,u'|')
    # stopka tabeli
    print("-"*(sum_longest_arg+30)) # TMP!! (magic number)
    print("\nLokacja: Kto tu wejdzie, ten niechybnie zginie","\n...","\n")

def main():
    # ustawia nam podstawowe zmienne:
    game_lvl = 0
    # importuje nam Postać do głównej funkcji (w procesie tworzenie postaci lub ładowawnia gry nastapi update postaci):
    player_character = hero_setting()
    '''
    ############ ustawiamy przeciwników - możemy tu ich definiować, ale chyba damy do osobnej funkcji...
    wolf = Enemy("wilk",1,3,1,10,"animal",5,1,None,"Wrrrrr!")
    dog = Enemy("pies",1,1,1,2,"animal",5,1,None,"Hau!")
    bear = Enemy("niedźwiedź",2,1,3,30,"animal",15,2,None,"Mrrrrrruummm!")
    troll = Enemy("troll",2,1,3,30,"beast",15,2,"Kamienna skóra - trolla ciężko ubić","Co Ty chcieć?!")
    '''
    game_lvl = 1
    imported_enemy = enemy_settings(name = "Zły Miś", loc = None, lvl = None, gen = None)
    print(imported_enemy.name, imported_enemy.attrib_dict["obrażenia"], imported_enemy.attrib_dict["atak"], imported_enemy.treasure_dict.items())

    # imported_enemy_rnd = imported random enemy from function 'enemy_settings':
    imported_enemy_rnd = enemy_settings(name = None, loc = 1, lvl = 2, gen = "human")
    print(imported_enemy_rnd.name, imported_enemy_rnd.speach_list, imported_enemy_rnd.treasure_dict)

    #print(imported_enemy.name, imported_enemy.treasure_dict)
    #print(imported_enemy.__dict__)
    

    #print(imported_enemy.treasure_dict, imported_enemy.dmg, imported_enemy.attrib_dict["atak"], imported_enemy.location)

    #print(wolf)
        
    #enemy_random = enemy_random_choice(game_lvl)
    #print(enemy_random.name, enemy_random.specials, enemy_random.treasure_dict)
    #print(enemy_random.attributes())

    #print(troll.name)

################ TU URUCHAMIAMY FUNKCJE:
    #intro() # tytuł, powitanie, wybór:

    ####### ładowanie gry LUB tworzenie bohatera LUB galeria sław LUB info o nas
    ####### po każdej z tych funkcji odpalamy główną pętlę:
     
    # ----- tu będzie funkcja do wyświetlania mapy
    #display_hero_chart(player_character)
    #prints_enemy_attributes(troll(Enemy))



main()




