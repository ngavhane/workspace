from crash_helpers import Crashhelpers

class MatchHelpers(object):
    def __init__(self):
        self.crash_helper = Crashhelpers()

    def check_if_crash_matches_with_signature(self, crash_uuid, signature_uuid):
        crash = self.crash_helper.get_crash(crash_uid=crash_uuid)
        signature = self.crash_helper.get_signature(signature_uuid=signature_uuid)
        print "Crash under the test is : %s" % crash
        print "Signature under test is : %s" % signature
        if signature['signature_content'] in crash['crash_content']:
            return True
        else:
            return False
    
    def number_of_crashes_matching_with_signature(self, signature_uuid):
        count = 0
        signature = self.crash_helper.get_signature(signature_uuid=signature_uuid)
        all_crashes = self.crash_helper.list_all_crashes_from_db()
        for crash in all_crashes:
            if self.check_if_crash_matches_with_signature(crash['uuid'], signature['uuid']):
                count += 1
        return count
