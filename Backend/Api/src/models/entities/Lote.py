
class Lote:

#constructor lote
    def __init__(self, id_lote, fecha_llegada = None, estado_ubicacion= None, fecha_caducidad = None, peso =None, precio =None, estado=None,  nombre_proveedor = None, nombre_producto = None) -> None:
        self.id_lote = id_lote
        self.fecha_llegada = fecha_llegada
        self.estado_ubicacion = estado_ubicacion
        self.fecha_caducidad = fecha_caducidad
        self.peso = peso
        self.precio = precio
        self.estado = estado
        self.nombre_proveedor = nombre_proveedor
        self.nombre_producto = nombre_producto
        

    #conversor a formato JSON de los datos de un lote
    def to_JSON(self):
        return {
            'id_lote': self.id_lote,
            'fecha_llegada': self.fecha_llegada,
            'estado_ubicacion': self.estado_ubicacion,
            'fecha_caducidad': self.fecha_caducidad,
            'peso': self.peso,
            'precio': self.precio,
            'estado': self.estado,
            'nombre_proveedor': self.nombre_proveedor,
            'nombre_producto': self.nombre_producto,
            
            
        }
