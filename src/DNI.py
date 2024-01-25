from src.tablaAsignacion import tablaAsignacion

class Dni:

    LENDNI = 9

    def __init__(self, dni):
        tabla = tablaAsignacion().getTabla()
        self.dni = dni
    
    def checkLen(self):
        return len(self.dni) == self.LENDNI