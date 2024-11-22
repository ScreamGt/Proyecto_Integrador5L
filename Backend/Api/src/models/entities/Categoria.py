# herramienta para dar formato a la fecha
# from utils.DateFormat import DateFormat

class Categoria:
    #constructor categoria
    def __init__(self, id_categoria, categoria = None,  estado = None) -> None:
        self.id_categoria = id_categoria
        self.categoria = categoria
        self.estado = estado

    #conversor a formato JSON de los datos de una categoria
    def to_JSON(self):
        return {
            'categoria': self.categoria,
            'estado': self.estado,
            
        }