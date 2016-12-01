# -*- coding:utf-8 -*-
import functools

def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print("*args={0}, **kwargs={1}".format(*args, **kwargs))
            print("{1} calling {0}".format(func.__name__, text))
            return func(*args,**kwargs)
        return wrapper
    return decorator

@logger("sys")
def get_args(*args, **kwargs):
    print("*args={0}, **kwargs={1}".format(*args,**kwargs))
    print('xue')


# if __name__ == '__main__':
get_args("chuan","cong")
print("func.name = {0}".format(get_args.__name__))