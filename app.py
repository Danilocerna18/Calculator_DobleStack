from flask import Flask, render_template, request, redirect #Importa Flash, render_template (sirve para mostrar achivos HTML al usuario), request (Obtiene información enviada por el usuario desde peticiones HTTP) y redirect (srive para redirigir al usuario a otra ruta)
from calculator import Calculator #Importa la clase Calculator 

app = Flask (__name__) #Crea la aplicación Flask

calculator = Calculator() #Crea una instancia de la calculadora 

@app.route("/") #Ruta principal de la página
def index():
    data = calculator.get_data() #Obtiene los datos acturales de la calculadora
    return render_template("index.html", data = data) #Renderiza el HTML y envía los datos 

