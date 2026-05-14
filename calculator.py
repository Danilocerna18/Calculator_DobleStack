from double_stack import DoubleStack


class Calculator:
    def __init__(self):
        self.result = 0
        self.history = DoubleStack()

    def operate(self, operator, number):
        previous_result = self.result

        if operator == "+":
            self.result += number
        elif operator == "-":
            self.result -= number
        elif operator == "*":
            self.result *= number
        elif operator == "/":
            if number == 0:
                return "No se puede dividir entre cero"
            self.result /= number
        else:
            return "Operador inválido"

        self.history.push_undo(previous_result)
        self.history.clear_redo()
        return "Operación realizada"

    def undo(self):
        previous = self.history.pop_undo()

        if previous is None:
            return "No hay operaciones previas"

        self.history.push_redo(self.result)
        self.result = previous
        return "Undo realizado"


    def redo(self):
        next_value = self.history.pop_redo()

        if next_value is None:
            return "No hay operaciones que rehacer"

        self.history.push_undo(self.result)
        self.result = next_value
        return "Redo realizado"

    def clear(self):
        self.result = 0
        self.history.clear_all()
        return "Calculadora reiniciada"

    def get_data(self):
        return {
            "result": self.result,
            "undo_stack": self.history.get_undo_stack(),
            "redo_stack": self.history.get_redo_stack()
        }