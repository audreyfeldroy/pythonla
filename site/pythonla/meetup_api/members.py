import json
import requests

import utils
import settings

url = settings.BASE_URL + 'members.json'

get_data = dict(
    group_urlname=settings.GROUP_NAME,
    key=settings.API_KEY,
)

def get_members():
    '''
    Get a blob of member data and return a recurisve DictObject of the
    same.
    '''
    r = requests.get(url, get_data)
    if r.status_code == 200:
        data = json.loads(r.content)
        obj = utils.recursive_dictobject(data)
    else:
        raise Exception()
    
    for member in obj.results:
        print member.name + ":", member.lat, member.lon

    return obj
