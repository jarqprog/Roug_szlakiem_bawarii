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
   def __init__(self, name, attack, agility, defence, life_point, genre, xp4hero, treasure, specials, speach):
       self.name = name
       self.attack = attack
       self.agility = agility
       self.defence = defence
       self.life_point = life_point
       self.genre = genre
       self.xp4hero = xp4hero
       self.treasure = treasure
       self.specials = specials
       self.speach = speach


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


def enemy_random_choice(game_lvl = None):  # PRZECIWNICY - inicjacja zmiennych ##############################
    wolf = Enemy("wilk",1,3,1,10,"animal",5,1,None,"Wrrrrr!")
    dog = Enemy("pies",1,1,1,2,"animal",5,1,None,"Hau!")
    bear = Enemy("niedźwiedź",2,1,3,30,"animal",15,2,None,"Mrrrrrruummm!")
    troll = Enemy("troll",2,1,3,30,"beast",15,2,"Kamienna skóra - trolla ciężko ubić","Co Ty chcieć?!")
    # na tej samej zasadzie zrobimy przemioty, itd!
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
        print("\n"*2,"***Szkakiem Bawarii***") # tu powinna być załadowana grafika strony tytułowej
        print("\n"*5,"""
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


def prints_enemy_attributes(Enemy = None):
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
    game_lvl = 2

    enemy_random = enemy_random_choice(game_lvl)
    print(enemy_random.name, enemy_random.specials)
    print(enemy_random.name)

    #print(troll.name)

################ TU URUCHAMIAMY FUNKCJE:
    #intro() # tytuł, powitanie, wybór:

    ####### ładowanie gry LUB tworzenie bohatera LUB galeria sław LUB info o nas
    ####### po każdej z tych funkcji odpalamy główną pętlę:
     
    # ----- tu będzie funkcja do wyświetlania mapy
    #display_hero_chart(player_character)
    #prints_enemy_attributes(troll(Enemy))



main()




