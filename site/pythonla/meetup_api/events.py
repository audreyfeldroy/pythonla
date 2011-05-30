import json
import requests

import utils
import settings

url = settings.BASE_URL + 'events.json'

get_data = dict(
    group_urlname=settings.GROUP_NAME,
    key=settings.API_KEY,
)

def get_events():
    '''
    Get a blob of events data and return a recurisve DictObject of the same.
    '''
    r = requests.get(url, get_data)
    if r.status_code == 200:
        data = json.loads(r.content)
        obj = utils.recursive_dictobject(data)
    else:
        raise Exception()
    
    for event in obj.results:
        print event.name + ":", event.lat, event.lon

    return obj
