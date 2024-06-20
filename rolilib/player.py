import requests
from .exceptions import PlayerNotFound

class player():
    def __init__(self, player = None):
        if str(player).isdigit():
            self.id = str(player)
            self.getPlayerInfo(self.id)
        else:
            request = requests.get(f'https://api.rolimons.com/players/v1/playersearch?searchstring={player}').json()
            if request['players']:
                for item in request['players']:
                    if player == item[1]:
                        self.id = item[0]
                        self.getPlayerInfo(self.id)
                    else:
                        raise PlayerNotFound(f'Player {player} not found!')
            else:
                raise PlayerNotFound(f'Player {player} not found!')

    def getPlayerInfo(self, id):
        request = requests.get(f'https://api.rolimons.com/players/v1/playerinfo/{id}').json()
        self.name = request['name']
        self.value = request['value']
        self.rap = request['rap']
        self.rank = request['rank']
        self.premium = request['premium']
        self.privacy_enabled = request['privacy_enabled']
        self.terminated = request['terminated']
        self.stats_updated = request['stats_updated']
        self.last_scan = request['last_scan']
        self.last_online = request['last_online']
        self.last_location = request['last_location']
