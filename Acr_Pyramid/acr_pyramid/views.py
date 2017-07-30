from pyramid.view import view_config
from db_connect import connect

class Views(object):
    
    def __init__(self, request):
        self.request = request
        
    @view_config(route_name='home', renderer='templates/mytemplate.jinja2')
    def my_view(self):
        return {'project': 'Acr_Pyramid'}

    @view_config(route_name='submit_crash_form', renderer='templates/submit_crash.jinja2')
    def my_view1(self):
        return {'project': 'Acr_Pyramid'}
    
    @view_config(route_name='submit_crash', renderer='templates/submit_crash.jinja2')
    def submit_crash(self):
        print "nitin"
        print self.request.params.get("crashcontent")
        #print self.request.params['crashcontent']
        print "nitin"
        return {'project': 'Acr_Pyramid'}
