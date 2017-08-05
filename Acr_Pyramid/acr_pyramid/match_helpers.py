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
