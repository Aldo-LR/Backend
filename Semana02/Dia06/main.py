#importamos dependencias para Flask y SqlAlchemy
from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)

#configuramos el acceso a la base de datos mysql en clever cloud con sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ulhvmsdwadk05fqk:kkWRfd6vpizBqvnQyKTB@bfq5jwrxeqw6bqzifjy6-mysql.services.clever-cloud.com:3306/bfq5jwrxeqw6bqzifjy6'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

#CREAMOS TABLAS EN LA BASE DE DATOS
class Alumno(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),unique=True)
    
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        
db.create_all()
print("SE CREARON LAS TABLAS EN LA BASE DE DATOS")

#CREAMOS SCHEMAS
class AlumnosSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','email')
        
alumno_schema = AlumnosSchema()

@app.route('/')
def index():
    return jsonify(
                    {
                    'status':'OK',
                    'mensaje':'Bienvenido a mi APIREST con Flask'
                    }
                   )
    
@app.route('/alumno',methods=['POST'])
def alumno():
    #capturamos los valores
    nombre = request.json['nombre']
    email = request.json['email']
    #insertarmos el registro en la base de datos
    nuevoAlumno = Alumno(nombre,email)
    db.session.add(nuevoAlumno)
    db.session.commit()
    return alumno_schema.jsonify(nuevoAlumno)

alumnos_schema = AlumnosSchema(many=True)
@app.route('/alumnos')
def alumnos():
    lstAlumnos = Alumno.query.all()
    dataAlumnos = alumnos_schema.dump(lstAlumnos)
    return jsonify(dataAlumnos)
    
#*METODO PUT PARA ACTUALIZAR ALUMNOS
@app.route('/updalumno/<id>',methods=['PUT'])
def updateAlumno(id):
    alumno = Alumno.query.get(id)
    print('Alumno')
    nombre = request.json['nombre']
    email = request.json['email']
    #Actualizamos los valores
    alumno.nombre = nombre
    alumno.email = email
    
    db.session.commit()
    
    return alumno_schema.jsonify(alumno)

@app.route('/delAlumno/<id>',methods=['DELETE'])
def deleteAlumno(id):
    alumno = Alumno.query.get(id)
    db.session.delete(alumno)
    db.session.commit()
    return alumno_schema.jsonify(alumno)
    
@app.route('/alumno/<id>')
def getAlumno(id):
    alumno = Alumno.query.get(id)
    return alumno_schema.jsonify(alumno)

if __name__ == "__main__":
    app.run(debug=True,port=5000)