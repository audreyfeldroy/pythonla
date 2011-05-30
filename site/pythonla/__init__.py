from pyramid_beaker import session_factory_from_settings
from pyramid_beaker import set_cache_regions_from_settings

from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from pythonla.models import initialize_sql

def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.
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

    # 
    config.include('pyramid_jinja2')

    config.begin()
    config.set_session_factory(session_factory)
    config.end()



    config.include(basic_routes)
    config.scan()
    return config.make_wsgi_app()


def basic_routes(config):
    # home page
    config.add_route('home', '/', view='pythonla.views.home')
    # members
    config.add_route('members', '/members', view='pythonla.views.members_view')
	# events
    config.add_route('events', '/events', view='pythonla.views.events_view')
	# map
    config.add_route('map', '/map', view='pythonla.views.map_view')

