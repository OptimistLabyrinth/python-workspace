from collections import UserDict
from typing import Any

class Box(UserDict):
    def __init__(self, data):
        super().__init__(data)

    def __getattr__(self, key: str):
        if key in self.data:
            return self.data[key]
        else:
            raise AttributeError(f'\'Box\' object has no attribute \'{key}\'')

    def __setattr__(self, key: str, value) -> None:
        if key == 'data':
            super().__setattr__(key, value)
        else:
            self.data[key] = value

    def __delattr__(self, key: str) -> None:
        if key in self.data:
            del self.data[key]
        else:
            raise AttributeError(f'\'Box\' object has no attribute \'{key}\'')

def test_box():
    character = Box({
        'id': 1,
        'name': 'Spock',
        'species': 'Vulcan',
        'rank': 'Commander',
    })
    print(character.name)
    print(character.species)
    print(character.rank)

    character.rank = 'Captain'
    print(character.rank)

    del character.rank
    try:
        print(character.rank)
    except Exception as e:
        print(f'Error: {e}')

    print('OK')
