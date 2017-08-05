from db_connect import connect

class Crashhelpers(object):
    def __init__(self):
        self.handle = connect()

    def list_all_crashes_from_db(self):
        crash_list = []
        for info in self.handle.mycollection.find():
            print info
            if info['entity_type'] == "crash":
                crash_list.append(info['crash_content'])
        return crash_list
    
    def list_all_signature_from_db(self):
        signature_list = []
        for info in self.handle.mycollection.find():
            print info
            if info['entity_type'] == "signature":
                signature = info['signature_type'] + " | " + info['signature_content']
                signature_list.append(signature)
        return signature_list
