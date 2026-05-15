import sys # importamos el modulo sys para trabajar con funciones y configuraciones del sistema

import os # importamos el modulo os para trabajar con rutas y directorios


sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# agregamos una nueva ruta al sistema de Python __file__ obtiene la ubicacion del archivo actual 
# os.path.dirname(__file__) obtiene la carpeta donde esta el archivo el segundo dirname sube un nivel mas arriba
# sys.path.append agrega esa ruta para poder importar archivos del proyecto
# en resumen basicamente esto es para que se pueda correr el pytest

from calculator import Calculator #importamos para usar las funciones de calculator 


def test_initial_result_is_zero():  # verifica que el resultado sea 0
    calc = Calculator()
    assert calc.result == 0


def test_sum_operation(): # verifica una suma y si el resultado da lo esperado
    calc = Calculator()
    calc.operate("+", 5)
    assert calc.result == 5


def test_subtraction_operation():# verifica una resta y si el resultado da lo esperado
    calc = Calculator()
    calc.operate("-", 3)
    assert calc.result == -3

def test_multiplication_operation():# verifica una multiplicacion y si el resultado da lo esperado
    calc = Calculator()
    calc.operate("+", 5)
    calc.operate("*", 2)
    assert calc.result == 10


def test_division_operation():# verifica una division y si el resultado da lo esperado
    calc = Calculator()
    calc.operate("+", 10)
    calc.operate("/", 2)
    assert calc.result == 5


def test_division_by_zero(): #division entre 0 
    calc = Calculator()
    message = calc.operate("/", 0)
    assert message == "No se puede dividir entre cero"


def test_undo_operation(): # verifica que el undo funcione
    calc = Calculator()
    calc.operate("+", 5)
    calc.undo()
    assert calc.result == 0


def test_redo_operation():  # verifica el redo
    calc = Calculator()
    calc.operate("+", 5)
    calc.undo()
    calc.redo()
    assert calc.result == 5

def test_clear_calculator(): #verifica el borrar los datos que se tiene
    calc = Calculator()
    calc.operate("+", 10)
    calc.clear()
    assert calc.result == 0


def test_redo_clears_after_new_operation(): # verifica que despues de una nueva operacion el redo sea nulo o que este vacio en este caso 
    calc = Calculator()
    calc.operate("+", 5)
    calc.undo()
    calc.operate("+", 3)
    assert calc.history.get_redo_stack() == []