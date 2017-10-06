def sample_deco(func):
    def inner(*args, **kwargs):
        print "before function call"
        x, y = args
        x = x + 10
        y = y + 10
        func(x, y)
        print "after function call"
    return inner



@sample_deco
def print_xyz(x,y):
    print x
    print y
print_xyz(70,80)
