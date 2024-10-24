# herramienta para dar formato a la fecha
# from utils.DateFormat import DateFormat

class Proveedores:
    #constructor empleado
    def __init__(self, id_proveedor, nombre = None, telefono = None, direccion = None, estado = None) -> None:
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.estado = estado
        

    #conversor a formato JSON de los datos de un proveedor
    def to_JSON(self):
        return {
            'nombre': self.nombre,
            'telefono': self.telefonoo,
            'direccion': self.direccion,
            'estado': self.estado,

        }