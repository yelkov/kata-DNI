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

    def getLetter(self,posicion):
        return tablaAsignacion().getTabla()[posicion]
    
    def getLength(self):
        return len(tablaAsignacion().getTabla())
    
    def getPosition(self,DNI):
        return int(DNI) % tablaAsignacion().getLength()
    
    def calculateLetter(self,DNI):
        return tablaAsignacion().getLetter(tablaAsignacion().getPosition(DNI))

    def __repr__(self) -> str:
        return str(tablaAsignacion().getTabla())
