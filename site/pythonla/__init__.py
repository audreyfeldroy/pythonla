from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from pythonla.models import initialize_sql

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_route('home', '/', view='pythonla.views.my_view',
                                 view_renderer='templates/mytemplate.jinja2')
    return config.make_wsgi_app()


