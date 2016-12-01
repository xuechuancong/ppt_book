# -*- coding:utf-8 -*-

# print 'Hello, World!'

def swap():
    global a
    a = [6, 3]
    if(a[0] > a[1]):
        a[0], a[1] = a[1], a[0]
    else:
        return a


swap()
for i in a:
    print i
