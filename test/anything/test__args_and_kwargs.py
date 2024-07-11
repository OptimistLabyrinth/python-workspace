import pytest
from src.anything.args_and_kwargs import func_with_args_only, func_with_kwargs_only

class TestArgsAndKwargs:
    class TestFuncWithArgsOnly:
        def test__check_pass_as_args(self):
            print()
            a = 1
            b = 'hello'
            c = {
                'k1': 10,
                'k2': 20,
            }
            func_with_args_only(a, b, c)

        def test__check_pass_as_kwargs(self):
            print()
            a = 1
            b = 'hello'
            c = {
                'k1': 10,
                'k2': 20,
            }
            func_with_args_only(a=a, b=b, c=c)

    class TestFuncWithKwargsOnly:
        def test__check_pass_as_args(self):
            print()
            a = 1
            b = 'hello'
            c = {
                'k1': 10,
                'k2': 20,
            }
            with pytest.raises(TypeError):
                func_with_kwargs_only(a, b, c)

        def test__check_pass_as_kwargs(self):
            print()
            a = 1
            b = 'hello'
            c = {
                'k1': 10,
                'k2': 20,
            }
            func_with_kwargs_only(a=a, b=b, c=c)
