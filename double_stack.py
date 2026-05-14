class DoubleStack: #Clase de Double Stack
    def __init__(self): #Constructor de la clase 
        self.undo_stack = [] #Stack que almacena los estados anteriores 
        self.redo_stack = [] #Stack que almacena los estados deshechos
        
    def push_undo(self, value): #Método para agregar un valor al undo stack
        self.undo_stack.append(value) #agrega el valor al final de la lista 

    def push_redo(self,value): #Método para agregar un valor al redo stack
        self.redo_stack.append(value) #Agrega el valor al final de la lista

    
