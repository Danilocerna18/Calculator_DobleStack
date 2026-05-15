from double_stack import DoubleStack # importamos todas las logicas que tenemos en double_stack


class Calculator: # creamos la clase calculator
    def __init__(self): # constructor
        self.result = 0 # inicia en 0 
        self.history = DoubleStack() # se crea un objeto doublestack para manejar el undo y redo

    def operate(self, operator, number): # en la operacion esperamos el operador (signo) y el numero a operar
        previous_result = self.result 

        if operator == "+": # if para hacer las operaciones
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

        self.history.push_undo(previous_result)  # guardamos el resultado anterior en el undo stack
        self.history.clear_redo() # limpiamos el redo stack porque se hizo una nueva operacion
        return "Operación realizada"

    def undo(self):
        previous = self.history.pop_undo() # sacamos el ultimo valor guardado del undo stack

        if previous is None:
            return "No hay operaciones previas" # si esta vacio retornamos esto

        self.history.push_redo(self.result) # guardamos el resultado actual en el redo stack  
        self.result = previous # regresamos al resultado anterior
        return "Undo realizado"


    def redo(self): 
        next_value = self.history.pop_redo() #sacamos el ultimo valor de redo

        if next_value is None: #usamos la logica de undo en el redo
            return "No hay operaciones que rehacer" 

        self.history.push_undo(self.result)
        self.result = next_value
        return "Redo realizado"

    def clear(self): # esto es para borrar todos los datos y regresar a 0 inicial
        self.result = 0
        self.history.clear_all()
        return "Calculadora reiniciada"

    def get_data(self): # esto es solo para obtener la info de lo que se tiene 
        return {
            "result": self.result,
            "undo_stack": self.history.get_undo_stack(),
            "redo_stack": self.history.get_redo_stack()
        }