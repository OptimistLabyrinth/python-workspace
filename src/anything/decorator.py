import functools

class DecoratorClass:
    @staticmethod
    def decorate_static_method(func):
        @functools.wraps(func)
        def decorated(*args, **kwargs):
            print(f'prior to     {func}')
            func()
            print(f'posterior to {func}')
        return decorated

    @staticmethod
    def decorate_instance_method(func):
        @functools.wraps(func)
        def decorated(self, *args, **kwargs):
            print(f'followed by {func}')
            func(self)
            print(f'following   {func}')
        return decorated

def decorator_function(func):
    def wrapper():
        print(f'before func {func}')
        func()
        print(f'after  func {func}')
    return wrapper

@decorator_function
def say_whee():
    print('whee!')

@DecoratorClass.decorate_static_method
def say_gee():
    print('gee!')

class Say:
    @DecoratorClass.decorate_instance_method
    def hello(self):
        print('hello!')
