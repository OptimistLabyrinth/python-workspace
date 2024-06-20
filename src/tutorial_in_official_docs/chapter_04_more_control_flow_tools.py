def else_with_loop():
    for n in range(2, 20):
        print(f'({n})')
        for x in range(2, n):
            print(f'  ({n}, {x})')
            if n % x == 0:
                print('    ', n, 'equals', x, '*', n//x)
                break
        else:
            # loop fell through without finding a factor
            print('  ', n, 'is a prime number')

def _where_is_tuple(point: tuple[int, int]):
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")

class _Point:
    # __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

def _where_is_class(point: _Point):
    match point:
        case _Point(x=0, y=0):
            point.x = 999
            point.y = 999
            print("Origin")
        case _Point(x=0, y=y):
            print(f"Y={y}")
        case _Point(x=x, y=0):
            print(f"X={x}")
        case _Point():
            print("Somewhere else")
        case _:
            print("Not a point")

def match_expression():
    point_tuples = [(0, 0), (3, 0), (0,7), (5, 11), 'x']
    print()
    try:
        for point_tuple in point_tuples:
            _where_is_tuple(point_tuple)
    except Exception as e:
        print(e.args)
    print('pointTuples:', point_tuples)
    print()
    point_classes: list = [_Point(0, 0), _Point(3, 0), _Point(0, 7), _Point(5, 11), 'x']
    for point_class in point_classes:
        _where_is_class(point_class)
    print('points: ', end='')
    for point_class in point_classes:
        if hasattr(point_class, 'x') and hasattr(point_class, 'y'):
            print(f'Point(x:{point_class.x},y:{point_class.y})', end=' ')
        else:
            print(point_class, end=' ')
    print('\n')

def _concat(*args, sep="/"):
    return sep.join(args)

def test_concat(*args):
    result1 = _concat("earth", "mars", "venus")
    result2 = _concat("earth", "mars", "venus", sep=".")
    print(result1)
    print(result2)
    print()

def test_unpack():
    list01 = [2, 5]
    a, b = list01
    print(range(a, b))
    print(range(*list01))
    print()

def _parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")
    print()

def test_parrot():
    d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
    _parrot(**d)

def _documentation_string():
    '''summary of the documentation of the function

first line of contents of doc
second line of contents of doc
third line of contents of doc
'''

def test_documentation_string():
    print(_documentation_string.__doc__)
