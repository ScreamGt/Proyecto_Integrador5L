# herramienta para dar formato a la fecha
# from utils.DateFormat import DateFormat

class Productos:
    #constructor productos
    def __init__(self, codigo_producto, nombre = None, precio_libra = None, estado = None, nombre_categoria = None) -> None:
        self.codigo_producto = codigo_producto
        self.nombre = nombre
        self.precio_libra = precio_libra
        self.estado = estado
        self.nombre_categoria = nombre_categoria

    #conversor a formato JSON de los datos de un productto
    def to_JSON(self):
        return {
            'codigo_producto': self.codigo_producto,
            'nombre': self.nombre,
            'precio_libra': self.precio_libra,
            'estado': self.estado,
            'nombre_categoria': self.nombre_categoria
        }
