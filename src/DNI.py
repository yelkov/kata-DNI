from src.tablaAsignacion import tablaAsignacion

class Dni:

    LENDNI = 9

    def __init__(self, dni):
        self.tabla = tablaAsignacion()
        self.dni = dni
    
    def getNumbers(self):
        try:
            return int(self.dni[:8])
        except ValueError:
            return None 
    
    def getLetter(self):
        return self.dni[-1]

    def checkLen(self):
        return len(self.dni) == self.LENDNI        

    def checkNumbers(self):
        return  True if self.getNumbers() else False

    def checkLetter(self):
        return self.getLetter() in self.tabla.getTabla()
    
