#!/usr/bin/python

def multipliers():
    return [lambda x: i * x for i in range(4)]

print multipliers()
print [m(2) for m in multipliers()]
print [m(3) for m in multipliers()]
print [m(1) for m in multipliers()]


def multipliers1():
    return [lambda x, i=i : i * x for i in range(4)]

print [m(1) for m in multipliers1()]

#
# def extendList(val, list=[]):
#     list.append(val)
#     return list
#
#
# list1 = extendList(10)
# list2 = extendList(123, [])
# list3 = extendList('a')
#
# print "list1 = %s" % list1
# print "list2 = %s" % list2
# print "list3 = %s" % list3

def extendList01(val, list=None):
    if list is None:
        list = []
    list.append(val)
    return list

list01 = extendList01(10)
list02 = extendList01(123, [])
list03 = extendList01('a')

print "list01 = %s" % list01
print "list02 = %s" % list02
print "list03 = %s" % list03


