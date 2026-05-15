# Proyecto final-Calculadora implementada con Double Stack 

Este proyecto consiste en crear una calculadora básica desarrollada en Python utilizando Flask y una implementación de Double Stack, la cuál es la estructura de datos requerida para el proyecto. La idea principal es lograr una simulación del funcionamiento de una calculadora utilizando acciones de Undo y Redo,  empleamos referencias como Word, los navegadores web y otros ejemplos vistos en clase para entender completamente el uso implementado de Double Stack. Cada vez que el usuario realiza una operación, el estado anterior se guarda en un stack de Undo. Cuando el usuario deshace una acción, el estado actual pasa al stack de Redo. Para la interfaz gráfica utilizamos únicamante HTML para su desarrollo. 

## ¿Cómo ejecutar el proyecto?

### windows una sola linea:
```bash
git clone https://github.com/Danilocerna18/Calculator_DobleStack.git; cd Calculator_DobleStack; pip install -r requirements.txt; python app.py
```

### mac en una sola linea 
```bash
git clone https://github.com/Danilocerna18/Calculator_DobleStack.git && cd Calculator_DobleStack && pip3 install -r requirements.txt && python3 app.py
```

### paso por paso:
### clonar el repositorio:
```bash
git clone https://github.com/Danilocerna18/Calculator_DobleStack.git
```

### Windows: 

```bash
pip install -r requirements.txt; python app.py

```

#### si no dejo con el anterior intentar con este: 

```bash
pip install -r requirements.txt && python app.py
```

### MacOS:
```bash
pip3 install -r requirements.txt && python3 app.py
```

## ¿Cómo ejecutar el pytest?

### Windows: 

```bash
cd Calculator_DobleStack; pytest

```

#### si no dejo con el anterior intentar con este: 

```bash
cd Calculator_DobleStack && pytest
```

### MacOS:
```bash
cd Calculator_DobleStack && pytest  
```
#### si no dejo con el anterior intentar con este: 
```bash
cd Calculator_DobleStack && python3 -m pytest
```

## Funciones principales de la calculadora:

-Suma
-Resta
-Multiplicación
-División
-Undo
-Redo
-Reiniciar calculadora 
-Visualización de Undo Stack y de Redo Stack

## Implementación de Double Stack: 

La estructura de datos fue implementada desde cero utilizando listas de Python.

El proyecto utiliza dos stacks:

-undo_stack: GUarda los estados anteriores de la calculadora antes de realizar una nueva operación. 

-redo_stack: Guarda los estados que fueron deshechos mediante Undo para poder recuperarlos con Redo. 

## Complejidad temporal: 

-push-Undo() O(1)
-push_redo() O(1)
-pop_undo()  O(1)
-pop_redo()  O(1)
-clear_all()  O(n)
-is_undo_empty() O(1)
-is_redo_empty() O(1)

## Tecnologías utilizadas:
 Python, Flash, HTML, CSS y Pytest







