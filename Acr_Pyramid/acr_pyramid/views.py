from pyramid.view import view_config
from db_connect import connect

@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'Acr_Pyramid'}

@view_config(route_name='submit_crash', renderer='templates/submit_crash.jinja2')
def my_view1(request):
    return {'project': 'Acr_Pyramid'}
