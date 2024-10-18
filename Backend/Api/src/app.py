from flask import Flask
from config import config
from routes import Empleado
from routes import vistas_routes

app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(Empleado.main, url_prefix = '/api/empleado')
    app.register_blueprint(vistas_routes.Vistas, url_prefix = '/')
    app.config.from_object(config['development'])
    app.run()