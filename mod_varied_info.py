# mod_varied_info - custom mod, contains list of short messages to random display in main:

import random, time


def dot_loop():
    '''
    display animated dot ('.'): . -> .. -> ... 
    '''

    for i in ('...'):        
        print(i, end='', flush=True)
        time.sleep(.2)


def display_varied_info():
    '''
    function with a list of short messages (mainly to increse playability). It random generates message to display from list:
    '''
    info_to_display_list = [
    "Zapowiada się piękny dzień", "Zbiera się na burzę", "Noc była chłodna, ale poranek słoneczny i ciepły",
    "Mam przeczucie, że coś się wydarzy",
    "Jest bezpiecznie",



    "Porada: sklep na mapce oznaczony jest literką 'S'", "Porada: symbol '?' oznacza zagadkowe zdarzenie - kto wie, co to może być?"

    ]


    info_to_display = info_to_display_list[random.randint(0, len(info_to_display_list)-1)]

    return print(info_to_display, end=''), dot_loop()

