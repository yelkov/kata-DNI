class tablaAsignacion:
    
    def __init__(self):
        self.tabla = [  
            "T",
            "R",
            "W",
            "A",
            "G",
            "M",
            "Y",
            "F",
            "P",
            "D",
            "X",
            "B",
            "N",
            "J",
            "Z",
            "S",
            "Q",
            "V",
            "H",
            "L",
            "C",
            "K",
            "E",
        ]
        
    def getTabla(self):
        return self.tabla

    def getLetra(self,posicion):
        return tablaAsignacion.getTabla(self)[posicion]
    
    def getLength(self):
        return len(tablaAsignacion.getTabla(self))
    
    def getPosition(self,DNI):
        return int(DNI) % tablaAsignacion.getLength(self)
    
    def calculateLetter(self,DNI):
        return tablaAsignacion.getLetra(self, tablaAsignacion.getPosition(self,DNI))

