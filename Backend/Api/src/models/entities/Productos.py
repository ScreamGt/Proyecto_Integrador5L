# herramienta para dar formato a la fecha
# from utils.DateFormat import DateFormat

class Productos:
    #constructor empleado
    def __init__(self, codigo_producto , nombre = None, precio_libra = None, estado = None, id_categoria = None) -> None:
        self.codigo_producto = codigo_producto
        self.nombre = nombre
        self.precio_libra = precio_libra
        self.estado = estado
        self.id_categoria = id_categoria

    #conversor a formato JSON de los datos de un empleado
    def to_JSON(self):
        return {
            'nombre': self.nombre,
            'precio libra': self.precio_libra,
            'estado': self.estado,
            'id_categoria': self.id_categoria
            
        }