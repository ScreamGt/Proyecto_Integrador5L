from flask import Blueprint , jsonify, request, render_template
from models.LoteModel import LoteModel
from models.ProveedoresModel import ProveedoresModel
from routes import ValidarToken

main = Blueprint('lote_blueprint', __name__)

# Ruta para traer todos los lotes
@main.route('/getAll')
def get_lotes():
    token = request.args.get('token')
    if ValidarToken.validar_token(token):
        try:
            lotes = LoteModel.get_lotes()
            return jsonify(lotes)
        except Exception as ex:
            return jsonify({'message' : str(ex)}) , 500
    else:
        return jsonify({'message': "token no valido"}), 500

#Ruta para traer un lote por el nombre del producto
@main.route('/getOne_name', methods=['GET'])
def get_lote_nombre():
    token = request.args.get('token')
    if ValidarToken.validar_token(token):
        try:
            nombre_producto = request.args.get('nombre_producto')
            lotes = LoteModel.get_lote_nombre(nombre_producto)

            if lotes != None:
                return jsonify(lotes)
            else:
                return jsonify(None)
        except Exception as ex:
            return jsonify({'message' : str(ex)}) , 500
        
#Ruta para traer un lote por su estado
@main.route('/getOne_estado', methods=['GET'])
def get_lote_estado():
    token = request.args.get('token')
    if ValidarToken.validar_token(token):
        try:
            estado_lote = request.args.get('estado_lote')
            lotes = LoteModel.get_lote_estado(estado_lote)

            if lotes != None:
                return jsonify(lotes)
            else:
                return jsonify(None)
        except Exception as ex:
            return jsonify({'message' : str(ex)}) , 500


@main.route('/add', methods=['POST'])
def add_lote():
    token = request.form.get('token')
    if ValidarToken.validar_token(token) == "administrador":
        try:
            # Recibir datos desde el formulario HTTP
            
            fecha_llegada = request.form.get('fechaLlegada')
            peso = str(request.form.get('peso'))
            precio = str(request.form.get('precio'))
            nombre_proveedor = request.form.get('nombre_proveedor')
            nombre_producto = request.form.get('nombre_producto')
            

            success = LoteModel.add_lote(fecha_llegada, peso, precio, nombre_proveedor, nombre_producto)

            # Mensaje para mirar si fue exitoso los cambios en la BD
            if success:  
                return jsonify({'status': 'succesfull'})
            else:
                return jsonify({'status': "Ningun Lote Agregado"}), 404
        except Exception as ex:
            return jsonify({'status': str(ex)}), 500
    else:
        return jsonify({'status': "token no valido"})


#Ruta para actualizar un Proveedor
@main.route('/update', methods=['PUT'])
def update_proveedor():
    token = request.args.get('token')
    if ValidarToken.validar_token(token) == "administrador":
        try:
            # Recibir datos desde el formulario HTTP POST
            id_lote = request.args.get('id_lote')
            fecha_llegada = request.args.get('fecha_llegada')
            peso = request.args.get('peso')
            precio = request.args.get('precio')
            success = LoteModel.update_lote(id_lote, fecha_llegada, peso,precio)

            # Mensaje para mirar si fue exitoso los cambios en la BD
            if success :  
                return jsonify({'message': 'Lote actualizado exitosamente'}),200
            else:
                return jsonify({'message': "Ningun Lote actualizado"}), 500
        
        except Exception as ex:
            return jsonify({'message': str(ex)}), 500
    else:
        return jsonify({'message': "token no valido"}), 500

#Ruta para eliminar un lote de la BD
@main.route('/delete', methods=['PUT'])
def delete_lote():
    token = request.args.get('token')
    if ValidarToken.validar_token(token) == "administrador":
        try:
            # Recibir datos desde el formulario HTTP POST
            id_lote = request.args.get('id_lote')
            success = LoteModel.delete_lote(id_lote)

            # Mensaje para mirar si fue exitoso los cambios en la BD
            if success:  
                return jsonify({'message': 'Lote Eliminado'})
            else:
                return jsonify({'message': "Ningun Lote eliminado"}), 404
        
        except Exception as ex:
            return jsonify({'message': str(ex)}), 500
    else:
        return jsonify({'message': "token no valido"}), 500