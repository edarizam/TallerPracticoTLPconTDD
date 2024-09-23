class Usuario:
    
    def __init__(self, cuenta = None, nombre = "", edad = 0, bancoVirtual = None):
        
        self._cuenta = cuenta
        self._nombre = nombre
        self._edad = edad
        self._bancoVirtual = bancoVirtual

        if self._bancoVirtual is not None:
            self._bancoVirtual.getCuentasCreadas().append(self) 

    def getCuenta(self):
        return self._cuenta

    def setCuenta(self, cuenta):
        self._cuenta = cuenta

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getBancoVirtual(self):
        return self._bancoVirtual
    
    def setBancoVirtual(self, bancoVirtual):
        self._bancoVirtual = bancoVirtual