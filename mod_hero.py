
# mod_hero - custom mod, contains player_character data

################################ Hero class:
class Hero:
    def __init__(self, name, proffession, level, attrib_regular_dict, inventory_dict, onbody_dict):
        # hero's name:
        self.name = name
        # hero's class (warior, hunter, thief...)
        self.proffession = proffession
        # hero's expirience level:
        self.level = level
        # contains basic atributes (attack, defence, agility...), that we are using in game mechanic's tests:  
        self.attrib_regular_dict = attrib_regular_dict
        # contains hero inventory (non active items - in bag):
        self.inventory_dict = inventory_dict
        # contains active items that have influence on hero (wearing items):
        self.onbody_dict = onbody_dict

        self.maxLife = 99 # max life points (limit)
        self.actualLife = 99 # actual number of life points
        self.actualExp = 1 # actual number of exp points
        self.gold = 2 # wealt in pouch
        self.location = 1 # actual map level
        self.dmg_list = [1,2]

        
# BOHATER - inicjacja zmiennych ##############################

def hero_settings():
    '''
    contains player_character data to export to main:
    '''
    # hero dicts:
    attrib_regular_dict = {"atak":3, "obrona":2, "zwinność":1, "percepcja":1, "inteligencja":1, "siła woli":2}

    ################## inventory_dict keep only names and values of items (without deep specyfication)
    inventory_dict = {"nóż":1,"placki":10, "resztki mapy":1} #placki będzie można sprzedać albo nakarmić głodnego (quest)

    ################################ show active items on Hero:

    onbody_dict = {u'głowa':'skórzany hełm','szyja':'','tors':'skórzany kaftan','lewa ręka':'','prawa ręka':'maczuga','palec':'','kieszeń':'sok z gumijagód'}
    
    ################################ przykładowy bohater (odpalenie funkcji hero_crea )
    player_character = Hero("Rabarbar", "Zbójcerz", 1, attrib_regular_dict, inventory_dict, onbody_dict)

    
    return player_character


def exp_nextlvl(player_character):
    '''
    calculate experience points required to achive next experience level
    '''
    return ((50*player_character.level)*2*player_character.level)

def display_exp(player_character):
    '''
    display actual exp and exp needed to achive next level
    '''
    nextLevel = exp_nextlvl(player_character)

    return (''.join((str(player_character.actualExp),'/',(str(nextLevel)))))


def display_life(player_character):
    '''
    display actual life points and max life points
    '''

    return (''.join((str(player_character.actualLife),'/',(str(player_character.maxLife)))))


def display_gold(player_character):
    '''
    display gold (hero's wealth) in right format
    '''

    return (''.join((str(player_character.gold),' szt. złota')))

def display_location(player_character):
    if player_character.location == 1:
        return "Łotrzykowa Dolina"
    elif player_character.location == 2:
        return "Niezmierzony Las"
    elif player_character.location == 3:
        return "Kraina Gigantów"
    elif player_character.location == 4:
        return "Dymiąca Góra"



def display_damage(player_character):
    '''
    display hero's actual min and max damage
    '''
    player_character.dmg_list


    return (''.join((str(player_character.dmg_list[0]),'-',(str(player_character.dmg_list[1])))))

