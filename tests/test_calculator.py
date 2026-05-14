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

def test_multiplication_operation():
    calc = Calculator()
    calc.operate("+", 5)
    calc.operate("*", 2)
    assert calc.result == 10


def test_division_operation():
    calc = Calculator()
    calc.operate("+", 10)
    calc.operate("/", 2)
    assert calc.result == 5


def test_division_by_zero():
    calc = Calculator()
    message = calc.operate("/", 0)
    assert message == "No se puede dividir entre cero"


def test_undo_operation():
    calc = Calculator()
    calc.operate("+", 5)
    calc.undo()
    assert calc.result == 0


def test_redo_operation():
    calc = Calculator()
    calc.operate("+", 5)
    calc.undo()
    calc.redo()
    assert calc.result == 5