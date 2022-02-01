from pymongo import MongoClient
cliente = MongoClient('mongo://localhost:27017')

db = cliente['codigog11']

colAlumnos = db['alumnos']

alumnoId = colAlumnos.insert_one({'nombre':'Juan','email':'juan@gmail.com','nota':7})

print("Nuevo alumnos creado ID : ", alumnoId)