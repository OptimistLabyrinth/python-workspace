def func_with_args_only(a, b, c):
    print(a)
    print(b)
    print(c)


def func_with_kwargs_only(*, a, b, c):
    print(a)
    print(b)
    print(c)


def func_that_pass_kwargs(*args, **kwargs):
    print('passes:', args)
    print('passes:', kwargs)
    func_that_accept_kwargs(**kwargs['kwargs'])


def func_that_accept_kwargs(name, location, key2, key1):
    print('accept:', kwargs)


if __name__ == '__main__':
    kwargs = {
        'key1': 'aaa',
        'key2': 'bbb',
        'name': 'anonymous',
        'location': 'Gyeonggi-do',
        'rest': '...',
        'more': '??',
    }
    func_that_pass_kwargs(kwargs=kwargs)

