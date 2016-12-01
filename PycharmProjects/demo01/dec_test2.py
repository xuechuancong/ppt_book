from types import MethodType




class Decorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Inside the decorator.')
        return self.func(*args, **kwargs)

    def __get__(self, instance, cls):
        return self if instance is None else MethodType(self, instance)



@Decorator
def testfunc():
    print('Inside the function.')
    print('xue')



testfunc()
print(type(testfunc))
