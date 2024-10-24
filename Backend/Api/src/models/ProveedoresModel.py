from database.db import get_connection
from .entities.Proveedores import Proveedores

class ProveedoresModel:

    #Metodo para traer todos los proveedores
    @classmethod
    def get_proveedores(self):
        try:
            connection = get_connection()
            proveedores = []

            #Query y operacion para obtener los proveedores
            with connection.cursor() as cursor:
                cursor.execute("SELECT  * From proveedores")
                resultset = cursor.fetchall()

                #Guardar proveedores en la lista con formato JSON
                for row in resultset:
                    proveedor = Proveedores(row[1], row[2], row[3], row[4])
                    proveedores.append(proveedor.to_JSON())

            #Cerrar conexion BD
            connection.close()
            return proveedores
        
        #Manejar en caso de Error
        except Exception as ex:
            raise Exception(ex)
    
    #Metodo para traer un proveedor por un dato
    # 'cedula'
    @classmethod
    def get_proveedor(self,nombre):
        try:
            connection = get_connection()

            #Query y operacion para obtener el proveedor segun su nombre
            with connection.cursor() as cursor:
                cursor.execute("SELECT  nombre_empresa, telefono, direccion, estado FROM proveedores WHERE nombre_empresa = %s", (nombre,))
                row = cursor.fetchone()

                #Guardar el proveedor en la lista con formato JSON
                proveedor = None
                if row != None :
                    proveedor = Proveedores(row[1], row[2], row[3], row[4])
                    proveedor = proveedor.to_JSON()

            #Cerrar conexion BD
            connection.close()
            return proveedor
        
        #Manejar en caso de Error
        except Exception as ex:
            raise Exception(ex)

    # Metodo para insertar un proveedor en la BD
    @classmethod
    def add_proveedor(self, proveedor):
        try:
            connection = get_connection()

            # Query con procedimiento para insertar un proveedor
            with connection.cursor() as cursor:
                print(proveedor.nombre, proveedor.telefono, proveedor.direccion, proveedor.estado)
                cursor.execute("CALL insertar_proveedor(%s, %s, %s, %s)", (proveedor.nombre, proveedor.telefono,
                    proveedor.direccion, "activo" ))
                affected_rows = cursor.rowcount
                connection.commit()

            # Cerrar conexion BD y mostrar filas afectadas
            connection.close()
            return affected_rows

        # Manejar en caso de Error
        except Exception as ex:
            raise Exception(ex)

    # Metodo para modificar un proveedor en la BD
    @classmethod
    def update_proveedor(self, proveedor):
        try:
            connection = get_connection()

            # Query con procedimiento para insertar un proveedor
            with connection.cursor() as cursor:
                print(proveedor.nombre, proveedor.telefono, proveedor.direccion)
                cursor.execute("CALL actualizar_proveedor(%s, %s, %s)", (print(proveedor.nombre, proveedor.telefono, proveedor.direccion)))
                affected_rows = cursor.rowcount
                connection.commit()

            # Cerrar conexion BD y mostrar filas afectadas
            connection.close()
            return affected_rows

        # Manejar en caso de Error
        except Exception as ex:
            raise Exception(ex)

    # Metodo para eliminar un proveedo en la BD
    @classmethod
    def delete_proveedor(self, proveedor):
        try:
            connection = get_connection()

            # Query con procedimiento para insertar un proveedor
            with connection.cursor() as cursor:
                print(print(proveedor.nombre, proveedor.telefono, proveedor.direccion, proveedor.estado))
                cursor.execute("CALL eliminar_proveedor(%s)", (proveedor.nombre, "inactivo"))
                affected_rows = cursor.rowcount
                connection.commit()

            # Cerrar conexion BD y mostrar filas afectadas
            connection.close()
            return affected_rows

        # Manejar en caso de Error
        except Exception as ex:
            raise Exception(ex)
