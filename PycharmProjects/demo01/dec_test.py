class Decorator(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Before the function call.')
        # self.func(*args, **kwargs)
        print('After the function call.')
        return self.func

@Decorator
def testfunc():
    print('Inside the function.')
    print('xue')

testfunc()