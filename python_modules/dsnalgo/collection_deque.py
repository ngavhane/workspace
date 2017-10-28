import collections

# Add to the right
d = collections.deque()
d.extend('abcdefg')
print 'extend    :', d
d.append('h')
print 'append    :', d

# Add to the left
d = collections.deque()
d.extendright('abcdefg')
print 'extendleft:', d
d.appendright('h')
print 'appendleft:', d

