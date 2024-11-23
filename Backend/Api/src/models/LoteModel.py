from database.db import get_connection
from .entities.Lote import Lote

class LoteModel:

    #Metodo para traer todos los lotes
    @classmethod
    def get_lotes(self):
        try:
            connection = get_connection()
            lotes = []

            #Query y operacion para obtener los lotes
            with connection.cursor() as cursor:
                cursor.execute("SELECT  * From ver_lotes()")
                resultset = cursor.fetchall()
                #print(resultset) para revisar si se recuperaron los datos de la BD

                #Guardar lotes en la lista con formato JSON
                for row in resultset:
                    lote = Lote(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    lotes.append(lote.to_JSON())

            #Cerrar conexion BD
            connection.close()
            return lotes if lotes else False
        
        #Manejar en caso de Error
        except Exception as ex:
            print(f"Error en get_lotes: {str(ex)}")  # Imprime el error en consola
            raise Exception(ex)
    
    # Método para traer lotes con el nombre del produto o con el estado del lote
    @classmethod
    def get_lote_estado(self, estado_lote):
        try:
            connection = get_connection()
            lotes = []

            # Query para obtener lotes cuyo estado sea parecido al dado
            with connection.cursor() as cursor:
                cursor.execute("""SELECT l.id_lote, TO_CHAR(l.fecha_llegada, 'DD-MM-YYYY')::VARCHAR, l.estado_lote, TO_CHAR(l.fecha_caducidad, 'DD-MM-YYYY')::VARCHAR, l.peso, l.precio, l.estado, p.nombre, pro.nombre_empresa FROM lote l 
                                JOIN productos p ON l.codigo_producto = p.codigo_producto JOIN proveedores pro ON l.id_proveedores = pro.id_proveedores WHERE LOWER(estado_lote) LIKE LOWER(%s) """, ('%' + estado_lote + '%',))
                rows = cursor.fetchall()
                print(rows)

                # Si se encontraron filas, convertir cada fila en un objeto Proveedores y luego a JSON
                if rows:
                    for row in rows:
                        lote = Lote(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                        lotes.append(lote.to_JSON())
                        print(lote)

            # Cerrar conexión a la BD
            connection.close()

            # Retornar la lista de los lotes en formato JSON
            return lotes if lotes else False
        
        # Manejar en caso de error
        except Exception as ex:
            print(f"Error en get_lote: {str(ex)}")  # Imprime el error en consola
            raise Exception(ex)


# Método para traer lotes con el nombre del produto
    @classmethod
    def get_lote_nombre(self, nombre_producto):
        try:
            connection = get_connection()
            lotes = []

            # Query para obtener lotes cuyo nombre o estado sea parecido al dado
            with connection.cursor() as cursor:
                cursor.execute("""SELECT l.id_lote, TO_CHAR(l.fecha_llegada, 'DD-MM-YYYY')::VARCHAR, l.estado_lote, TO_CHAR(l.fecha_caducidad, 'DD-MM-YYYY')::VARCHAR, l.peso, l.precio, l.estado, p.nombre, pro.nombre_empresa FROM lote l 
                                JOIN productos p ON l.codigo_producto = p.codigo_producto JOIN proveedores pro ON l.id_proveedores = pro.id_proveedores  WHERE LOWER(l.estado) LIKE LOWER('activo') AND LOWER(p.nombre) LIKE LOWER(%s)""", ('%' + nombre_producto + '%',))
                rows = cursor.fetchall()
                print(rows)

                # Si se encontraron filas, convertir cada fila en un objeto Lote y luego a JSON
                if rows:
                    for row in rows:
                        lote = Lote(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                        lotes.append(lote.to_JSON())
                        print(lote)

            # Cerrar conexión a la BD
            connection.close()

            # Retornar la lista de los lotes en formato JSON
            return lotes if lotes else False
        
        # Manejar en caso de error
        except Exception as ex:
            print(f"Error en get_lote: {str(ex)}")  # Imprime el error en consola
            raise Exception(ex)

    # Metodo para insertar un lote en la BD
    @classmethod
    def add_lote(cls,nombre_producto,nombre_proveedor,fecha_llegada,peso, precio):
        try:
            connection = get_connection()

            # Query con procedimiento para insertar un lote
            with connection.cursor() as cursor:
                cursor.execute("CALL insertar_lote(%s, %s, %s, %s, %s)",(str(nombre_producto), str(nombre_proveedor), fecha_llegada, float(peso), float(precio)))
                connection.commit()

            # Cerrar conexion BD y mostrar filas afectadas
            connection.close()
            return True

        # Manejar en caso de Error
        except Exception as ex:
            print(f"Error en add_lote: {str(ex)}")  # Imprime el error en consola
            return False

    # Método para modificar un proveedor en la BD
    @classmethod
    def update_lote(cls, id_lote,fecha_llegada,peso,precio):
        try:
            connection = get_connection()

            # Query con procedimiento para actualizar un proveedor
            with connection.cursor() as cursor:
                print(id_lote,fecha_llegada, peso, precio)
                cursor.execute("CALL  modificar_lote(%s, %s, %s, %s)", (id_lote,fecha_llegada,peso,precio))
                connection.commit()

            # Cerrar conexión
            connection.close()
            return True
        
        # Manejar en caso de Error
        except Exception as ex:
            print(f"Error en update_proveedores: {str(ex)}")  # Imprime el error en consola
            return False

    # Metodo para eliminar un proveedo en la BD
    @classmethod
    def delete_lote(csl,id_lote):
        try:
            connection = get_connection()

            # Query con procedimiento para eliminar un proveedor
            with connection.cursor() as cursor:
                print(print( id_lote))
                cursor.execute("CALL eliminar_lote(%s)", ( id_lote,))
                connection.commit()

            # Cerrar conexion BD y mostrar filas afectadas
            connection.close()
            return True

        # Manejar en caso de Error
        except Exception as ex:
            print(f"Error en delete_proveedores: {str(ex)}")  # Imprime el error en consola
            raise Exception(ex)