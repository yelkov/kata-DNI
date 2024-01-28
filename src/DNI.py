from src.tablaAsignacion import tablaAsignacion

class Dni:

    LENDNI = 9

    def __init__(self, dni):
        self.tabla = tablaAsignacion()
        self.dni = dni
    
    def checkLen(self):
        return len(self.dni) == self.LENDNI
    
    def checkNumbers(self):
        try:
            numbers = int(self.dni[:8])
            return True
           
        except ValueError:
            return False

    def checkLetter(self):
        return self.dni[-1] in self.tabla.getTabla()