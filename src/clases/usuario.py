class Usuario:
    
    def __init__(self, cuenta = None, nombre = "", edad = 0):
        
        self.cuenta = cuenta
        self.nombre = nombre
        self.edad = edad

    def getCuenta(self):
        return self.cuenta

    def setCuenta(self, cuenta):
        self.cuenta = cuenta

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad