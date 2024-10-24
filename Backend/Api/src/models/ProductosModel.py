from database.db import get_connection
from .entities.Productos import Productos

class ProductosModel:

    #Metodo para traer todos los productos
    @classmethod
    def get_productos(self):
        try:
            connection = get_connection()
            productos = []

            #Query y operacion para obtener los productos
            with connection.cursor() as cursor:
                cursor.execute("SELECT  * FROM productos")
                resultset = cursor.fetchall()

                #Guardar productos en la lista con formato JSON
                for row in resultset:
                    producto = Productos(row[1], row[2], row[3], row[4])
                    productos.append(producto.to_JSON())

            #Cerrar conexion BD
            connection.close()
            return productos
        
        #Manejar en caso de Error
        except Exception as ex:
            raise Exception(ex)
    
    #Metodo para traer un producto por un dato
    # 'nombre'
    @classmethod
    def get_producto(self,nombre):
        try:
            connection = get_connection()

            #Query y operacion para obtener el producto segun su nombre
            with connection.cursor() as cursor:
                cursor.execute("SELECT  nombre, precio_libra, estado FROM productos WHERE nombre = %s", (nombre,))
                row = cursor.fetchone()

                #Guardar el producto en la lista con formato JSON
                producto = None
                if row != None :
                    producto = Productos(row[1], row[2], row[3])
                    producto = producto.to_JSON()

            #Cerrar conexion BD
            connection.close()
            return producto
        
        #Manejar en caso de Error
        except Exception as ex:
            raise Exception(ex)

    # Método para insertar un producto en la BD
    @classmethod
    def add_producto(self, producto):
        try:
            connection = get_connection()

            # Query con procedimiento para insertar un producto
            with connection.cursor() as cursor:
                print(producto.nombre, producto.precio_libra, producto.estado, producto.id_categoria)
                cursor.execute("CALL insertar_producto(%s, %s, %s, %s)", (producto.nombre, producto.precio_libra, "activo", producto.id_categoria))
                affected_rows = cursor.rowcount
                connection.commit()

            # Cerrar conexión BD y mostrar filas afectadas
            connection.close()
            return affected_rows

        # Manejar en caso de Error
        except Exception as ex:
            raise Exception(ex)

    # Mtodo para modificar un producto en la BD
    @classmethod
    def update_producto(self, producto):
        try:
            connection = get_connection()

            # Query con procedimiento para modificar un producto 
            with connection.cursor() as cursor:
                print(producto.codigo_producto, producto.nombre, producto.precio_libra, producto.estado, producto.nombre_categoria)
                cursor.execute("CALL modificar_producto(%s, %s, %s, %s, %s)", (print(producto.codigo_producto, producto.nombre, producto.precio_libra, producto.estado, producto.nombre_categoria)))
                affected_rows = cursor.rowcount
                connection.commit()

            # Cerrar conexión BD y mostrar filas afectadas
            connection.close()
            return affected_rows

        # Manejar en caso de Error
        except Exception as ex:
            raise Exception(ex)

    # Método para eliminar un producto en la BD
    @classmethod
    def delete_producto(self, producto):
        try:
            connection = get_connection()

            # Query con procedimiento para elimnar un producto
            with connection.cursor() as cursor:
                print(print(producto.codigo_producto, producto.nombre, producto.precio_libra, producto.estado, producto.nombre_categoria))
                cursor.execute("CALL eliminar_producto(%s, %s, %s)", (producto.codigo_producto, producto.nombre, "inactivo"))
                affected_rows = cursor.rowcount
                connection.commit()

            # Cerrar conexión BD y mostrar filas afectadas
            connection.close()
            return affected_rows

        # Manejar en caso de Error
        except Exception as ex:
            raise Exception(ex)
