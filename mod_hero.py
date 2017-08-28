
# mod_hero - custom mod, contains player_character data

################################ Hero class:
class Hero:
    def __init__(self, name, proffession, attrib_regular_dict, attrib_additional_dict, inventory_dict, onbody_dict):
        self.name = name
        self.proffession = proffession
        self.attrib_regular_dict = attrib_regular_dict
        self.attrib_additional_dict = attrib_additional_dict
        self.inventory_dict = inventory_dict
        self.onbody_dict = onbody_dict



def hero_settings(): # BOHATER - inicjacja zmiennych ##############################
    '''
    contains player_character data to export to main:
    '''
    attrib_regular_dict = {"atak":3,"obrona":2, "zwinność":1, "percepcja":1, "inteligencja":1, "siła woli":2}
    attrib_additional_dict = {"życie":13, "pełne życie":30, "doświadczenie":24, "poziom doświadczenia":1,"doświadczenie":12, "pkt do następnego poziomu": 30, "złoto":2 }

    ################## items will go to another function (like enemies)
    placek_sliwkowy = {u"name":"placek śliwkowy","related":"jedzenie","value":2,"info":"zjedz mnie","cena":2,"waga":1}
    wolek_zbozowy = {u"name":"wołek zbożowy","related":"robak","value":10,"info":"jestem szkodnikiem","cena":0,"waga":0}   

    ################## inventory_dict keep only names and values of items (without deep specyfication)
    inventory_dict = {"nóż":1,"placki":10, "resztki mapy":1} #placki będzie można sprzedać albo nakarmić głodnego (quest)

    ################################ show active items on Hero:

    onbody_dict = {u'głowa':'skórzany hełm','szyja':'','tors':'skórzany kaftan','lewa ręka':'','prawa ręka':'maczuga','palec':'','kieszeń':'sok z gumijagód'}
    ################################ przykładowy bohater (odpalenie funkcji hero_crea )
    player_character = Hero("Rabarbar","Zbójcerz", attrib_regular_dict, attrib_additional_dict, inventory_dict, onbody_dict)

    
    return player_character