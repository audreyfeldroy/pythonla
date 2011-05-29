import json
import requests

from settings import API_KEY, GROUP_NAME

base_url = "https://api.meetup.com/members.json"

group_name = "lapython"
get_data = dict(
    group_urlname=GROUP_NAME,
    key=API_KEY
    )

def get_members():
    
    r = requests.get(base_url, get_data)
    if r.status_code == 200:
        data = json.loads(r.content)
    else:
        raise Exception()
    
    for member in data['results']:
        print member['lat'], member['lon']
        
get_members()
