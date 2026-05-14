from calculator import Calculator


def test_initial_result_is_zero():
    calc = Calculator()
    assert calc.result == 0


def test_sum_operation():
    calc = Calculator()
    calc.operate("+", 5)
    assert calc.result == 5


def test_subtraction_operation():
    calc = Calculator()
    calc.operate("-", 3)
    assert calc.result == -3