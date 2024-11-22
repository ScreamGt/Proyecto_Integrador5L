from database.db import get_connection
from .entities.Proveedores import Proveedores

class ProveedoresModel:

    #Metodo para traer todos los proveedores
    @classmethod
    def get_ventas(self):
        try:
            connection = get_connection()
            proveedores = []

            #Query y operacion para obtener los proveedores
            with connection.cursor() as cursor:
                cursor.execute("SELECT  * From proveedores where Lower(estado) = Lower('activo')")
                resultset = cursor.fetchall()
                #print(resultset) para revisar si se recuperaron los datos de la BD

                #Guardar proveedores en la lista con formato JSON
                for row in resultset:
                    proveedor = Proveedores(row[0], row[1], row[2], row[3], row[4])
                    proveedores.append(proveedor.to_JSON())

            #Cerrar conexion BD
            connection.close()
            return proveedores if proveedores else False
        
        #Manejar en caso de Error
        except Exception as ex:
            print(f"Error en get_proveedores: {str(ex)}")  # Imprime el error en consola
            raise Exception(ex)
    
    # Método para traer proveedores con un nombre parecido
    @classmethod
    def get_proveedor(self, nombre):
        try:
            connection = get_connection()
            proveedores = []

            # Query para obtener proveedores cuyo nombre sea parecido al dado
            with connection.cursor() as cursor:
                cursor.execute("""SELECT id_proveedores, nombre_empresa, telefono, direccion, estado FROM proveedores
                    WHERE Lower(estado) = Lower('activo') and Lower(nombre_empresa) LIKE Lower(%s)""", ('%' + nombre + '%',))
                rows = cursor.fetchall()
                print(rows)

                # Si se encontraron filas, convertir cada fila en un objeto Proveedores y luego a JSON
                if rows:
                    for row in rows:
                        proveedor = Proveedores(row[0], row[1], row[2], row[3], row[4])
                        proveedores.append(proveedor.to_JSON())
                        print(proveedor)

            # Cerrar conexión a la BD
            connection.close()

            # Retornar la lista de proveedores en formato JSON
            return proveedores if proveedores else False
        
        # Manejar en caso de error
        except Exception as ex:
            print(f"Error en get_proveedor: {str(ex)}")  # Imprime el error en consola
            raise Exception(ex)


    # Metodo para insertar un proveedor en la BD
    @classmethod
    def add_proveedor(cls,nombre,telefono,direccion,estado):
        try:
            connection = get_connection()

            # Query con procedimiento para insertar un proveedor
            with connection.cursor() as cursor:
                cursor.execute("CALL insertar_proveedor(%s, %s, %s, %s)", (nombre, telefono, direccion, estado))
                connection.commit()

            # Cerrar conexion BD y mostrar filas afectadas
            connection.close()
            return True

        # Manejar en caso de Error
        except Exception as ex:
            print(f"Error en add_proveedores: {str(ex)}")  # Imprime el error en consola
            return False

    # Método para modificar un proveedor en la BD
    @classmethod
    def update_proveedor(cls, nombre, telefono, direccion):
        try:
            connection = get_connection()

            # Query con procedimiento para actualizar un proveedor
            with connection.cursor() as cursor:
                print(nombre, telefono, direccion)
                cursor.execute("CALL modificar_proveedor(%s, %s, %s)", (nombre, telefono, direccion))
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
    def delete_proveedor(csl,nombre,estado):
        try:
            connection = get_connection()

            # Query con procedimiento para eliminar un proveedor
            with connection.cursor() as cursor:
                print(print(nombre,estado))
                cursor.execute("CALL eliminar_proveedor(%s, %s)", (nombre, estado))
                connection.commit()

            # Cerrar conexion BD y mostrar filas afectadas
            connection.close()
            return True

        # Manejar en caso de Error
        except Exception as ex:
            print(f"Error en delete_proveedores: {str(ex)}")  # Imprime el error en consola
            raise Exception(ex)