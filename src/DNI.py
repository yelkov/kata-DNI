from src.tablaAsignacion import tablaAsignacion

class Dni:

    LENGHT_DNI = 9
    LENGHT_DNI_NUMBERS = 8

    def __init__(self, dni):
        self.tabla = tablaAsignacion()
        self.dni = dni
    
    def getNumbers(self):
        try:
            return int(self.dni[:self.LENGHT_DNI_NUMBERS])
        except ValueError:
            return None 
    
    def getLetter(self):
        return self.dni[-1]

    def isValidLenght(self):
        return len(self.dni) == self.LENGHT_DNI        

    def checkNumbers(self):
        return  self.getNumbers() != None

    def checkLetter(self):
        return self.getLetter() in self.tabla.getTabla()
    
    def checkDni(self):
        return (
             self.isValidLenght() and 
             self.checkNumbers() and 
             self.checkLetter() and 
             self.getLetter() == self.tabla.calculateLetter(self.getNumbers())
             )


    
