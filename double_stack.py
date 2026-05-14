class DoubleStack: #Clase de Double Stack
    def __init__(self): #Constructor de la clase 
        self.undo_stack = [] #Stack que almacena los estados anteriores 
        self.redo_stack = [] #Stack que almacena los estados deshechos

    def push_undo(self, value): #Método para agregar un valor al undo stack
        self.undo_stack.append(value) #agrega el valor al final de la lista 

    def push_redo(self,value): #Método para agregar un valor al redo stack
        self.redo_stack.append(value) #Agrega el valor al final de la lista
    
    def pop_undo (self): #Método para sacar el último valor del undo stack
        if self.is_undo_empty():#Verifica si el stack está vacío 
            return None #Devuelve None si no hay elementos
        return self.undo_stack.pop() #Elimina y retorna el último

    def pop_redo(self): #Método para sacar el último valor 
        if self.is_redo_empty(): #Verifica si el redo stack está vacío 
            return None #Retorna None si no hay elementos
        return self.redo_stack.pop()#Elimina y retorna el último elemento