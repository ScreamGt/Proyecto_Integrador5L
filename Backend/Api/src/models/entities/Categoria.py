# herramienta para dar formato a la fecha
# from utils.DateFormat import DateFormat

class Categoria:
    #constructor empleado
    def __init__(self, id_categoria, categoria = None,  estado = None) -> None:
        self.id_categoria = id_categoria
        self.categoria = categoria
        self.estado = estado

    #conversor a formato JSON de los datos de un empleado
    def to_JSON(self):
        return {
            'categoria': self.categoria,
            'estado': self.estado,
            
        }