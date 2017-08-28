# Szlakiem Bawarii - plik roboczy Jarka
import os, time, random  

# custom modules:
from mod_varied_info import display_varied_info
import mod_enemy
from mod_enemy import enemy_settings
import mod_hero 
from mod_hero import hero_settings

os.system('cls' if os.name == 'nt' else 'clear')

class Inv_items:
    '''
    muszę dodać:
    diamenty
    rubiny
    pierścień skurczybyka
    nóż


    '''
    pass  





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


def inventory_update(player_character, add_remove_items_dict):
    '''
    add or remove items from hero's inventory
    '''

    player_character.inventory_dict.update(add_remove_items_dict)

    temp_dict = {} # temporary inventory dict
    for item in player_character.inventory_dict:
        # if inventory key value is < 1 (empty position), remove item from inventory:
        if player_character.inventory_dict[item] > 0:
            temp_dict.update({item:player_character.inventory_dict[item]})
    
    player_character.inventory_dict = temp_dict

    return player_character.inventory_dict
    

def display_hero_chart(player_character): #### todo
    """wyświetla kartę bohatera"""
    # przekształca słownniki z atrybutami bohatera na listy kluczy i wartości:
    attrib_regular_key_list = list(player_character.attrib_regular_dict.keys())
    attrib_regular_value_list = list(player_character.attrib_regular_dict.values())

    #################### Ekwipunek do wyświetlenia ############################
    # player_character.inventory_dict
    clear_screen() # czyści ekran
    inventory_key_list = list(player_character.inventory_dict.keys())
    inventory_value_list = list(player_character.inventory_dict.values())

    # przedmioty noszone na sobie
    # przekształcenie kluczy i wartości słownka w listy
    onbody_key_list = list(player_character.onbody_dict.keys())
    onbody_value_list = list(player_character.onbody_dict.values())
    # sprawdza najdłuższy ciąg w listach kluczy atrybutów/umiejętności/ekwipunku/na sobie
    # (pomoże to odpowiednio wydrukować tabelkę):
    total_number_of_items = max(len(attrib_regular_key_list),len(inventory_key_list),len(onbody_key_list))
    # sprawdza najdłuższy wyraz wśród list atrybutów/umiejętności/ekwipunku/rzeczy na sobie - tworzy zmienne użyte przy druku tabeli:
    printing_var = 0 #helps correctly print hero chart
    attrib_regular_longest_arg = (max(len(x) for x in attrib_regular_key_list))+printing_var
    inventory_key_list.append("") # add to avoid error with "max" below
    inventory_value_list.append("") # add to avoid error with "max" below
    inventory_longest_key_arg = (max(len(x) for x in inventory_key_list))+printing_var
    inventory_longest_value_arg = (max(len(str(x)) for x in inventory_value_list))
    inventory_key_list.remove("") # remove - it's no longer needed
    inventory_value_list.remove("") # remove - it's no longer needed
    onbody_value_longest_arg = (max(len(x) for x in onbody_value_list))+printing_var
    onbody_key_longest_arg = (max(len(x) for x in onbody_key_list))+printing_var
    onbody_value_longest_arg = (max(len(x) for x in onbody_value_list))+printing_var
    sum_longest_arg = int(attrib_regular_longest_arg+inventory_longest_key_arg+inventory_longest_value_arg+onbody_key_longest_arg+onbody_value_longest_arg)
    # ta część kodu rysuje tabelę:
    # zmienne do nagłówka: attrib_additional_dict = ,"doświadczenie":24, "poziom doświadczenia":1, "złoto":2 }
    printing_var = 10 #helps correctly print hero chart
    h00 = player_character.name.ljust(printing_var)
    h01 = player_character.proffession.ljust(printing_var)
    h02 = player_character.attrib_additional_dict["poziom doświadczenia"]
    h03 = player_character.attrib_additional_dict["życie"]
    h04 = player_character.attrib_additional_dict["pełne życie"]
    h05 = player_character.attrib_additional_dict["doświadczenie"]
    h06 = player_character.attrib_additional_dict["pkt do następnego poziomu"]
    printing_var = 5 #helps correctly print hero chart
    h1 = 'atrybuty:'.rjust(attrib_regular_longest_arg+printing_var)
    printing_var = 10 #helps correctly print hero chart
    h2 = 'w torbie:'.rjust(inventory_longest_key_arg+printing_var)
    printing_var = 5 #helps correctly print hero chart
    h3 = 'na sobie:'.rjust(inventory_longest_value_arg+onbody_key_longest_arg+printing_var)
    print(u'\n\n','Karta postaci:\n\n',"imię:",h00,"klasa:",h01,'\tżycie:',h02,"/",h03,"\tdoświadczenie:",h05,"/",h06,'\n')
    print(h1,h2,h3)
    printing_var_head_bottom = 25 #helps correctly print hero chart
    print("-"*(sum_longest_arg+printing_var_head_bottom))
    for i in range(int(total_number_of_items)) :
        
        # printing attributes (atak, obrona...):
        try:
            int(len(attrib_regular_key_list)) >= i         
            if int(len(attrib_regular_key_list)) >= i:
                iattrib = int(i)
                attribKeyPrt = str(attrib_regular_key_list[iattrib])
                attribValuePrt = str(attrib_regular_value_list[iattrib])
        except:
            attribKeyPrt = ""
            attribValuePrt = ""
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
        p3 = inventoryKeyPrt.rjust(inventory_longest_key_arg)
        p4 = inventoryValuePrt.ljust(inventory_longest_value_arg)
        p5 = onbodyKeyPrt.rjust(onbody_key_longest_arg)
        p6 = onbodyValuePrt.ljust(onbody_value_longest_arg)
    # wnętrze tabeli
        print(u'| ',p1,u':',p2,u'| ',p3,u':',p4,u'|',p5,u':',p6,u'|')
    # stopka tabeli
    print("-"*(sum_longest_arg+printing_var_head_bottom))
    print("\nLokacja: Kto tu wejdzie, ten niechybnie zginie","\n...","\n")

def main():
    # ustawia nam podstawowe zmienne:
    game_lvl = 0
    add_remove_items_dict = {}
    # importuje nam Postać do głównej funkcji (w procesie tworzenie postaci lub ładowawnia gry nastapi update postaci):
    player_character = hero_settings()
    game_lvl = 1

################ TU URUCHAMIAMY FUNKCJE:
    #intro() # tytuł, powitanie, wybór:

    ####### ładowanie gry LUB tworzenie bohatera LUB galeria sław LUB info o nas
    ####### po każdej z tych funkcji odpalamy główną pętlę:
     
    # ----- tu będzie funkcja do wyświetlania mapy

    ''' testujemy'''

    display_hero_chart(player_character)
    # bawimy się modyfikacją inventory:
    add_remove_items_dict = {"placek":1,"jacek":1}
    player_character.inventory_dict = inventory_update(player_character, add_remove_items_dict)
    add_remove_items_dict = {"placki":-11,"jacek":1}
    player_character.inventory_dict = inventory_update(player_character, add_remove_items_dict)
    display_hero_chart(player_character)
    add_remove_items_dict = {"jacek":-10, "nóż":3, "placek":2}
    player_character.inventory_dict = inventory_update(player_character, add_remove_items_dict)
    display_hero_chart(player_character)
    #losujemy przeciwnika (random), filtr ustawiony na przeciwników o levelu 4: 
    imported_enemy_rnd = enemy_settings(name = None, loc = None, lvl = 4, gen = None)
    #dodajemy jego inventory do inventory bohatera:
    add_remove_items_dict = imported_enemy_rnd.treasure_dict
    player_character.inventory_dict = inventory_update(player_character, add_remove_items_dict)
    #wyświetlamy:
    clear_screen()
    display_hero_chart(player_character)
    display_varied_info() 



main()




