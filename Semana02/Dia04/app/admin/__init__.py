#IMPORTAMOS LA CLASE BLUEPRINT QUE NOS PERMITIRA REGISTRAR NUESTRO MODULO AL PROYECTO PRINCIPAL
from flask import Blueprint

admin = Blueprint('admin', __name__,url_prefix='/admin')
from . import views