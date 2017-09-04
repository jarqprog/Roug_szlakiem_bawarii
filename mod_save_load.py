# mod contains save game / load game functions

import pickle


def export_hero(hero = None, filename = None):
    '''export 'hero' object to file'''
    with open(filename, "wb") as file_:
        pickle.dump(hero, file_, -1)


def import_hero(importfilename = None):
    '''import 'hero' object to file'''
    hero = pickle.load(open(importfilename, "rb", -1))

    return hero