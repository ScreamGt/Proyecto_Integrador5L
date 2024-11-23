from database.db import get_connection
from .entities.Ventas import Ventas

class VentasModel:

    #Metodo para traer todos las ventas
    @classmethod
    def get_ventas(self):
        try:
            connection = get_connection()
            ventas = []

            #Query y operacion para obtener los proveedores
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM obtener_informacion_ventas();")
                resultset = cursor.fetchall()
                #print(resultset) para revisar si se recuperaron los datos de la BD

                #Guardar proveedores en la lista con formato JSON
                for row in resultset:
                    venta = Ventas(fecha = row[0], nombre_producto = row[1], precio = row[2], cantidad_peso = row[3], total = row[4] )
                    ventas.append(venta.to_JSON())

            #Cerrar conexion BD
            connection.close()
            return ventas if ventas else False
        
        #Manejar en caso de Error
        except Exception as ex:
            print(f"Error en get_proveedores: {str(ex)}")  # Imprime el error en consola
            raise Exception(ex)
    
    @classmethod
    def add_venta(cls, cantidad_peso, nombre_producto):
        try:
            # Establecer la conexión a la base de datos
            connection = get_connection()

            # Validar los parámetros
            if not cantidad_peso or not nombre_producto:
                print("Error: cantidad_peso y nombre_producto son requeridos.")
                return False

            # Ejecutar el procedimiento almacenado
            with connection.cursor() as cursor:
                cursor.execute("CALL registrar_venta(%s, %s)", (cantidad_peso, nombre_producto.strip()))

            # Confirmar la transacción
            connection.commit()

            # Cerrar la conexión
            connection.close()
            return True

        except Exception as ex:
            # Manejar el error y realizar rollback
            print(f"Error en add_ventas: {str(ex)}")
            if 'connection' in locals():  # Verificar si la conexión fue creada
                connection.rollback()
                connection.close()
            return False
        




