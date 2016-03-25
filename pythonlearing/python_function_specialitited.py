
print "1.A python function can be asssigned to a variable"
def printName():
    print "My name is nitin"
xyz=printName
xyz()    #This executs the function
printName()  #This also executes the Function

print "2.A function can be defined inside other function"

def greet(name):
    def printHello():
        return "Hello"
    res=printHello()+name
    return res
print greet("nitin")

print "##################################"

print "3.A function can be passed as parameter to any other function"

def firstFuc():
    print "I am in first function"
def secondFuc(first):
    print "I am in second function"
    first()
    firstFuc()

secondFuc(firstFuc)
print "#################################"
print "4.A function can return some other function which is defined in it"

def outer():
    print "First statement of outer function"
    def inner():
        print "I am in inner function now"
    return inner
innerfunc=outer()
innerfunc()
#From here you can't make a call to inner because inner is not available at this point
