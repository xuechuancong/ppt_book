#print 5**5
def story(**kwds):
    return 'Once upon a time, there was a %(job)s called %(name)s.' %kwds

print story(name = 'America', job = 'country')

def power(x, y, *others):
    if others:
        print 'received redundant parameters:', others
    return pow(x, y)
    
print power(2, 3)
params = (5,) * 2
print params
print power(*params)
print power(1, 0, *params)
print power(2, 2, 'Hello, World!')
