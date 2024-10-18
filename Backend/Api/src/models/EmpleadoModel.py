from database.db import get_connection
from .entities.Empleado import Empleado

class EmpleadoModel:

    #Metodo para traer todos los empleados
    @classmethod
    def get_empleados(self):
        try:
            connection = get_connection()
            empleados = []

            #Query y operacion para obtener los empleados
            with connection.cursor() as cursor:
                cursor.execute("SELECT  * From empleados")
                resultset = cursor.fetchall()

                #Guardar Empleados en la lista con formato JSON
                for row in resultset:
                    empleado = Empleado(row[0], row[1], row[2], row[3])
                    empleados.append(empleado.to_JSON())

            #Cerrar conexion BD
            connection.close()
            return empleados
        
        #Manejar en caso de Error
        except Exception as ex:
            raise Exception(ex)
    
    #Metodo para traer un empleado por un dato
    # 'cedula'
    @classmethod
    def get_empleado(self,cedula):
        try:
            connection = get_connection()

            #Query y operacion para obtener el empleado segun su cedula
            with connection.cursor() as cursor:
                cursor.execute("SELECT  cedula_empleado,nombre_completo,correo,rol From Empleados where cedula_empleado = %s", (cedula,))
                row = cursor.fetchone()

                #Guardar el Empleado en la lista con formato JSON
                empleado = None
                if row != None :
                    empleado = Empleado(row[0], row[1], row[2], row[3])
                    empleado = empleado.to_JSON()

            #Cerrar conexion BD
            connection.close()
            return empleado
        
        #Manejar en caso de Error
        except Exception as ex:
            raise Exception(ex)

    # Método para insertar un empleado en la BD
    @classmethod
    def add_empleado(self, empleado):
        try:
            connection = get_connection()

            # Query con procedimiento para insertar un empleado
            with connection.cursor() as cursor:
                print(empleado.cedula, empleado.nombre, empleado.correo, empleado.rol)
                cursor.execute("CALL insertar_empleado(%s, %s, %s, %s)", (empleado.cedula, empleado.nombre,
                    empleado.correo, "Empleado"))
                affected_rows = cursor.rowcount
                connection.commit()

            # Cerrar conexión BD y mostrar filas afectadas
            connection.close()
            return affected_rows

        # Manejar en caso de Error
        except Exception as ex:
            raise Exception(ex)

    # Método para insertar un empleado en la BD
    @classmethod
    def update_empleado(self, empleado):
        try:
            connection = get_connection()

            # Query con procedimiento para insertar un empleado
            with connection.cursor() as cursor:
                print(empleado.cedula, empleado.nombre, empleado.correo, empleado.rol)
                cursor.execute("CALL actualizar_empleado(%s, %s, %s)", (empleado.cedula, empleado.nombre, empleado.correo,))
                affected_rows = cursor.rowcount
                connection.commit()

            # Cerrar conexión BD y mostrar filas afectadas
            connection.close()
            return affected_rows

        # Manejar en caso de Error
        except Exception as ex:
            raise Exception(ex)

    # Método para insertar un empleado en la BD
    @classmethod
    def delete_empleado(self, empleado):
        try:
            connection = get_connection()

            # Query con procedimiento para insertar un empleado
            with connection.cursor() as cursor:
                print(empleado.cedula, empleado.nombre, empleado.correo, empleado.rol)
                cursor.execute("CALL eliminar_empleado(%s)", (empleado.cedula,))
                affected_rows = cursor.rowcount
                connection.commit()

            # Cerrar conexión BD y mostrar filas afectadas
            connection.close()
            return affected_rows

        # Manejar en caso de Error
        except Exception as ex:
            raise Exception(ex)
