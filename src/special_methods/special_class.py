class Special:
    def __new__(cls):
        print('Special.__new__')
        return super().__new__(cls)

    def __init__(self) -> None:
        print('Special.__init__')
        self.__dict__['_data'] = dict()

    def __del__(self):
        print('Special.__del__')

    def __setattr__(self, key, value):
        print('Special.__setattr__: key=', key, ', value=', value)
        self._data[key] = value

    def __getattr__(self, key):
        print('Special.__getattr__: key=', key)
        if key in self._data:
            return self._data[key]
        raise AttributeError(f'key \'{key}\' not exist in Special instance')

    def __setitem__(self, key, value):
        print('Special.__setitem__: key=', key, ', value=', value)
        self._data[key] = value

    def __getitem__(self, key):
        print('Special.__getitem__: key=', key)
        if key in self._data:
            return self._data[key]
        raise AttributeError(f'key \'{key}\' not exist in Special instance')

    def __repr__(self) -> str:
        str = 'Special {'
        for key in self._data:
            str += f'\n  {key}: {self._data[key]},'
        str += '\n}' if len(self._data) > 0 else '}'
        return str
