from flask import Flask
from flask_cors import CORS
from config import config
from routes import Empleado
from routes import Proveedores
from routes import vistas_routes

app = Flask(__name__)

CORS(app,resources = {"*": {"origins":"http://localhost:5000"}})

if __name__ == '__main__':
    app.register_blueprint(Empleado.main, url_prefix = '/empleado')
    app.register_blueprint(Proveedores.main, url_prefix = '/proveedores')
    app.register_blueprint(vistas_routes.Vistas, url_prefix = '/')
    app.config.from_object(config['development'])
    app.run()