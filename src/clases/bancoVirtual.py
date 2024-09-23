class BancoVirtual:

    def __init__(self):
        self._serviciosDisponibles = []
        self._clientesAsociados = []
        self._cuentasCreadas = []
    
    def getServiciosDisponibles(self):
        return self._serviciosDisponibles
    
    def getClientesAsociados(self):
        return self._clientesAsociados
    
    def getCuentasCreadas(self):
        return self._cuentasCreadas