import os
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import logging



api = Api()
db = SQLAlchemy()
logging.basicConfig(level=logging.INFO, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')



def create_app():
    app = Flask(__name__)
    load_dotenv()
    
    
    if not os.path.exists(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')):
        os.mknod(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME'))

    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')
    db.init_app(app)

    import main.controllers as resources

    api.add_resource(resources.ClientesResource, '/clientes')
    api.add_resource(resources.ClienteResource, '/cliente/<id>')
    api.add_resource(resources.EmpresasResource, '/empresas')
    api.add_resource(resources.EmpresaResource, '/empresa/<id>')
    api.add_resource(resources.EquiposResource, '/equipos')
    api.add_resource(resources.EquipoResource, '/equipo/<id>')
    api.add_resource(resources.ApuestasResource, '/apuestas')
    api.init_app(app)

    return app
