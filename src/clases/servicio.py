class Servicio:

    def __init__(self, nombre, tipo, planesMensuales, bancoVirtual):
        self._nombre = nombre
        self._tipo = tipo
        self._planesMensuales = planesMensuales
        self._bancoVirtual = bancoVirtual
        self._bancoVirtual.getServiciosDisponibles().append(self) 

    def realizarProcesoDePago(self, planAPagar, cuentaVirtualUsuario):

        valorAPagar = self._planesMensuales[planAPagar]

        if cuentaVirtualUsuario.getSaldo() >= valorAPagar:
            cuentaVirtualUsuario.retirar(valorAPagar)
            return True
        else:
            return False
    
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