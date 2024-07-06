from src.special_methods.special_class import Special

class TestSpecial:
    class TestCreate:
        def test_create_instance(self):
            print()
            sp = Special()
            print(sp)
            assert sp != None

    class TestSetAttr:
        def test_set_attr(self):
            print()
            sp = Special()
            sp.abc = 1234
            print(sp)
            assert len(sp.__dict__['_data']) == 1
            assert 'abc' in sp.__dict__['_data']

        def test_set_attr_key_data(self):
            print()
            sp = Special()
            sp.data = [1, 2, 3]
            print(sp)
            assert len(sp.__dict__['_data']) == 1
            assert 'data' in sp.__dict__['_data']

    class TestGetAttr:
        def test_get_attr(self):
            print()
            sp = Special()
            sp.abc = 1234
            print(sp)
            value = sp.abc
            assert value == 1234

        def test_get_attr_key_data(self):
            print()
            sp = Special()
            sp.data = [1, 2, 3]
            print(sp)
            value = sp.data
            assert value == [1, 2, 3]

    class TestSetItem:
        def test_set_item(self):
            print()
            sp = Special()
            sp['abc'] = 1234
            print(sp)
            assert len(sp.__dict__['_data']) == 1
            assert 'abc' in sp.__dict__['_data']

        def test_set_item_key_data(self):
            print()
            sp = Special()
            sp['data'] = [1, 2, 3]
            print(sp)
            assert len(sp.__dict__['_data']) == 1
            assert 'data' in sp.__dict__['_data']

    class TestGetItem:
        def test_get_item(self):
            print()
            sp = Special()
            sp['abc'] = 1234
            print(sp)
            value = sp['abc']
            assert value == 1234

        def test_get_item_key_data(self):
            print()
            sp = Special()
            sp['data'] = [1, 2, 3]
            print(sp)
            value = sp['data']
            assert value == [1, 2, 3]
