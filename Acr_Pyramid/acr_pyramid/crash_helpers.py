from db_connect import connect

class Crashhelpers(object):
    def __init__(self):
        self.handle = connect()

    def list_all_crashes_from_db(self):
        crash_list = []
        for info in self.handle.mycollection.find():
            crash_list.append(info['crash_content'])
        return crash_list
