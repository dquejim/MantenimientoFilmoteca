from dataclasses import dataclass

@dataclass
class Pelicula:
    id: int
    nombre: str
    genero : str
    anioEstreno: int

    def __init__(self,id,nombre,genero,anioEstreno):
        self.id = id
        self.nombre = nombre
        self.genero = genero
        self.anioEstreno = anioEstreno

    #Setter
    def setNombre(self, a):
        self.nombre = a

    def setGenero(self, a):
        self.genero = a

    def setAnioEstreno(self, a):
        self.anioEstreno = a

    def setId(self, a):
        self.id = a

    #Getter
    def getNombre(self):
        return self.nombre

    def getGenero(self):
        return self.genero

    def getAnioEstreno(self):
        return self.anioEstreno

    def getId(self):
        return self.id