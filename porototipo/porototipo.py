# importar flask y otra mugre para llamar otros archivos
from flask import Flask, render_template, request
import sqlite3
import os
import json

currentdirectory = os.path.dirname(os.path.abspath(__file__))
connection = sqlite3.connect(currentdirectory + "\proyecto_full.db", check_same_thread=False)

# hacer una página, template_folder es para que encuentre donde estan los html y cosas
app = Flask(__name__,template_folder='plantillas',static_folder='estatua') 

# le asignamo una ruta a la página
@app.route("/")   # "/" para que quede como la default, en este caso http://127.0.0.1:5000/  <-(tiene el "/")
# esta ruta va a ser la página principal
def home():
    # usando el render_template se se importó antes para llamar el .html
    query1 = "SELECT latitud, longitud from paradero"
    cursor = connection.cursor()
    resultado = cursor.execute(query1)
    resultado = resultado.fetchall()

    query2 = "SELECT latitud, longitud from Ruta WHERE num = '1a'"
    resultado2 = cursor.execute(query2)
    resultado2 = resultado2.fetchall()
    for i in range(len(resultado2)):
        resultado2[i] = list(resultado2[i])
    return render_template("main.html", stops = resultado, ruta1a = resultado2)

# que es rutu
@app.route("/que-es-rutu")
def pag():
    return render_template("que-es-rutu.html")

# about
@app.route("/sobre-nosotros")
def about():
    return render_template("sobre-nosotros.html")

@app.route("/terminos-y-servicios")
def TyC():
    return render_template("terminos-y-servicios.html")

'''   ya le puse el mapa a la página principal asi que esto no es necesario   '''
@app.route("/map")
def map():
    return render_template("casa.html")

#MAPA CON RUTA
@app.route("/ruta1a")
def ruta1a():
    query1 = "SELECT latitud, longitud from paradero"
    cursor = connection.cursor()
    resultado = cursor.execute(query1)
    resultado = resultado.fetchall()

    query2 = "SELECT latitud, longitud from Ruta WHERE num = '1a'"
    resultado2 = cursor.execute(query2)
    resultado2 = resultado2.fetchall()
    for i in range(len(resultado2)):
        resultado2[i] = list(resultado2[i])
    return render_template("mapa_ruta1a.html", stops = resultado, ruta1a = resultado2)

# acá para que la página abra
if __name__ == "__main__":
    # debug=True para que se pueda ver la página mientras editamos cosas
    app.run(debug=True)