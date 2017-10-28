class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return "%s is %d" %(self.name, self.age)
class PersonDecorator(Person):
    def __init__(self, person):
        self._person = person
    def __getattr__(self, name):
        return getattr(self._person, name)
    def __str__(self):
        age = self._person.age
        color = "white"
        if age  <=30:
            color = "red"
        else:
            color = "blue"
        return "%s%s" %(color, self._person.__str__())
p=[]
p.append(Person("nitin", 26))
p.append(Person("xyz", 52))
for person in p:
    person = PersonDecorator(person)
    print person
