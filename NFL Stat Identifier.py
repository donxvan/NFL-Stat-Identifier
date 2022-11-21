import 
from  import 
from import 
import time
import shutil
import re
import os
import json
import string
import glob


BASE_URL = 'https://www.pro-football-reference.com{0}'
PLAYER_LIST_URL = 'https://www.pro-football-reference.com/players/{0}'
PLAYER_PROFILE_URL = 'https://www.pro-football-reference.com/players/{0}/{1}'
PLAYER_GAMELOG_URL = 'https://www.pro-football-reference.com/players/{0}/{1}/gamelog/{2}'

class 
  
class NFLPassingStats(NFLStats):  
    def keys(): 
        return [ 'id', 'player_id', 'name', "side", 'ints', 'cmp', 'twoptm', 'yds', 'att', 'tds', "twopta"]
class NFLReceivingStats(NFLStats):
    def keys(): 
        return [ 'id', 'player_id', 'name', "side", 'twoptm', 'rec', 'yds', 'lngtd', 'tds', 'lng', 'twopta']
class NFLRushingStats(NFLStats):
    def keys(): 
        return ['id', 'player_id', 'name', "side", 'lngtd', 'twoptm', 'yds', 'att', 'tds', 'lng', 'twopta']
