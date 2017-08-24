# Szlakiem Bawarii - plik roboczy Jarka


class Hero:
    def __init__(self, name, proffession, attack, agility, defence, life_point, life_point_max, xp_point, xp_lvl): #add "Siła Woli", "Inteligencja"
        self.name = name
        self.proffession = proffession
        self.attack = attack
        self.agility = agility
        self.defence = defence
        self.life_point = life_point
        self.life_point_max = life_point_max
        self.xp_point = xp_point
        self.xp_lvl = xp_lvl


player_character = Hero("Rabarbar","Zbójcerz",1,1,1,2,20,0,1)

hero_list = []
def __init__(self, Hero):
    hero_list.append(self)
    print(hero_list)



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

wolf = Enemy("wilk", 1, 3, 1, 10, "animal", 5, 1, None, "Wrrrrr!")
bear = Enemy("niedźwiedź", 2, 1, 3, 30, "animal", 15, 2, None, "Mrrrrrruummm!")
troll = Enemy("troll", 2, 1, 3, 30, "beast", 15, 2, "Kamienna skóra - trolla ciężko ubić", "Co Ty chcieć?!")

def prints_hero_attributes(Hero):
    print(player_character.name)

def prints_enemy_attributes(enemy=None):
    '''
    just4fun&test
    '''
    if enemy.genre == "animal":
        print("Jestem zwierzakiem, nie zabijajcie mnie! Jestem", enemy.name, "!")
    else:
        print("Zginiesz, głupcze!")

    if enemy.life_point < 20:
        print("Mam niską wytrzymałość!")
    else:
        print("Nie jestem taki słaby!")
    enemy = troll
    print(enemy.speach, enemy.specials)


def display_hero(Hero):
    '''
    prints player character simple Chart
    '''
#def __init__(self, name, proffession, attack, agility, defence, life_point, life_point_max, xp_point, xp_lvl
    print("\nCechy Postaci:\n")
    print("Imię:", player_character.name) #imię
    print("Klasa:", player_character.proffession) #klasa
    print("Atak:", player_character.attack)
    print("Zwinność:", player_character.agility)
    print("Obrona:", player_character.defence)
    print("Życie:", player_character.life_point, "/", player_character.life_point_max)
    print("Doświadczenie:", player_character.xp_point, "/ Poziom:", player_character.xp_lvl)
'''
    for i in player_character():
        print(i)
'''
'''
 count = 0
    total_number_of_items = 0
    for item in inventory:
        total_number_of_items += int(inventory[item])
# checks lenght of the string:
        if len(item) > count:
            count = len(item)
            longest_arg = item
    lenght_in_printing = int(len(longest_arg)) # variable used below, helps correctly print table:
    print("\nInventory: \n\n", "count".rjust(6)
prints_hero_attributes(Hero)
prints_enemy_attributes(troll)
player_character = Hero("Rabarbar","Zbójcerz",1,1,1,2,20,0,1)
'''

def main():
    player_character = Hero("Rabarbar","Zbójcerz",1,1,1,2,20,0,1)
    prints_enemy_attributes(troll)
    display_hero(Hero)
    __init__(player_character)


main()
