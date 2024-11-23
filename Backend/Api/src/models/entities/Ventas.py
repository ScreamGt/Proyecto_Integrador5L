
class Ventas:

#constructor ventas
    def __init__(self,id_venta, cantidad_peso = None, nombre_producto = None, fecha = None,  estado = None) -> None:
        self.cantidad_peso = cantidad_peso
        self.nombre_producto = nombre_producto
        self.id_venta = id_venta  
        self.fecha = fecha
        self.estado = estado

    #conversor a formato JSON de los datos de una venta
    def to_JSON(self):
        return {
            'cantidad_peso': self.cantidad_peso,
            'nombre_producto': self.nombre_producto,
            'fecha': self.fecha,
            'estado': self.estado,
            
        }