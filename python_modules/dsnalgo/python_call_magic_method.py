class Person(object):
    def __init__(self):
        print "in __init class"
    def __call__(self, name, age):
        self.name = name
        self.age = age
        if self.age > 45:
            print "person is older"
        else:
            print "person is youger"
    def print_data(self):
        print self.name
        print self.age

p = Person()
p("xyz", 54)
print vars(p)

