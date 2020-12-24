""" This File manages the generation of a single map segment

this file contains following functions:
    create_map_base - returns the map list of lists

"""
import json
from configparser import ConfigParser
from random import randint
from TA_Data.src.makemapblueprint import create_map_base
from TA_Data.src.TA_Errors import NotARaceError
from TA_Data.src.module_ta import Logger
        
Logger = Logger()
config = ConfigParser()
config.read('TA_Data\\game_data\\mapgeneration.ini')
size = int(config.get("DUNGEON_MAP_GENERATION", "DUNGEON_MAP_SIZE"))
prob_one = int(config.get("DUNGEON_MAP_GENERATION", "ENEMIES_PROBABILLITY"))
prob_mult = int(config.get("DUNGEON_MAP_GENERATION", "ENEMIES_AMOUNT_PROBABILLITY"))
max = int(config.get("DUNGEON_MAP_GENERATION", "ENEMIES_MAX_AMOUNT"))


def create_new_map_segment():

    map = create_map_base(size)
    Logger.all_log("map bluprint found" + Logger.lineno())
    set_enimies(map, prob_one, prob_mult, max)
    Logger.all_log("map segment has been populated with enimies")
    return map


def set_enimies(map, prob_one=50, prob_mult=10 , max=4):
    """ This function spawns the enimies onto the map fields"""
    
    # for every colum in the map
    for x in range(len(map)):
        for y in range(len(map[x])):
            enemycout = 0
            run = True
            if randint(0, 100/prob_one) == 1:
                enemycout = 1
                while run and enemycout < max:
                    if randint(0, 100/prob_mult) == 1:
                        enemycout += 1
                    else:
                        run = False
            enemy_list = []
            for count in range(enemycout):
                enemy_list.append(enemy_picker())
            
            map[x][y].append(enemy_list)


def enemy_picker(restriction=None):
    configer = ConfigParser()

    configer.read('TA_Data\\game_data\\META_data\\Enemies_data.ini')

    enemy_races = json.loads(configer.get("ENEMIES", "ENEMY_TYPES")) 
    if restriction is not None:
        try:
            enemy_races = list(set(enemy_races) - set(restriction))

        except:
            raise NotARaceError("Restriction " + restriction + " is not an enemy race")

    enemy_race = enemy_races[randint(0, len(enemy_races) - 1)]

    possible_enemies = json.loads(configer.get(enemy_race, enemy_race))

    enemy = possible_enemies[randint(0, len(possible_enemies) -1)]

        
    return enemy[1]

