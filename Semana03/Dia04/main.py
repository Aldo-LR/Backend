from flask import FLask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/db_matricula'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class AlumnoSchema(ma.Schema):
    class Meta:
        fields = ('alumno_id','alumno_nombre','alumno_email')

@app.route('/')
def index():
    return jsonify({
        'message':'BIENVENIDO A MI API'
        })

@app.route('/alumnos')
def alumnos():
    schemaAlumnos = AlumnoSchema(many=True)
    tuplaAlumnos = db.engine.execute ('select * from tbl_alumnos')	
    listaAlumnos = list(tuplaAlumnos)
    dataAlumnos = schemaAlumnos.dump(listaAlumnos)
    return jsonify(dataAlumnos)

if __name__ == '__main__':
    app.run(debug=True,port=5000)