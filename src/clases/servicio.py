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
        
    def __str__(self) -> str:
        
        enumerarPlanes = ''
        i = 0

        for planMensual in self._planesMensuales.keys():
            i+=1
            enumerarPlanes += f'\n\t{i}. {planMensual}: {self._planesMensuales[planMensual]}'
        
        return f'Servicio: {self._nombre}; \nTipo: {self._tipo}, \nPlanes:{enumerarPlanes}'
    
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