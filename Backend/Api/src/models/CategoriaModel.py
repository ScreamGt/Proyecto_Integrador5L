from database.db import get_connection
from .entities.Categoria import Categoria

class CategoriasModel:

    #Metodo para traer todos los categorias
    @classmethod
    def get_Categorias(self):
        try:
            connection = get_connection()
            categorias = []

            #Query y operacion para obtener los categorias
            with connection.cursor() as cursor:
                cursor.execute("SELECT  * From categoria")
                resultset = cursor.fetchall()

                #Guardar categorias en la lista con formato JSON
                for row in resultset:
                    Categoria = Categoria(row[1], row[2])
                    categorias.append(Categoria.to_JSON())

            #Cerrar conexion BD
            connection.close()
            return categorias
        
        #Manejar en caso de Error
        except Exception as ex:
            raise Exception(ex)
    
    #Metodo para traer una categoria por un dato
    # 'nombre'
    @classmethod
    def get_categoria(self,nombre):
        try:
            connection = get_connection()

            #Query y operacion para obtener la categoria segun su nombre
            with connection.cursor() as cursor:
                cursor.execute("SELECT  categoria, estado, FROM categoria WHERE categoria = %s", (nombre,))
                row = cursor.fetchone()

                #Guardar la categoria en la lista con formato JSON
                categoria = None
                if row != None :
                    categoria = Categoria(row[0], row[1], row[2])
                    categoria = categoria.to_JSON()

            #Cerrar conexion BD
            connection.close()
            return categoria
        
        #Manejar en caso de Error
        except Exception as ex:
            raise Exception(ex)

    # Metodo para insertar una categoria en la BD
    @classmethod
    def add_categoria(self, categoria):
        try:
            connection = get_connection()

            # Query con procedimiento para insertar un categoria
            with connection.cursor() as cursor:
                print(categoria.id_categoria, categoria.categoria,categoria.estado)
                cursor.execute("CALL insertar_categoria(%s, %s)", (categoria.categoria, "activo" ))
                affected_rows = cursor.rowcount
                connection.commit()

            # Cerrar conexion BD y mostrar filas afectadas
            connection.close()
            return affected_rows

        # Manejar en caso de Error
        except Exception as ex:
            raise Exception(ex)

    # Metodo para modificar una categoria en la BD
    @classmethod
    def update_categoria(self, categoria):
        try:
            connection = get_connection()

            # Query con procedimiento para modificar la categoria
            with connection.cursor() as cursor:
                print(categoria.id_categoria, categoria.categoria, categoria.estado)
                cursor.execute("CALL actualizar_categoria(%s)", (print(categoria.categoria)))
                affected_rows = cursor.rowcount
                connection.commit()

            # Cerrar conexion BD y mostrar filas afectadas
            connection.close()
            return affected_rows

        # Manejar en caso de Error
        except Exception as ex:
            raise Exception(ex)

    # Metodo para eliminar una categoria en la BD
    @classmethod
    def delete_categoria(self, categoria):
        try:
            connection = get_connection()

            # Query con procedimiento para insertar un proveedor
            with connection.cursor() as cursor:
                #print(print(proveedor.nombre, proveedor.telefono, proveedor.direccion, proveedor.estado))
                cursor.execute("CALL eliminar_categoria(%s, %s)", (categoria.categoria, "inactivo"))
                affected_rows = cursor.rowcount
                connection.commit()

            # Cerrar conexion BD y mostrar filas afectadas
            connection.close()
            return affected_rows

        # Manejar en caso de Error
        except Exception as ex:
            raise Exception(ex)