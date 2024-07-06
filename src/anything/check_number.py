from enum import Enum

class NumberCategory(Enum):
    ZERO = "Zero"
    POSITIVE = "Positive"
    NEGATIVE = "Negative"

def check_number(num: str):
    num = float(num)
    if num >= 0:
        if num == 0:
            return NumberCategory.ZERO
        else:
            return NumberCategory.POSITIVE
    else:
        return NumberCategory.NEGATIVE
