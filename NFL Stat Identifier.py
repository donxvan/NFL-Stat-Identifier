BASE_URL = 'https://www.pro-football-reference.com{0}'
PLAYER_LIST_URL = 'https://www.pro-football-reference.com/players/{0}'
PLAYER_PROFILE_URL = 'https://www.pro-football-reference.com/players/{0}/{1}'
PLAYER_GAMELOG_URL = 'https://www.pro-football-reference.com/players/{0}/{1}/gamelog/{2}'



class NFLStats(object):
  
class NFLPassingStats(NFLStats):
    @staticmethod
    def keys(): 
        return [ 'id', 'player_id', 'name', "side", 'ints', 'cmp', 'twoptm', 'yds', 'att', 'tds', "twopta"]
