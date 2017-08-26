
class Employee(object):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        #self.email = fname + lname + "@gmail.com"
    
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.fname, self.lname)

    @property
    def full_name(self):
        return '{} {}'.format(self.fname, self.lname)
    
    @full_name.getter
    def full_name(self):
        return '{} {}'.format(self.fname, self.lname)
    
    @full_name.setter
    def full_name(self, fullname):
        fname, lname = fullname.split(" ")
        self.fname=fname
        self.lname = lname

    @full_name.deleter
    def full_name(self):
        self.fname = None
        self.lname = None
    
    def print_data(self):
        print self.fname
        print self.lname
        print self.email
        print self.full_name
        self.full_name = "san jose"
        print self.full_name
    
    
e=Employee("nitin", "gavhane")
e.fname="pqr"

e.print_data()
print e.full_name

print e.email
