from flask import Flask
from flask_cors import CORS
from config import config
from routes import Proveedores
from routes import Categoria
from routes import Productos
from routes import Lote
from routes import Ventas
from routes import Reportes
from routes import vistas_routes
from routes import notificaciones

app = Flask(__name__)

CORS(app)

if __name__ == '__main__':
    app.register_blueprint(Proveedores.main, url_prefix = '/proveedores')
    app.register_blueprint(Categoria.main, url_prefix = '/categoria')
    app.register_blueprint(Productos.main, url_prefix = '/productos')
    app.register_blueprint(Lote.main, url_prefix = '/lote')
    app.register_blueprint(Ventas.main, url_prefix = '/ventas')
    app.register_blueprint(Reportes.main, url_prefix = '/reportes')
    app.register_blueprint(notificaciones.main, url_prefix = '/notificacion')
    app.register_blueprint(vistas_routes.Vistas, url_prefix = '/')
    app.config.from_object(config['development'])
    app.run(port = 80)