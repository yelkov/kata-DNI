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
        
    def getListaLetra(self):
        return self.tabla
    
    def getNumLetras(self):
        return len(self.tabla)
    
    def getLetra(self):
        
    
    def calcularLetra(self,DNI):
        posicion = int(DNI) % self.getNumLetras()
        return 
    
    def __repr__(self) -> str:
        return self.getListaLetra