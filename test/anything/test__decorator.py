from src.anything.decorator import say_whee, say_gee, Say

class TestDecorator:
    def test__say_whee(self):
        print()
        say_whee()

    def test__say_gee(self):
        print()
        say_gee()

    class TestSay:
        def test__hello(self):
            print()
            Say().hello()
