import requests
from .exceptions import RateLimit

class getItem():
    def __init__(self, id):
        itemdetails = requests.get("https://www.rolimons.com/itemapi/itemdetails").json()
        if not itemdetails['success']:
            raise RateLimit('Rate limit exceeded')
        # [item_name, acronym, rap, value, default_value, demand, trend, projected, hyped, rare]

        self.id = str(id)
        self.name = itemdetails['items'][str(id)][0]
        self.acronym = itemdetails['items'][str(id)][1]
        self.rap = itemdetails['items'][str(id)][2]
        self.value = itemdetails['items'][str(id)][3]
        self.default_value = itemdetails['items'][str(id)][4]
        self.demand = itemdetails['items'][str(id)][5]
        self.trend = itemdetails['items'][str(id)][6]
        self.projected = itemdetails['items'][str(id)][7]
        self.hyped = itemdetails['items'][str(id)][8]
        self.rare = itemdetails['items'][str(id)][9]

class getLimiteds(): # raw = True
    def __init__(self):
        itemdetails = requests.get("https://www.rolimons.com/itemapi/itemdetails").json()
        if not itemdetails['success']:
            raise RateLimit('Rate limit exceeded')
        # [item_name, acronym, rap, value, default_value, demand, trend, projected, hyped, rare]

        self.id = [str(item) for item in itemdetails['items']]
        self.name = [itemdetails['items'][str(item)][0] for item in itemdetails['items']]
        self.acronym = [itemdetails['items'][str(item)][1] for item in itemdetails['items']]
        self.rap = [itemdetails['items'][str(item)][2] for item in itemdetails['items']]
        self.value = [itemdetails['items'][str(item)][3] for item in itemdetails['items']]
        self.default_value = [itemdetails['items'][str(item)][4] for item in itemdetails['items']]
        self.demand = [itemdetails['items'][str(item)][5] for item in itemdetails['items']]
        self.trend = [itemdetails['items'][str(item)][6] for item in itemdetails['items']]
        self.projected = [itemdetails['items'][str(item)][7] for item in itemdetails['items']]
        self.hyped = [itemdetails['items'][str(item)][8] for item in itemdetails['items']]
        self.rare = [itemdetails['items'][str(item)][9] for item in itemdetails['items']]
