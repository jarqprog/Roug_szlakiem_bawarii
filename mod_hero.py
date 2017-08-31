
# mod_hero - custom mod, contains hero data

import mod_items
from mod_items import items_settings


################################ Hero class:
class Hero:
    def __init__(self, name, proffession, level, attrib_dict, inventory_dict, onbody_dict):
        # hero's name:
        self.name = name
        # hero's class (warior, hunter, thief...)
        self.proffession = proffession
        # hero's expirience level:
        self.level = level
        # contains basic atributes (attack, defence, agility...), that we are using in game mechanic's tests:  
        self.attrib_dict = attrib_dict
        # contains hero inventory (non active items - in bag):
        self.inventory_dict = inventory_dict
        # contains active items that have influence on hero (wearing items):
        self.onbody_dict = onbody_dict

        self.maxLife = 30 # max life points (limit)
        self.actualLife = 30 # actual number of life points
        self.actualExp = 1 # actual number of exp points
        self.gold = 2 # initial wealt in pouch
        self.location = 1 # actual map level
        self.dmg_list = [1,4] # initial min and max damage
        self.attack = 0 # initial attack points
        self.defend = 0 # initial defend points
        self.courage = 0 # initial courage points
        self.attack_attribute = None
        self.defend_attribute = None
        self.max_armour = 0 # max armour points calculated by "amour_max_calc(hero = None)" function in this mod
        self.act_armour = 1 # modified by armour in onbody_dict OR (OPTIONAL) actual armour points calculated by "amour_act_calc(hero = None)" function in this mod
        
        # combat_attribute:
        # determines what hero attribute is used in combat tests, it comes from item in hero onbody_dict["prawa ręka"]
        # for example, if hero is using dagger,
        # main concidered attribute is aggility ("zwinność") or in case of heavy axe we use strenght ("siła")
        # if hero onbody_dict["prawa ręka"] is empty ("") default attribute is set by function:
        # combat_attribute_default(hero = hero) in this mod
        self.combat_attribute = combat_attribute_default(hero = self)
        
# BOHATER - inicjacja zmiennych ##############################

def hero_settings():
    '''
    contains hero data to export to main:
    '''
    # hero dicts:
    attrib_dict = {"siła":3, "zwinność":2, "percepcja":2, "inteligencja":1, "siła woli":2}

    ################## inventory_dict keep only names and values of items (without deep specyfication)
    inventory_dict = {"nóż":1,"placki":10, "resztki mapy":1} #placki będzie można sprzedać albo nakarmić głodnego (quest)

    ################################ show active items on Hero:

    onbody_dict = {u'głowa':'skórzany hełm','szyja':'','tors':'skórzany kaftan','lewa ręka':'','prawa ręka':'maczuga','palec':'','kieszeń':'sok z gumijagód'}
    
    ################################ przykładowy bohater (odpalenie funkcji hero_crea )
    hero = Hero("Rabarbar", "Zbójcerz", 1, attrib_dict, inventory_dict, onbody_dict)


    
    return hero

def attack_points_calc(hero = None):
    ''' calculates hero attack ability '''
    hero.attack = hero.attrib_dict["siła"]+hero.attrib_dict["zwinność"]+hero.attrib_dict["inteligencja"]
    
    return hero.attack


def defend_points_calc(hero = None):
    ''' calculates hero defend ability '''
    hero.defend = 2*hero.attrib_dict["zwinność"]+hero.attrib_dict["inteligencja"]+hero.act_armour
    
    return hero.defend


def exp_nextlvl(hero = None):
    '''
    calculate experience points required to achive next experience level
    '''
    return ((50*hero.level)*2*hero.level)


def amour_max_calc(hero = None):
    ''' calculates max armour points '''
    hero.max_armour = hero.attrib_dict["siła"]
    
    return hero.max_armour


def amour_act_calc(hero = None): ######################### TEMP!
    ''' calculates actual armour points '''
    '''
    mod_items.items_settings()
    try:
        for item in hero.onbody_dict.values():
            if item in 
            
    except Exception as e:
        raise e
    hero.max_armour = 2*hero.attrib_dict["siła"]
    
    return hero.max_armour
    '''

def display_exp(hero = None):
    '''
    display actual exp and exp needed to achive next level
    '''
    nextLevel = exp_nextlvl(hero)

    return (''.join((str(hero.actualExp),'/',(str(nextLevel)))))


def display_life(hero = None):
    '''
    display actual life points and max life points
    '''

    return (''.join((str(hero.actualLife),'/',(str(hero.maxLife)))))


def display_gold(hero = None):
    '''
    display gold (hero's wealth) in right format
    '''

    return (''.join((str(hero.gold),' szt. złota')))

def display_location(hero = None):
    if hero.location == 1:
        return "Łotrzykowa Dolina"
    elif hero.location == 2:
        return "Niezmierzony Las"
    elif hero.location == 3:
        return "Kraina Gigantów"
    elif hero.location == 4:
        return "Dymiąca Góra"



def display_damage(hero = None):
    '''
    display hero's actual min and max damage
    '''
    hero.dmg_list


    return (''.join((str(hero.dmg_list[0]),'-',(str(hero.dmg_list[1])))))



def display_armour(hero = None):
    '''
    used to display actual and max armour points
    '''

    return (''.join((str(hero.act_armour),'/',(str(hero.max_armour)))))

def display_armour(hero = None):
    '''
    used to display actual and max armour points
    '''

    return (''.join((str(hero.act_armour),'/',(str(hero.max_armour)))))


def combat_attribute_default(hero = None):
    '''set default value of combat_attribute'''


    if hero.onbody_dict["prawa ręka"] == "":
        if hero.attrib_dict["siła"] >= hero.attrib_dict["zwinność"]:
            hero.combat_attribute = "siła"
            return hero.combat_attribute
        else:
            hero.combat_attribute = "zwinność"
            return hero.combat_attribute            
            
    else:
        items_settings(name = (hero.onbody_dict["prawa ręka"]), loc = None, lvl = None, gen = None, hero = None, all = None)

        impored_item = items_settings(name = hero.onbody_dict["prawa ręka"], loc = None, lvl = None, gen = None, hero = hero, all = None)

        hero.combat_attribute = impored_item.combat_attribute

        return hero.combat_attribute
        
        '''
        hero.combat_attribute = ("pobieram z przedmiotu", hero.onbody_dict["prawa ręka"])
        '''
        
        



    

