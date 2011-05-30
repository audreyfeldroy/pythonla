# beaker and pyramid_beaker
from pyramid_beaker import session_factory_from_settings
from pyramid_beaker import set_cache_regions_from_settings

# pyramid config
from pyramid.config import Configurator

# models/sqlalchemy config intialization
from sqlalchemy import engine_from_config
from pythonla.models import initialize_sql

# helper library for templates
from pyramid.events import BeforeRender
from pythonla import helpers


def main(global_config, **settings):
    """
    Configure Pyramid WSGI application and return aWSGI object
    """

    # SQLAlchemy
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)

    # begin beaker setup
    session_factory = session_factory_from_settings(settings)
    set_cache_regions_from_settings(settings)

    # basic config
    config = Configurator(settings=settings)

    # static url setup
    config.add_static_view('static', 'pythonla:static')

    # include jinja2 using pyramid_jinaj2
    config.include('pyramid_jinja2')
    config.include(basic_routes)

    # wrap up beaker
    config.begin()
    config.set_session_factory(session_factory)

    # end config
    config.end()

    # scan for view configs
    config.scan()

    # register varienty of renderer globals
    config.add_subscriber(add_renderer_globals, BeforeRender)

    return config.make_wsgi_app()


def basic_routes(config):
    """
    Basic routes used by the app.
    """
    # home page
    config.add_route('home', '/', view='pythonla.views.home')
    # members
    config.add_route('members', '/members', view='pythonla.views.members_view')
    # events
    config.add_route('events', '/events', view='pythonla.views.events_view')
    # map
    config.add_route('map', '/map', view='pythonla.views.map_view')


def add_renderer_globals(event):
    """
   Add global render globals such as:
    - helpers library as 'h'
    http://docs.pylonsproject.org/projects/pyramid_cookbook/dev/templates.html
    """
    event['h'] = helpers
