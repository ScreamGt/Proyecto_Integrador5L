from flask import Blueprint , jsonify, request
from models.VentasModel import VentasModel
from routes import ValidarToken

main = Blueprint('ventas_blueprint', __name__)

# Ruta para traer todos las ventas
@main.route('/getAll')
def get_ventas():
    token = request.args.get('token')
    if ValidarToken.validar_token(token):
        try:
            ventas = VentasModel.get_ventas()
            return jsonify(ventas)
        except Exception as ex:
            return jsonify({'message' : str(ex)}) , 500
    else:
        return jsonify({'message': "token no valido"}), 500




#Ruta para agregar una venta a la BD 
@main.route('/add', methods=['POST'])
def add_venta():
    token = request.form.get('token')
    if ValidarToken.validar_token(token) == "administrador":
        try:
            # Recibir datos desde el formulario HTTP
            peso = request.form.get('peso')
            nombreProducto = request.form.get('nombreProducto')
            

            success = VentasModel.add_venta(peso, nombreProducto)

            # Mensaje para mirar si fue exitoso los cambios en la BD
            if success :  
                return jsonify({'status': 'succesfull'})
            else:
                return jsonify({'status': "Ninguna venta Agregada"}), 404
        except Exception as ex:
            return jsonify({'status': str(ex)}), 500
    else:
        return jsonify({'status': "token no valido"})


