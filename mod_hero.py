#!/usr/bin/python3
# mod_hero - custom mod, contains hero data

# import custom modules:
import mod_items
import mod_display


# Hero class:
class Hero:
    def __init__(self):
        # hero's name:
        self.name = ""
        # hero's class (warior, hunter, thief...)
        self.proffession = ""
        # hero's expierience level:
        self.level = 1
        # contains basic atributes (attack, defence, agility...),
        # that we are using in game mechanic's tests:
        self.attrib_dict = {
            "siła": 1, "zwinność": 1, "percepcja": 1,
            "inteligencja": 1, "siła woli": 1
            }  # starting attributes dict
        
        # contains hero inventory (non active items - in bag):
        self.inventory_dict = {'placek śliwkowy': 3}
        # contains active items that have influence on hero (wearing items):
        self.onbody_dict = {
            'głowa': '',
            'szyja': '',
            'tors': '',
            'lewa ręka': '',
            'prawa ręka': '',
            'palec': '',
            'kieszeń': ''
            }
        self.max_life = 40  # max life points (limit)
        self.actual_life = 40  # actual number of life points
        self.actualExp = 1  # actual number of exp points
        self.location = 1  # actual map level
        self.map_position = 0  # hero map position ????????????????????????
        self.position_horizontal = 1  # hero map coordinate X
        self.position_vertical = 18  # hero map coordinate Y
        # initial min and max damage
        # (calculate by function dmg_points_calc in this mode)
        self.dmg_list = [0, 0]
        self.attack = 0  # initial attack points
        self.defend = 0  # initial defend points
        self.courage = 0  # initial courage points - not used yet
        # max armour points calculated by "amour_max_calc(hero=None)"
        # function in this mod (it depends on hero strength)
        self.max_armour = 0
        # modified by armour in onbody_dict OR
        # (OPTIONAL) actual armour points calculated
        # by "amour_act_calc(hero=None)" function in this mod
        self.act_armour = 0
        # dict used for modify hero inventory (add/remove)
        self.add_remove_items_dict = {}
        # define replenish life level after each turn
        self.life_recovery = 1
        # define actual game turn (number of main loop executed)
        self.calendar_list = [
            0, "niedziela", "wieczór"
            ]  # start value of calendar list
      
        # combat_attribute:
        # determines what hero attribute is used in combat tests,
        # it comes from item in hero onbody_dict["prawa ręka"]
        # for example, if hero is using dagger,
        # main concidered attribute is aggility ("zwinność") or
        # in case of heavy axe we use strenght ("siła")
        # if hero onbody_dict["prawa ręka"] is empty ("")
        # default attribute is set by functioncheck_combat_attribute
        self.combat_attribute = check_combat_attribute(self)

        # QUESTS parametres:

        # quest_info contains speach statements, that have been told by NPC,
        # if element od NPC speach list is in value of dict key,
        # key = quest name,
        # NPC tells next element on list
        self.quest_info = {}

        # hero.quest_condition_list stores info, if hero has completed quest
        # - if True - it affect on npc's statements and behaviour
        # list will expand by new info, while hero will execute quests:
        self.quest_condition_list = [""]  # *
        # * empty string in quest_condition_list is used in some quests, that..
        # should be automatically succesfull:
        # info quests, quests where task is to meet npc..

        # quest_blocked_list contains statements already heared (block it):
        self.quest_blocked_list = []

        # quest quest_completed_list contains quest names already finished:
        self.quest_completed_list = []
        
        # list with already killed enemies:
        # unique\special\quest enemies - blocked them for future
        self.enemy_killed = []

        
# HERO - import function ##############################

def import_hero():
    '''
    contains hero data to export to main:
    '''
    # start specs:
    hero = Hero()
    hero.new_location = 1  # variable used in change location mechanic
    hero.gold = 2  # initial wealt in pouch
    update_hero_parameters(hero)

    return hero


def update_hero_parameters(hero):
    '''
    update hero parameters:
    attack, defend, max_armour, combat_attribute
    use in main (or before combat)
    may add here other params to update
    '''
    hero.attack = attack_points_calc(hero)
    hero.defend = defend_points_calc(hero)
    hero.max_armour = amour_max_calc(hero)
    hero.combat_attribute = check_combat_attribute(hero)

    return hero


def dmg_points_calc(hero):
    ''' calculates hero min and max '''  # not implemented yet
    hero.dmg_list = [1, 4]


def attack_points_calc(hero):
    ''' calculates hero attack ability '''
    hero.attack = (
        2*hero.attrib_dict["siła"] +
        2*hero.attrib_dict["zwinność"] +
        hero.attrib_dict["inteligencja"]
        )

    return hero.attack


def defend_points_calc(hero):
    ''' calculates hero defend ability '''
    hero.defend = (
        3*hero.attrib_dict["zwinność"] + hero.attrib_dict["siła"]
        + hero.attrib_dict["inteligencja"] + hero.act_armour
        )

    return hero.defend


def exp_nextlvl(hero):
    '''
    calculate experience points required to achive next experience level
    '''
    return (50*hero.level)*2*hero.level


def amour_max_calc(hero):
    ''' calculates max armour points '''
    hero.max_armour = hero.attrib_dict["siła"]*3

    return hero.max_armour


def check_combat_attribute(hero):
    '''
    set default value of combat_attribute: 'siła' or 'zwinność'
    (depends on weapon in hand)
    if no weapon: deaoult attribut is higher attribut
    '''
    if hero.onbody_dict["prawa ręka"] == "":
        if hero.attrib_dict["siła"] >= hero.attrib_dict["zwinność"]:
            hero.combat_attribute = "siła"

        else:
            hero.combat_attribute = "zwinność"

    else:
        imported_item = mod_items.import_item(
            name=hero.onbody_dict["prawa ręka"]
            )

        hero.combat_attribute = imported_item.combat_attribute

    return hero.combat_attribute


def display_exp(hero):
    '''
    display actual exp and exp needed to achive next level
    '''
    nextLevel = exp_nextlvl(hero)

    return ''.join((str(hero.actualExp), '/', (str(nextLevel))))


def display_life(hero):
    '''
    display actual life points and max life points
    '''

    return ''.join((str(hero.actual_life), '/', (str(hero.max_life))))


def display_gold(hero):
    '''
    display gold (hero's wealth) in right format
    '''

    return ''.join((str(hero.gold), ' szt. złota'))


def display_location(hero):
    '''
    export hero location to display (used in display mod)
    '''
    if hero.location == 1:
        return "Niezmierzony Las"
    elif hero.location == 2:
        return "Kraina Trolli"
    elif hero.location == 3:
        return "Dymiąca Góra"
    elif hero.location == 4:
        return "Nawiedzone zamczysko"


def display_damage(hero):
    '''
    display hero's actual min and max damage
    '''
    return ''.join((str(hero.dmg_list[0]), '-', (str(hero.dmg_list[1]))))


def display_armour(hero):
    '''
    used to display actual and max armour points
    '''
    return ''.join((str(hero.act_armour), '/', (str(hero.max_armour))))


def items_list_to_dict(items_to_add):
    '''
    transform list of items to dictionary
    (used to update hero's inventory dict)
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
        # if it's new item = copy item to inventory
        if item not in hero_items:
            hero_items[item] = add_items[item]
        
        # if it's not new item = add item value to inventory
        elif item in hero_items:
            hero_items[item] += add_items[item]
        
        # if value inventory item is negativ number:
        # remove item from inventory*
        if int(hero_items[item]) < 1:
            del hero_items[item]

    # * we can use it in shops, when selling items..

    hero.inventory_dict = hero_items

    return hero


def dict_update(items_dict, add_remove_items_dict):
    '''
    update items_dict by add_remove_items_dict
    (operation on dicts with items, e.g.:
    {'milk': 1, 'bread': 3}
    key is item, value is item quantity)
    '''
    for item in add_remove_items_dict.keys():
        # if it's new item = copy item to inventory
        if item not in items_dict:
            items_dict[item] = add_remove_items_dict[item]
        
        # if it's not new item = add item value to inventory
        elif item in items_dict:
            items_dict[item] += add_remove_items_dict[item]

    return items_dict


def calendar(calendar_list):
    '''
    element of calendar mechanic - exports calendar elements to display
    '''
    week_list = [
        "poniedziałek", "wtorek", "środa", "czwartek",
        "piątek", "sobota", "niedziela"
        ]
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
      
        calendar_list[0] += 1
    del calendar_list[2]
      
    calendar_list.insert(2, time_of_day)
  
    return calendar_list


def quest(hero, npc=None):
    '''
    element of quest mechanic - block npc's statement, that have been said
    '''
    # hero.quest_info is dict that stores quest names (keys)
    # and npc statements (value of quest name key)
    # hero.quest_condition_list stores info, if hero has completed quest:
    # - if True - it affect on npc's statements and behaviour

    # if hero has finished quest before, just ignore rest:
    # if npc.quest_name not in hero.quest_completed_list:

    # if hero first time met npc and quest:
    if npc.quest_name not in hero.quest_info.keys():
        # create key with quest name and empty list (value) for npc's statement
        hero.quest_info.update({npc.quest_name: []})

        for element in npc.quest_list:
            if npc.quest_condition in hero.quest_condition_list:
                # add all statement (quest is completed):
                hero.quest_info[npc.quest_name].append(element)
            else:
                # add only first npc's statement:
                hero.quest_info[npc.quest_name].append(element)
                break

    # if hero has met npc before:
    else:
        for element in npc.quest_list:
            if npc.quest_condition in hero.quest_condition_list:
                if element not in hero.quest_info[npc.quest_name]:
                    # add all statement (quest is completed):
                    hero.quest_info[npc.quest_name].append(element)
            
            # if there is not any progress with quest
            # - npc doesn't say anything new besides small talk:
            else:
                break

    return hero


def next_level_promotion(hero):
    '''
    check if there is hero level promotion
    allows to player modify one of hero attributes
    displays result
    '''
    if hero.actualExp > ((50*hero.level)*2*hero.level):
        
        while True:
            player_choice = mod_display.display_next_level_promotion(hero)
            mod_display.display_hero_chart(hero)
            print("Awansujesz na kolejny poziom doświadczenia!\n")

            if player_choice == '1':
                hero.attrib_dict["siła"] += 1
                print("Gratulacje! Wzrosła siła i życie")
                mod_display.pause()
                break
            elif player_choice == '2':
                hero.attrib_dict["zwinność"] += 1
                print("Gratulacje! Wzrosła zwinność i życie")
                mod_display.pause()
                break
            elif player_choice == '3':
                hero.attrib_dict["percepcja"] += 1
                print("Gratulacje! Wzrosła percepcja i życie")
                mod_display.pause()
                break
            elif player_choice == '4':
                hero.attrib_dict["inteligencja"] += 1
                print("Gratulacje! Wzrosła inteligencja i życie")
                mod_display.pause()
                break
            elif player_choice == '5':
                hero.attrib_dict["siła woli"] += 1
                print("Gratulacje! Wzrosła siła woli i życie")
                mod_display.pause()
                break
            else:
                print("Wybierz numer atrybutu, spróbuj jeszcze raz.. ")
                mod_display.pause()
                continue
        
        hero.level += 1
        hero.max_life += 30  # buff to max life
        hero.actual_life = hero.max_life  # full life regeneration 
                
    return hero


def check_item_condition_quest(hero, npc=None):
    '''
    check if hero has items to finish quest (if it is quest condition):
    '''
    # npc.quest_items stores quest items forming quest condition:
    if len(npc.quest_items) > 0:
        
        # if hero hasn't fullfilled quest condition yet:
        if npc.quest_condition not in hero.quest_condition_list:
            # create list of npc quest condition items
            # and items in hero inventory: 
            npc_compare_list = [key for key in npc.quest_items.keys()]
            # hero_compare_list contains only that items, which are in npc dict
            # and quantity that items is >= quantity items in npc dict:
            hero_compare_list = [
                key for key in hero.inventory_dict.keys()
                if key in npc.quest_items.keys()
                and
                hero.inventory_dict[key] >= abs(npc.quest_items[key])
                ]
            
            # compare lists (have they same contant?):
            if npc_compare_list == hero_compare_list:
                # if true - add info, that hero has fulfilled quest condition:
                hero.quest_condition_list.append(npc.quest_condition)

                return hero
