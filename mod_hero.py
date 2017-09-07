
# mod_hero - custom mod, contains hero data

import mod_items, math, mod_npc, mod_display


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
        self.location = 1 # actual map level
        self.map_position = 0 # hero map position
        self.position_horizontal = 1 # hero map coordinate X
        self.position_vertical = 18 # hero map coordinate Y
        self.dmg_list = [1,4] # initial min and max damage
        self.attack = 0 # initial attack points
        self.defend = 0 # initial defend points
        self.courage = 0 # initial courage points
        self.attack = 0
        self.defend = 0
        self.max_armour = 0 # max armour points calculated by "amour_max_calc(hero = None)" function in this mod
        self.act_armour = 1 # modified by armour in onbody_dict OR (OPTIONAL) actual armour points calculated by "amour_act_calc(hero = None)" function in this mod
        self.add_remove_items_dict = {} # dict used for modify hero inventory (add/remove)
        self.life_recovery = 5 # define replenish life level after each turn
        self.calendar_list = [0, "niedziela", "wieczór"] # define actual game turn (number of main loop executed)


        
        # combat_attribute:
        # determines what hero attribute is used in combat tests, it comes from item in hero onbody_dict["prawa ręka"]
        # for example, if hero is using dagger,
        # main concidered attribute is aggility ("zwinność") or in case of heavy axe we use strenght ("siła")
        # if hero onbody_dict["prawa ręka"] is empty ("") default attribute is set by function:
        # combat_attribute_default(hero = hero) in this mod
        self.combat_attribute = combat_attribute_default(hero = self)
        # quest_info contains speach statements, that have been told by NPC..
        # if element od NPC speach list is in value of dict key, key = quest name,
        # NPC tells next element on list
        self.quest_info = {}
        self.quest_condition_list = []
        self.quest_blocked_list = []
        self.quest_completed_list = []
        #self.new_location = 1

        
# BOHATER - inicjacja zmiennych ##############################

def hero_settings():
    '''
    contains hero data to export to main:
    '''
    # hero dicts:
    attrib_dict = {"siła":1, "zwinność":1, "percepcja":1, "inteligencja":1, "siła woli":1}

    ################## inventory_dict keep only names and values of items (without deep specyfication)
    inventory_dict = {"srebro":3} #placki będzie można sprzedać albo nakarmić głodnego (quest)
    
    ################################ show active items on Hero:

    onbody_dict = {u'głowa':'skórzany hełm','szyja':'','tors':'skórzany kaftan','lewa ręka':'','prawa ręka':'maczuga','palec':'','kieszeń':'sok z gumijagód'}
    
    ################################ przykładowy bohater (odpalenie funkcji hero_crea )
    hero = Hero("", "", 1, attrib_dict, inventory_dict, onbody_dict)
    hero.calendar_list = [0, "niedziela", "wieczór"]
    #hero.attack = attack_points_calc(hero)
    #hero.defend = defend_points_calc(hero)
    hero.new_location = 1
    hero.map_board = ""
    hero.gold = 2 # initial wealt in pouch
  
    return hero

def attack_points_calc(hero = None):
    ''' calculates hero attack ability '''
    hero.attack = 2*hero.attrib_dict["siła"]+2*hero.attrib_dict["zwinność"]+hero.attrib_dict["inteligencja"]
    
    return hero.attack


def defend_points_calc(hero = None):
    ''' calculates hero defend ability '''
    hero.defend = 3*hero.attrib_dict["zwinność"]+hero.attrib_dict["siła"]+hero.attrib_dict["inteligencja"]+hero.act_armour
    
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
        return "Niezmierzony Las"
    elif hero.location == 2:
        return "Kraina Trolli"
    elif hero.location == 3:
        return "Dymiąca Góra"
    elif hero.location == 4:
        return "Nawiedzone zamczysko"



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
        mod_items.items_settings(name = (hero.onbody_dict["prawa ręka"]), loc = None, lvl = None, gen = None, hero = None, all = None)

        imported_item = mod_items.items_settings(name = hero.onbody_dict["prawa ręka"], loc = None, lvl = None, gen = None, hero = hero, all = None)

        hero.combat_attribute = imported_item.combat_attribute

        return hero.combat_attribute
        
        '''
        hero.combat_attribute = ("pobieram z przedmiotu", hero.onbody_dict["prawa ręka"])
        '''


def items_list_to_dict(items_to_add):
    '''
    transform list of items to dictionary (used to update hero's inventory dict)
    '''
    items_dict = {}
    for item in items_to_add:
        if item in items_dict:
            items_dict[item] += 1
        else:
            items_dict[item] = 1
        
    return items_dict


def inventory_update(hero, add_remove_items_dict):
    '''
    add or remove items from hero's inventory
    '''
    # make copy of both dicts:
    hero_items = hero.inventory_dict
    add_items = add_remove_items_dict

    for item in add_items.keys():
        if item not in hero_items: # if it's new item = copy item to inventory
            hero_items[item] = add_items[item]
        elif item in hero_items: # if it's not new item = add item value to inventory
            hero_items[item] += add_items[item]
        if int(hero_items[item]) < 1: # if value inventory item is negativ number = remove item from inventory*
            del hero_items[item]

    # * we can use it in shops, when selling items..

    hero.inventory_dict = hero_items

    return hero


def hero_on_map(hero = None):
    '''
    change hero coordinates while moving on the map
    '''
    pass


def hero_creation():
    clear_screen()
    print("tworzenie bohatera - do zrobienia") # to ja bym zrobił





def calendar(calendar_list = None):
    week_list = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"]
    day_time_list = ["poranek", "południe", "popołudniu", "wieczór"]
   
    week_index = week_list.index(calendar_list[1])
    day_index = day_time_list.index(calendar_list[2])
  

  
    if calendar_list[2] != day_time_list[3]:
        time_of_day = day_time_list[day_index+1]
        
    else:
        
        time_of_day = day_time_list[0]
        
        if calendar_list[1] != week_list[6]:
            day_of_week = week_list[week_index+1]
            
        if calendar_list[1] == week_list[6]:
            day_of_week = week_list[0]
        del calendar_list[1]
        calendar_list.insert(1, day_of_week)
      
        calendar_list[0] +=1 
    del calendar_list[2]
      
    calendar_list.insert(2, time_of_day)
  
    return calendar_list


def quest(hero = None, npc = None):

    if npc.quest_name not in hero.quest_info.keys():
        for element in npc.quest_list:
            if element not in hero.quest_info.values():
                hero.quest_info[npc.quest_name] = [element]
                break

    else:
        if npc.quest_list[0] not in hero.quest_blocked_list:       
            hero.quest_blocked_list.append(npc.quest_list[0])
        
        
    if npc.quest_condition in hero.quest_condition_list:
        if npc.quest_list[1] not in hero.quest_info[npc.quest_name]:
            temporary_list = []
            temporary_list.append([npc.quest_list[1]])
            hero.quest_info[npc.quest_name] += temporary_list[0]
            del temporary_list[:]

    return hero


def next_level_promotion(hero = None):
    '''
    check if there is hero level promotion
    allows to player modify one of hero attributes
    displays result 
    '''
    if hero.actualExp > ((50*hero.level)*2*hero.level):
        
        player_choice = mod_display.display_next_level_promotion(hero = hero)
        hero.level += 1
        hero.maxLife += 20 # buff to max life
        hero.actualLife = hero.maxLife # full life regenration
        mod_display.display_hero_chart(hero)
        if player_choice == 1:
            hero.attrib_dict["siła"] += 1
            print("Wzrosła siła i życie")
        elif player_choice == 2:
            hero.attrib_dict["zwinność"] += 1
            print("Wzrosła zwinność i życie")
        elif player_choice == 3:
            hero.attrib_dict["percepcja"] += 1
            print("Wzrosła percepcja i życie")
        elif player_choice == 4:
            hero.attrib_dict["inteligencja"] += 1
            print("Wzrosła inteligencja i życie")
        else:
            hero.attrib_dict["siła woli"] += 1
            print("Wzrosła siła woli i życie")
    
        mod_display.pause()
                
    return hero


def hero_life_regeneration(hero = None):
    '''
    regenerate hero life point after each turn 
    '''
    hero.actualLife += hero.life_recovery
    if hero.actualLife > hero.maxLife: hero.actualLife = hero.maxLife
              
    return hero












 

        



    

