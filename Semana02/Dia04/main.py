from flask import render_template

#* importar la funcion create_app de mi aplicacion app

from app import create_app

app = create_app()

#* creamos la rutas

@app.route('/')
def index():
    return render_template('index.html')
