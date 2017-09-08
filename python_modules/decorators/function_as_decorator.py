def comany_name_wrapper(func):
    def wrap_c_name(x):
        func(x)
        print x
        print x.fname
        print x.lname
        print type(x)
        print "xyz"
    return wrap_c_name
    


class Member(object):
    def __init__(self, fname, lname):
        print "In init function of Member clasas"
        self.fname = fname
        self.lname = lname

    @comany_name_wrapper
    def print_name(self):
        print "In print name function"
        print self.fname + self.lname
        
    
m= Member("nitin", "gavhane")
m.print_name()
