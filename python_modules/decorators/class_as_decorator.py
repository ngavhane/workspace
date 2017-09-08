class ClassAsDecorator(object):
    
    def __call__(self, func):
        def print_info(self, *inargs, **kwargs):
            func(self, *inargs, **kwargs)
            print "I am in __call__ methos of the ClassAsDecorator method"
        return print_info
    

class TestDecorator(object):
    
    def __init__(self):
        pass

    @ClassAsDecorator()
    def print_data(self, name):
        print "I am in print data function of TestDecorator class"

t = TestDecorator()
t.print_data("nitin")
