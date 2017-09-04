import random
import string
from msvcrt import getch

def hot_warm_cold():
    sekwencja_do_gry = []
    for i in range(3):
        string.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        losowa_liczba = random.choice(range(9))
        losowa_litera1 = random.choice(string.letters)
        losowa_litera2 = random.choice(string.letters)
        losowa_litera3 = random.choice(string.letters)
        wybór_do_gry = [str(losowa_liczba), losowa_litera1, losowa_litera2, losowa_litera3]
    for i in range(3):
        sekwencja_do_gry.append(random.choice(wybór_do_gry))
    while True:
        wybór_trudności = input("\nWybierz poziom trudnośći. Wciśnij 1, 2 lub 3 dla kolejno: łatwy, trudny, życzenie śmierci.:")
        if wybór_trudności == "1":
            print("\nMasz 15 prób.")
            wybór_trudności = 15
            break
        if wybór_trudności == "2":
            print("\nMasz 15 prób.")
            wybór_trudności = 10
            break
        if wybór_trudności == "3":
            print("\nMasz 15 prób.")
            wybór_trudności = 5
            break
        else:
            print("\nPOWIEDZIAŁEM 1, 2 lub 3 !!!")
    print("\nPomyślałem o 3 elementowym miksie cyfr i liter. Zgadnij!")
    print("Pamietaj:")
    print("Jak mówie", " " * 5, "to znaczy, że:\n")
    print("Zimno", " " * 9, "nie zgadłeś")
    print("Ciepło", " " * 8, "zgadłeś ale w złych pozycjach")
    print("Gorąco", " " * 8, "co najmniej jeden element jest dobrze i w dobrej pozycji.")
    for i in range(wybór_trudności):
        próba = input("--->")
        próba = list(próba.upper())
        if próba == sekwencja_do_gry:
            return "Brawo !!!"
        else:
            if len(próba) > 3:
                print("Chyba zapomniałeś, że zgadujesz tylko 3 elementy.....")
                continue
            i = 0
            podpowiedzi = []
            for i in range(len(próba)):
                if próba[i] in sekwencja_do_gry:
                    if próba[i] == sekwencja_do_gry[i]:
                        podpowiedzi.append("Gorąco")
                    else:
                        podpowiedzi.append("Ciepło")
                else:
                    podpowiedzi.append("Zimno")
                i += 1
            lista_podpowiedzi = []
            for i in range(podpowiedzi.count("Gorąco")):
                lista_podpowiedzi.append("Gorąco")
            for i in range(podpowiedzi.count("Ciepło")):
                lista_podpowiedzi.append("Ciepło")
            for i in range(podpowiedzi.count("Zimno")):
                lista_podpowiedzi.append("Zimno")
            print(" ".join(lista_podpowiedzi))
            continue
    return "\nNie zgadłeś !!!"
    


a = hot_warm_cold()
print(a)