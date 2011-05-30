from pythonla.models import DBSession
from pythonla.models import MyModel
from pyramid.view import view_config

from meetup_api.meetup import Meetup
meetup = Meetup()

@view_config(route_name='home', renderer='templates/home.jinja2')
def home(request):
    return {'breadcrumbs': [
            {'item': 'Home', 'caption' : 'Home'}
           ]}

@view_config(route_name='members', renderer='templates/members.jinja2')
def members_view(request):
    members = meetup.get_members()
    return {'breadcrumbs': [
            {'item': 'Members', 'caption' : 'Members'}
           ], 'members': members}

@view_config(route_name='events', renderer='templates/events.jinja2')
def events_view(request):
    events = meetup.get_events()
    return {'breadcrumbs': [
            {'item': 'Events', 'caption' : 'Events'}
           ], 'events': events}

@view_config(route_name='map', renderer='templates/map.jinja2')
def map_view(request):
    members = meetup.get_members()
    events = meetup.get_events()    
    return {'breadcrumbs': [
            {'item': 'Map', 'caption' : 'Map'}
           ], 'members': members,
            'events': events}
