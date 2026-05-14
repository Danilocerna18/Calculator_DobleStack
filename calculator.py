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