# -*- coding:utf-8 -*-

def nums():
    print 'yield 1'
    yield 1
    print 'yield 2'
    yield 2
    print 'Finished'


g1 = nums()
# print g1
# arry0 = list(g1)
for i in g1:
     print 'Receive %s' %i

arry1 = list(g1)

g2 = nums()
arry2 = list(g2)