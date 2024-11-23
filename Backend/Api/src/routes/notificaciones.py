from flask import Blueprint, jsonify
from database.db import get_connection

main = Blueprint('notificacion_blueprint', __name__)

# Ruta: Notificaciones de stock
def notify_stock():
    mensajes = []
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM notify_stock()")
        resultados = cursor.fetchall()
        for row in resultados:
            mensajes.append(row[0])  # Agregar el mensaje desde la función SQL
        cursor.close()
        conexion.close()
    except Exception as e:
        print(f"Error al ejecutar notify_stock(): {e}")
    return mensajes

# Ruta: Notificaciones de lotes que llegan hoy
def notify_lote():
    mensajes = []
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM notify_arriving_lotes()")
        resultados = cursor.fetchall()
        for row in resultados:
            mensajes.append(row[0])  # Agregar el mensaje desde la función SQL
        cursor.close()
        conexion.close()
    except Exception as e:
        print(f"Error al ejecutar notify_arriving_lotes(): {e}")
    return mensajes

# Nueva ruta combinada para notificaciones
@main.route('/notify', methods=['GET'])
def notificaciones_route():
    mensajes_stock = notify_stock()
    mensajes_lote = notify_lote()
    mensajes = mensajes_stock + mensajes_lote  # Combinar ambas listas de mensajes
    return jsonify({'mensajes': mensajes})
