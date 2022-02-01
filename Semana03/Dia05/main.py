import re
from flask import Flask,jsonify,request,Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_URI']= 'mongodb://localhost:27017/codigog11'

mongo = PyMongo(app)
@app.route('/')
def index():
    return jsonify({'mensaje':'Bienvenido a mi API'})

@app.route('/alumno',methods=['POST'])
def crearAlumno():
    nombre = request.json['nombre']
    email = request.json['email']
    nota = request.json['nota']
    id = mongo.db.alumnos.insert_one(
        {
            'nombre':nombre,
            'email':email,
            'nota':nota
        })
    response =jsonify({
        '_id':str(id),
        'nombre':nombre,
        'email':email,
        'nota':nota
    })
    response.status_cod=201
    return response
@app.route('/alumnos')
def consultarAlumnos():
    alumnos = mongo.db.alumnos.find()
    response = json_util.dumps(alumnos)
    return Response(response,mimetype='application/json')
#*PARA TRAER UN SOLO ALUMNO
@app.route('/alumno/<id>',methods)
def ctraerAlumno(id):
    alumno = mongo.db.alumnos.find_one({'_id':ObjectId(id)})
    response = json_util.dumps(alumno)
    return Response(response,mimetype='application/json')
@app.route('/alumno/<id>',methods=['PUT'])
def actualizarAlumno(_id):
    nombre = request.json['nombre']
    email = request.json['email']
    nota = request.json['nota']
    
    mongo.db.alumnos.update_one(
        {
            '_id':ObjectId(_id)},{'$set:'}
        {
            'nombre':nombre,
            'email':email,
            'nota':nota
        }
    )
    return jsonify({'mensaje':'Alumno actualizado'})
    
    

if __name__ == '__main__':
    app.run(debug=True,port = 5000)

