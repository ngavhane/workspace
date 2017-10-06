class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return "%s is %d" %(self.name, self.age)
p=[]
p.append(Person("nitin", 26))
p.append(Person("xyz", 52))
for person in p:
    print person
