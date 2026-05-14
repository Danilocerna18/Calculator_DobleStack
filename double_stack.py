class DoubleStack: #Clase de Double Stack
    def __init__(self): #Constructor de la clase 
        self.undo_stack = [] #Stack que almacena los estados anteriores 
        self.redo_stack = [] #Stack que almacena los estados deshechos
