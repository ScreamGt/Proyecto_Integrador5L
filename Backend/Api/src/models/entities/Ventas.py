
class Ventas:

#constructor ventas
    def __init__(self, id_venta, fecha = None,  estado = None) -> None:
        self.id_venta = id_venta  
        self.fecha = fecha
        self.estado = estado

    #conversor a formato JSON de los datos de una venta
    def to_JSON(self):
        return {
            'fecha': self.fecha,
            'estado': self.estado,
            
        }