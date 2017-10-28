import datetime
class Employee(object):

    def __new__(cls, *args, **kwargs):
        new_instance = object.__new__(cls, *args, **kwargs)
        setattr(new_instance, 'created_at', datetime.datetime.now())
        return new_instance
        print "in new method of Employee class"
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def print_data(self):
        print self.x
        print self.y
        print self.created_at

e = Employee("sds", 89)
e.print_data()
