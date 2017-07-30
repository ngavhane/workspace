from pyramid.view import view_config
from db_connect import connect

class Views(object):
    
    def __init__(self, request):
        self.request = request
        self.handle = connect()
        
    @view_config(route_name='home', renderer='templates/mytemplate.jinja2')
    def my_view(self):
        return {'project': 'Acr_Pyramid'}

    @view_config(route_name='submit_crash_form', renderer='templates/submit_crash.jinja2')
    def my_view1(self):
        return {'project': 'Acr_Pyramid'}
    
    @view_config(route_name='submit_crash', renderer='templates/submit_crash.jinja2')
    def submit_crash(self):
        crash_content = self.request.params.get("crashcontent")
        self.handle.mycollection.insert_one({"crash_content": crash_content})
        return {'project': 'Acr_Pyramid'}

    @view_config(route_name='list_crashes', renderer='templates/submit_crash.jinja2')
    def list_crashes(self):
        for info in self.handle.mycollection.find():
            print info
        return {'project': 'Acr_Pyramid'}

    @view_config(route_name='delete_crashes', renderer='templates/submit_crash.jinja2')
    def delete_crashes(self):
        self.handle.mycollection.drop()
        return {'project': 'Acr_Pyramid'}
