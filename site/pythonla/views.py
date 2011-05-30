from pythonla.models import DBSession
from pythonla.models import MyModel
from pyramid.view import view_config

from meetup_api.meetup import Meetup
meetup = Meetup()

@view_config(renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'foo': 1, 'bar': 2}

@view_config(renderer='templates/members.jinja2')
def members_view(request):
    members = meetup.get_members()
    return {'members': members}

@view_config(renderer='templates/events.jinja2')
def events_view(request):
    events = meetup.get_events()
    return {'events': events}
