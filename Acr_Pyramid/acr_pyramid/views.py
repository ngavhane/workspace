import uuid
from pyramid.view import view_config
from db_connect import connect
from crash_helpers import Crashhelpers

class Views(object):

    def __init__(self, request):
        self.request = request
        self.handle = connect()
        self.crash_helper = Crashhelpers()

    @view_config(route_name='home', renderer='templates/mytemplate.jinja2')
    def my_view(self):
        return {'project': 'Acr_Pyramid'}

    @view_config(route_name='submit_crash_form', renderer='templates/submit_crash.jinja2')
    def my_view1(self):
        return {'project': 'Acr_Pyramid'}

    @view_config(route_name='submit_crash', renderer='templates/list_crashes.jinja2')
    def submit_crash(self):
        crash_content = self.request.params.get("crashcontent")
        crash_name = self.request.params.get("crashname")
        self.handle.mycollection.insert_one(
            {"crash_content": crash_content, "entity_type": "crash", 'is_classified': False,
             "crash_name": crash_name, "uuid": str(uuid.uuid4())})
        all_crashes = self.crash_helper.list_all_crashes_from_db()
        return {'crash_list': all_crashes}

    @view_config(route_name='list_crashes', renderer='templates/list_crashes.jinja2')
    def list_crashes(self):
        all_crashes = self.crash_helper.list_all_crashes_from_db()
        return {'crash_list': all_crashes}

    @view_config(route_name='delete_crashes', renderer='templates/list_crashes.jinja2')
    def delete_crashes(self):
        self.handle.mycollection.drop()
        return {'project': 'Acr_Pyramid'}

    @view_config(route_name='submit_signature_form', renderer='templates/submit_signature.jinja2')
    def my_view1(self):
        return {'project': 'Acr_Pyramid'}

    @view_config(route_name='submit_signature', renderer='templates/list_signatures.jinja2')
    def submit_signature(self):
        signature_content = self.request.params.get("signaturecontent")
        signature_type = self.request.params.get("signaturetype")
        self.handle.mycollection.insert_one(
            {"signature_content": signature_content, "entity_type": "signature",
             "signature_type": signature_type, 'uuid': str(uuid.uuid4())})
        all_signature = self.crash_helper.list_all_signature_from_db()
        return {'signature_list': all_signature}

    @view_config(route_name='list_signatures', renderer='templates/list_signatures.jinja2')
    def list_signatures(self):
        all_signature = self.crash_helper.list_all_signature_from_db()
        return {'signature_list': all_signature}

    @view_config(route_name='get_crash', request_method='GET', renderer='templates/single_crash_view.jinja2')
    def my_view(self):
        crash_uid = str(self.request.matchdict['crash_uuid'])
        crash = self.crash_helper.get_crash(crash_uid=crash_uid)
        return {'crash_name': crash['crash_name'], 'crash_uuid': crash['uuid'],
                'crash_content': crash['crash_content'], 'is_crash_classified': crash['is_classified']}
