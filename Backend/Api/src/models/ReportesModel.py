from database.db import get_connection

class ReportesModel:

    @classmethod
    def get_prod_mas_lotes(self):
        print("entro a la funcion")
        try:
            connection = get_connection()
            # Lista para almacenar los resultados
            productos = []

            # Consulta para obtener el producto con más lotes
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT p.nombre AS Producto, COUNT(l.id_lote) AS Total_Lotes 
                    FROM lote l 
                    INNER JOIN productos p ON l.codigo_producto = p.codigo_producto 
                    GROUP BY p.nombre 
                    ORDER BY Total_Lotes DESC 
                    LIMIT 1;
                """)
                resultset = cursor.fetchall()

                # Convertir el resultset a una lista de diccionarios
                for row in resultset:
                    productos.append({
                        'nombre': row[0],         # Nombre del producto
                        'total_lotes': row[1]     # Total de lotes
                    })

            # Cerrar conexión
            connection.close()
            print("conexion cerrada")
            return productos if productos else False

        except Exception as ex:
            print(f"Error en get_prod_mas_lotes: {str(ex)}")
            raise Exception(ex)
        

    @classmethod
    def prod_llega_rec(cls):
        try:
            connection = get_connection()
            productos = []  # Lista para almacenar los resultados

            # Consulta para obtener el producto con más lotes
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT 
                        p.nombre AS Producto, 
                        l.fecha_llegada AS Fecha_Llegada
                    FROM 
                        lote l
                    INNER JOIN 
                        producto p
                    ON 
                        l.codigo_producto = p.codigo_producto
                    ORDER BY 
                        l.fecha_llegada DESC
                    LIMIT 1;
                """)
                resultset = cursor.fetchall()

                # Verificar si hay resultados y convertir a lista de diccionarios
                for row in resultset:
                    productos.append({
                        'nombre': row['Producto'],       # Usa el alias definido en la consulta
                        'fecha_llegada': row['Fecha_Llegada'].strftime('%Y-%m-%d')  # Formato legible
                    })

            connection.close()
            return productos if productos else []  # Retorna lista vacía si no hay datos

        except Exception as ex:
            print(f"Error en prod_llega_rec: {str(ex)}")
            return []

