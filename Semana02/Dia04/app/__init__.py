#*Importamos el framework Flask
from flask import Flask
from flask_bootstrap import Bootstrap
from .admin import admin
from .config import Config
def create_app():
    app = Flask(__name__)
    
    #* AGREGAMOS BOOSSTRAP A MI APP
    
    bootstrap = Bootstrap(app)
    app.config.from_object(Config)
    
    app.register_blueprint(admin)
    return app
    