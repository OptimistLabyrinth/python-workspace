def _append(list01: list, list02: list):
    appended = list01.append(list02)
    print('list01:', list01)
    print('list02:', list02)
    print('appended:', appended)
    print()

def _extend(list01: list, list02: list):
    extended = list01.extend(list02)
    print('list01:', list01)
    print('list02:', list02)
    print('extended:', extended)
    print()

class _Person:
    id_seq = 1
    def __init__(self, name: str, age: int):
        _Person.id_seq += 1
        self.id = _Person.id_seq
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'Person({self.name}, {self.age})'

def _print_list(list_to_print: list):
    for each in list_to_print:
        print(each, end=', ')
    print()

def _sort():
    test_list = [
        _Person(name='Jack', age=16),
        _Person(name='Harrison', age=35),
        _Person(name='Fredrick', age=22),
    ]
    sorted_by_id = sorted(test_list, key=lambda x: x.id)
    print('sorted by id   : ', end='')
    _print_list(sorted_by_id)
    print('sorted by name : ', end='')
    sorted_by_name_in_ascending = sorted(test_list, key=lambda x: x.name, reverse=False)
    _print_list(sorted_by_name_in_ascending)
    print('sorted by age  : ', end='')
    sorted_by_age_in_descending = sorted(test_list, key=lambda x: x.age, reverse=True)
    _print_list(sorted_by_age_in_descending)
    print()

def playing_with_list():
    list01 = [1, 1, 2, 3, 1, 1, 0, 0]
    list02 = ['a', 'b', 'def']

    _append(list01.copy(), list02.copy())
    _extend(list01[:], list02[:])

    print('list01:', list01)
    print('list02:', list02)
    print()

    _sort()

def _list_comprehensions_01():
    squares = []
    for x in range(10):
        squares.append(x**2)
    print(squares)
    squares = list(map(lambda x: x**2, range(10)))
    print(squares)
    squares = [x**2 for x in range(10)]
    print(squares)
    print()

def _list_comprehensions_02():
    combs = []
    for x in [1,2,3]:
        for y in [3,1,4]:
            if x != y:
                combs.append((x, y))
    print(combs)
    combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
    print(combs)
    print()

def _list_comprehensions_03():
    vec = [-4, -2, 0, 2, 4]
    result01 = [x*2 for x in vec]
    print(result01)
    result02 = [x for x in vec if x >= 0]
    print(result02)
    result03 = [abs(x) for x in vec]
    print(result03)
    fresh_fruit = ['  banana', '  loganberry ', 'passion fruit  ']
    result04 = [fruit.strip() for fruit in fresh_fruit]
    print(result04)
    result05 = [(x, x**2) for x in range(6)]
    print(result05)
    vec = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    result07 = [elem for elem in vec]
    result08 = [num for elem in vec for num in elem]
    print(result07)
    print(result08)
    from math import pi
    result09 = [str(round(pi, i)) for i in range(1, 6)]
    print(result09)
    print()

def list_comprehensions():
    _list_comprehensions_01()
    _list_comprehensions_02()
    _list_comprehensions_03()

def _nested_list_comprehensions_01():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    result01 = [row[i] for row in matrix for i in range(len(row))]
    print(result01)

    transposed = []
    for i in range(len(matrix[0])):
        transposed.append([row[i] for row in matrix])
    print(transposed)
    transposed02 = list(zip(*matrix))
    print(transposed02)
    transposed03 = [list(each) for each in zip(*matrix)]
    print(transposed03)
    print()

def nested_list_comprehensions():
    _nested_list_comprehensions_01()

def playing_with_dictionary():
    dict01 = {}
    dict01['key003'] = 'value003'
    dict01['key002'] = 'value002'
    dict01['key001'] = 'value001'
    dict01['key003'] = 'value333'
    print(dict01)
    list_from_dict01 = list(dict01)
    print(list_from_dict01)
    dict02 = dict([
        ('sape', 4139),
        ('guido', 8227),
        ('jack', 1098)
    ])
    print(dict02)
    dict03 = {x: x**2 for x in (2, 4, 6)}
    print(dict03)
    dict04 = dict(sape=4139, guido=8227, jack=1098)
    print(dict04)
    for k, v in dict04.items():
        print('    ', k, v)
    print()
