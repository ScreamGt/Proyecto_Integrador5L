from database.db import get_connection
from .entities.Categoria import Categoria

class CategoriaModel:

    #Metodo para traer todas las categorias 
    @classmethod
    def get_categorias(self):
        try:
            connection = get_connection()
            categorias = []

            #Query y operacion para obtener las categorias
            with connection.cursor() as cursor:
                cursor.execute("SELECT  * From categoria where estado = 'activo'")
                resultset = cursor.fetchall()
                #print(resultset) para revisar si se recuperaron los datos de la BD

                #Guardar categorias en la lista con formato JSON
                for row in resultset:
                    categoria = Categoria(row[0], row[1], row[2])
                    categorias.append(categoria.to_JSON())

            #Cerrar conexion BD
            connection.close()
            return categorias if categorias else False
        
        #Manejar en caso de Error
        except Exception as ex:
            print(f"Error en get_categorias: {str(ex)}")  # Imprime el error en consola
            raise Exception(ex)
    
    # Método para traer categoria con un nombre parecido
    @classmethod
    def get_categoria(self, nombre):
        try:
            connection = get_connection()
            categorias = []

            # Query para obtener categoria cuyo nombre sea parecido al dado
            with connection.cursor() as cursor:
                cursor.execute("""SELECT id_categoria, categoria, estado FROM categoria
                    WHERE estado = 'activo' and categoria LIKE %s""", ('%' + nombre + '%',))
                rows = cursor.fetchall()
                print(rows)

                # Si se encontraron filas, convertir cada fila en un objeto categoria y luego a JSON
                if rows:
                    for row in rows:
                        categoria = Categoria(row[0], row[1], row[2])
                        categorias.append(categoria.to_JSON())
                        print(categoria)

            # Cerrar conexión a la BD
            connection.close()

            # Retornar la lista de categorias en formato JSON
            return categorias if categorias else False
        
        # Manejar en caso de error
        except Exception as ex:
            print(f"Error en get_categoria: {str(ex)}")  # Imprime el error en consola
            raise Exception(ex)


    # Metodo para insertar una categoria en la BD
    @classmethod
    def add_categoria(cls,nombre,estado):
        try:
            connection = get_connection()

            # Query con procedimiento para insertar una categoria
            with connection.cursor() as cursor:
                cursor.execute("CALL insertar_categoria(%s, %s)", (nombre, estado))
                connection.commit()

            # Cerrar conexion BD y mostrar filas afectadas
            connection.close()
            return True

        # Manejar en caso de Error
        except Exception as ex:
            print(f"Error en add_categoria: {str(ex)}")  # Imprime el error en consola
            raise Exception(ex)

    

    # Metodo para eliminar una categria en la BD
    @classmethod
    def delete_categoria(csl,nombre, estado):
        try:
            connection = get_connection()

            # Query con procedimiento para insertar una categoria
            with connection.cursor() as cursor:
                print(print(nombre))
                cursor.execute("CALL eliminar_categoria(%s, %s)", (nombre, estado))
                connection.commit()

            # Cerrar conexion BD y mostrar filas afectadas
            connection.close()
            return True

        # Manejar en caso de Error
        except Exception as ex:
            print(f"Error en delete_categoria: {str(ex)}")  # Imprime el error en consola
            raise Exception(ex)
