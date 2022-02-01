from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/')
def index():
    return '<H1>Hola Mundo</H1>'
app.run()
