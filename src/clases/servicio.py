class Servicio:
    
    _serViciosDisponibles = []

    def __init__(self, nombre, tipo, planesMensuales, bancoVirtual):
        self._nombre = nombre
        self._tipo = tipo
        self._planesMensuales = planesMensuales
        self._bancoVirtual = bancoVirtual

        if self._bancoVirtual is not None:
            self._bancoVirtual.getServiciosDisponibles().append(self) 

        Servicio._serViciosDisponibles.append(self)

    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getTipo(self):
        return self._tipo
    
    def setTipo(self, tipo):
        self._tipo = tipo

    def getPlanesMensuales(self):
        return self._planesMensuales
    
    def setPlanesMensuales(self, planesMensuales):
        self._planesMensuales = planesMensuales

    def getBancoVirtual(self):
        return self._bancoVirtual
    
    def setBancoVirtual(self, bancoVirtual):
        self._bancoVirtual = bancoVirtual

    @classmethod
    def getServiciosDisponibles(cls):
        return Servicio._serViciosDisponibles
    
    @classmethod
    def setServiciosDisponibles(cls, serviciosDisponibles):
        Servicio._serViciosDisponibles = serviciosDisponibles