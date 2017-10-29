
class Stack(object):
    def __init__(self, initial=[]):
        self.holder = initial

    def push(self, element):
        self.holder.append(element)

    def pop(self):
        self.holder.pop()

    def show_data(self):
        for element in self.holder:
            print element



s = Stack([1,2])
s.push(3)
s.pop()
s.show_data()
print "***"
s.pop()
s.show_data()
print "***"
s.push(10)
s.push(15)
s.show_data()
print "***"