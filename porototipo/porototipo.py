# importar flask y otra mugre para llamar otros archivos
from flask import Flask, render_template, request

# hacer una página, template_folder es para que encuentre donde estan los html y cosas
app = Flask(__name__,template_folder='plantillas',static_folder='estatua') 

# le asignamo una ruta a la página
@app.route("/")   # "/" para que quede como la default, en este caso http://127.0.0.1:5000/  <-(tiene el "/")
# esta ruta va a ser la página principal
def home():
    # usando el render_template se se importó antes para llamar el .html
    return render_template("main.html")

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

@app.route("/pelao")
def pelao():
    return render_template("mapa-pelao.html")

# acá para que la página abra
if __name__ == "__main__":
    # debug=True para que se pueda ver la página mientras editamos cosas
    app.run(debug=True)