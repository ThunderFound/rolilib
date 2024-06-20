import requests
from .exceptions import RateLimit

class utils():
    def getLimiteds(type= 'id'): # raw = True
        itemdetails = requests.get("https://www.rolimons.com/itemapi/itemdetails").json()
        if not itemdetails['success']:
            raise RateLimit('Rate limit exceeded')
        # [item_name, acronym, rap, value, default_value, demand, trend, projected, hyped, rare]

        output = []
        if type == 'id':
            for item in itemdetails['items']:
                output.append(str(item))
        elif type == 'all':
            output = itemdetails['items']
        else:
            for item in itemdetails['items']:
                output.append(itemdetails['items'][str(item)][utils.__typeToIndex__(type)])

        #if not raw:
        #    output = utils.__enhance__(output)

        return output
    def __enhance__(item):
        if type(item) is list:
            for index, value in enumerate(item):
                if value == -1 or value == '':
                    item[index] = None

            return item
        else:
            if item == -1 or item == '':
                return None
            else:
                return item

    def __typeToIndex__(type):
        if type == 'name':
            return 0
        elif type == 'acronym':
            return 1
        elif type == 'rap':
            return 2
        elif type == 'value':
            return 3
        elif type == 'default_value':
            return 4
        elif type == 'demand':
            return 5
        elif type == 'trend':
            return 6
        elif type == 'projected':
            return 7
        elif type == 'hyped':
            return 8
        elif type == 'rare':
            return 9
        else:
            return 0
