
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
    
    
e=Employee("nitin", "gavhane")
e.fname="pqr"
print e.email
e.full_name = "Niteen Gavhane"
del e.full_name

