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
                cursor.execute("SELECT  * From productos where estado = 'activo'")
                resultset = cursor.fetchall()
                #print(resultset) para revisar si se recuperaron los datos de la BD

                #Guardar productos en la lista con formato JSON
                for row in resultset:
                    producto = Productos(row[0], row[1], row[2], row[3], row[4])
                    productos.append(producto.to_JSON())

            #Cerrar conexion BD
            connection.close()
            return productos if productos else False
        
        #Manejar en caso de Error
        except Exception as ex:
            print(f"Error en get_productos: {str(ex)}")  # Imprime el error en consola
            raise Exception(ex)
    
    # Método para traer productos con un nombre parecido
    @classmethod
    def get_producto(self, nombre):
        try:
            connection = get_connection()
            productos = []

            # Query para obtener productos cuyo nombre sea parecido al dado
            with connection.cursor() as cursor:
                cursor.execute("""SELECT codigo_producto, nombre, precio_libra, estado, id_categoria FROM productos
                    WHERE estado = 'activo' and nombre LIKE %s""", ('%' + nombre + '%',))
                rows = cursor.fetchall()
                print(rows)

                # Si se encontraron filas, convertir cada fila en un objeto productos y luego a JSON
                if rows:
                    for row in rows:
                        producto = Productos(row[0], row[1], row[2], row[3], row[4])
                        productos.append(producto.to_JSON())
                        print(producto)

            # Cerrar conexión a la BD
            connection.close()

            # Retornar la lista de proveedores en formato JSON
            return productos if productos else False
        
        # Manejar en caso de error
        except Exception as ex:
            print(f"Error en get_producto: {str(ex)}")  # Imprime el error en consola
            raise Exception(ex)


    # Metodo para insertar un producto en la BD
    @classmethod
    def add_producto(cls,codigo_producto,nombre,precio_libra,estado,nombre_categoria):
        try:
            connection = get_connection()

            # Query con procedimiento para insertar un producto
            with connection.cursor() as cursor:
                cursor.execute("CALL insertar_producto(%s, %s, %s, %s, %s)", (codigo_producto, nombre, precio_libra, estado, nombre_categoria))
                connection.commit()

            # Cerrar conexion BD y mostrar filas afectadas
            connection.close()
            return True

        # Manejar en caso de Error
        except Exception as ex:
            print(f"Error en add_producto: {str(ex)}")  # Imprime el error en consola
            raise Exception(ex)

    # Método para modificar un producto en la BD
    @classmethod
    def update_producto(cls, nombre, precio_libra, nombre_categoria):
        try:
            connection = get_connection()

            # Query con procedimiento para actualizar un producto
            with connection.cursor() as cursor:
                print(nombre, precio_libra, nombre_categoria)
                cursor.execute("CALL actualizar_producto(%s, %s, %s)", (nombre, precio_libra, nombre_categoria))
                connection.commit()

            # Cerrar conexión
            connection.close()
            return True
        
        # Manejar en caso de Error
        except Exception as ex:
            print(f"Error en update_producto: {str(ex)}")  # Imprime el error en consola


    # Metodo para eliminar un producto en la BD
    @classmethod
    def delete_producto(csl,nombre):
        try:
            connection = get_connection()

            # Query con procedimiento para insertar un proveedor
            with connection.cursor() as cursor:
                print(print(nombre))
                cursor.execute("CALL eliminar_producto(%s)", (nombre))
                connection.commit()

            # Cerrar conexion BD y mostrar filas afectadas
            connection.close()
            return True

        # Manejar en caso de Error
        except Exception as ex:
            print(f"Error en delete_producto: {str(ex)}")  # Imprime el error en consola
            raise Exception(ex)
