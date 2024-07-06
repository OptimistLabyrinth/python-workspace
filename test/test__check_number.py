from src.anything.check_number import check_number
from src.anything.check_number import NumberCategory

class TestCheckNumber:
    def test__check_number__negative(self):
        assert check_number('-22') == NumberCategory.NEGATIVE

    def test__check_number__zero(self):
        assert check_number('0') == NumberCategory.ZERO

    def test__check_number__positive(self):
        assert check_number('10') == NumberCategory.POSITIVE
