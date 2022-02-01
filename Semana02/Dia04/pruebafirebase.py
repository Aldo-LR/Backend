import pyrebase

config ={
    "apiKey": "AIzaSyDEkiewFACwWy49QfDso2IAc_ithNgqZa8",
    "authDomain": "portafolio-c7688.firebaseapp.com",
    "databaseURL": "https://portafolio-c7688-default-rtdb.firebaseio.com",
    "projectId": "portafolio-c7688",
    "storageBucket": "portafolio-c7688.appspot.com",
    "messagingSenderId": "990764298231",
    "appId": "1:990764298231:web:ae0064b00f1390779a48f2",
    "measurementId": "G-D3FJ7QCHYJ"
}

firebase = pyrebase.initialize_app(config)

#*Ejemplo con auth

auth = firebase.auth()
try:
    usuario = auth.sign_in_with_email_and_password('aldoglazaror@gmail.com','codigo2022')
    print(auth.get_account_info(usuario['idToken']))
    auth.delete_user_account(usuario['idToken'])
except:
    print("usuario o password invalidos")

#print("Enviando email de verificacion")
#auth.send_email_verification(usuario['idToken'])

#*cambiando la contraseña del usuario
#auth.send_password_reset_email('aldoglazaror@gmail.com')
#print("Se envio un correo de reseteo para aldoglazaror@gmail.com")

#*Crear usuarios

email = input("Ingrese Email : ")
password = input ("Ingrese password : ")

auth.create_user_with_email_and_password(email,password)
print("Usuario creado con exito")


