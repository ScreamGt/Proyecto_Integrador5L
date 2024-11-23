
class Ventas:

#constructor ventas
    def __init__(self,id_venta = None, fecha = None, nombre_producto = None, precio = None, cantidad_peso = None,  total = None,  estado = None) -> None:
        self.fecha = fecha
        self.nombre_producto = nombre_producto
        self.precio = precio
        self.cantidad_peso = cantidad_peso
        self.total = total
        self.id_venta = id_venta  
        
        self.estado = estado
        

    #conversor a formato JSON de los datos de una venta
    def to_JSON(self):
        return {
            'fecha': self.fecha,
            'nombre_producto': self.nombre_producto,
            'precio': self.precio,
            'cantidad_peso': self.cantidad_peso,
            'total': self.total,
            'estado': self.estado,
            
        }