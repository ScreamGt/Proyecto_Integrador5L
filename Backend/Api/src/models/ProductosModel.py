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
                cursor.execute("""SELECT p.codigo_producto,p.nombre,p.precio_libra,p.estado,c.categoria AS nombre_categoria FROM productos p 
                               JOIN categoria c ON p.id_categoria = c.id_categoria WHERE LOWER(p.estado) = LOWER('activo')""")
                resultset = cursor.fetchall()

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
    def get_producto_nombre(self, nombre):
        try:
            connection = get_connection()
            productos = []

            # Query para obtener productos cuyo nombre sea parecido al dado
            with connection.cursor() as cursor:
                cursor.execute("""SELECT p.codigo_producto,p.nombre,p.precio_libra,p.estado,c.categoria AS nombre_categoria FROM productos p 
                               JOIN categoria c ON p.id_categoria = c.id_categoria WHERE LOWER(p.estado) = LOWER('activo') AND LOWER(p.nombre) LIKE LOWER(%s)""", ('%' + nombre + '%',))
                rows = cursor.fetchall()

                # Si se encontraron filas, convertir cada fila en un objeto productos y luego a JSON
                if rows:
                    for row in rows:
                        producto = Productos(row[0], row[1], row[2], row[3], row[4])
                        productos.append(producto.to_JSON())
                        print(producto)

            # Cerrar conexión a la BD
            connection.close()
            print("termino consulta")

            # Retornar la lista de productos en formato JSON
            return productos if productos else False
        
        # Manejar en caso de error
        except Exception as ex:
            print(f"Error en get_producto_nombre: {str(ex)}")  # Imprime el error en consola
            raise Exception(ex)
        
    # Método para traer productos con una categoria en concreto
    @classmethod
    def get_producto_categoria(self, nombre_categoria):
        try:
            connection = get_connection()
            productos = []

            # Query para obtener productos cuyo nombre sea parecido al dado
            with connection.cursor() as cursor:
                cursor.execute("""SELECT p.codigo_producto,p.nombre,p.precio_libra,p.estado,c.categoria AS nombre_categoria FROM productos p 
                               JOIN categoria c ON p.id_categoria = c.id_categoria WHERE LOWER(p.estado) = LOWER('activo') AND LOWER(c.categoria) LIKE LOWER(%s)""", ('%' + nombre_categoria + '%',))
                rows = cursor.fetchall()

                # Si se encontraron filas, convertir cada fila en un objeto productos y luego a JSON
                if rows:
                    for row in rows:
                        producto = Productos(row[0], row[1], row[2], row[3], row[4])
                        productos.append(producto.to_JSON())
                        print(producto)

            # Cerrar conexión a la BD
            connection.close()
            print("termino consulta")

            # Retornar la lista de productos en formato JSON
            return productos if productos else False
        
        # Manejar en caso de error
        except Exception as ex:
            print(f"Error en get_producto_categoria: {str(ex)}")  # Imprime el error en consola
            raise Exception(ex)

    # Metodo para insertar un producto en la BD
    @classmethod
    def add_producto(cls, codigo_producto, nombre ,precio_libra, estado, nombre_categoria):
        try:
            connection = get_connection()

            # Query con procedimiento para insertar un producto
            with connection.cursor() as cursor:
                cursor.execute("CALL insertar_producto(%s, %s, %s, %s, %s)", (nombre_categoria, codigo_producto, nombre, precio_libra, estado))
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
                cursor.execute("CALL modificar_producto(%s, %s, %s)", (nombre_categoria, nombre, precio_libra))
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

            # Query con procedimiento para eliminar un producto
            with connection.cursor() as cursor:
                cursor.execute("CALL eliminar_producto(%s)", (nombre,))
                connection.commit()

            # Cerrar conexion BD y mostrar filas afectadas
            connection.close()
            print("termino consulta")
            return True

        # Manejar en caso de Error
        except Exception as ex:
            print(f"Error en delete_producto: {str(ex)}")  # Imprime el error en consola
            raise Exception(ex)
