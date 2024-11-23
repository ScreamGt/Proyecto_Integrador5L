from flask import  render_template, Blueprint, jsonify
from models import ReportesModel  # Asegúrate de importar correctamente tu modelo

main = Blueprint('reportes_blueprint', __name__)

@main.route('/productos_mas_lotes')
def productos_mas_lotes():
    print("entro a la ruta")
    # Llamar al método que obtiene el producto con más lotes
    productos = ReportesModel.get_prod_mas_lotes()
    
    # Imprimir productos para verificar su contenido
    print(productos)  # Verifica en la consola de Flask
    
    # Pasar los datos a la plantilla
    return render_template('view_reportes.html', productos=productos)

@main.route('/producto_llega_rec')
def producto_llega_rec():
    try:
        productos = ReportesModel.prod_llega_rec()

        if productos:
            return jsonify({"productos": productos}), 200  # Respuesta exitosa
        else:
            return jsonify({"productos": [], "mensaje": "No hay datos disponibles"}), 200
    except Exception as ex:
        print(f"Error en la ruta /producto_llega_rec: {str(ex)}")
        return jsonify({"error": "Ocurrió un error en el servidor"}), 500
