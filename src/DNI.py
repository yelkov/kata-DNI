from src.tablaAsignacion import tablaAsignacion

class Dni:

    LENDNI = 9

    def __init__(self, dni):
        self.tabla = tablaAsignacion()
        self.dni = dni
    
    def checkLen(self):
        return len(self.dni) == self.LENDNI
    
    def getNumbers(self):
        try:
            return int(self.dni[:8])
        except ValueError:
            return None 
            
    def checkNumbers(self):
        return  True if self.getNumbers() else False

    def checkLetter(self):
        return self.dni[-1] in self.tabla.getTabla()
    
