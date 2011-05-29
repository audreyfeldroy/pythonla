from pythonla.models import DBSession
from pythonla.models import MyModel
from pyramid.view import view_config


@view_config(renderer='templates/mytemplate.jinja2')
def my_view(request):
        return {'foo': 1, 'bar': 2}
