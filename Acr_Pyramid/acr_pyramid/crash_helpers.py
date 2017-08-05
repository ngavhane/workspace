from db_connect import connect


class Crashhelpers(object):
    def __init__(self):
        self.handle = connect()

    def list_all_crashes_from_db(self):
        crash_list = []
        for info in self.handle.mycollection.find():
            print info
            if info['entity_type'] == "crash":
                crash_list.append(info)
        return crash_list
    
    def list_all_signature_from_db(self):
        signature_list = []
        for info in self.handle.mycollection.find():
            print info
            if info['entity_type'] == "signature":
                signature = info['signature_type'] + " | " + info['signature_content']
                signature_list.append(signature)
        return signature_list

    def get_crash(self, crash_uid):
        for info in self.handle.mycollection.find():
            if info["uuid"] == crash_uid:
                return info
        raise Exception("There is no crash in the system with uuid : %s" % crash_uid)
