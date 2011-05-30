from pyramid_beaker import (session_factory_from_settings, 
                            set_cache_regions_from_settings)

from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from pythonla.models import initialize_sql

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    session_factory = session_factory_from_settings(settings)
    set_cache_regions_from_settings(settings)
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_route('home', '/', view='pythonla.views.my_view',
                                 view_renderer='templates/mytemplate.jinja2')
    config.begin()
    config.set_session_factory(session_factory)
    config.end()
    return config.make_wsgi_app()


