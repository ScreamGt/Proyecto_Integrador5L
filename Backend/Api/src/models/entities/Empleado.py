# herramienta para dar formato a la fecha
# from utils.DateFormat import DateFormat

class Empleado:
    #constructor empleado
    def __init__(self, cedula, nombre = None, correo = None, rol = None) -> None:
        self.cedula = cedula
        self.nombre = nombre
        self.correo = correo
        self.rol = rol

    #conversor a formato JSON de los datos de un empleado
    def to_JSON(self):
        return {
            'cedula': self.cedula,
            'nombre': self.nombre,
            'correo': self.correo,
            'rol': self.rol
        }