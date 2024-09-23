class BancoVirtual:

    def __init__(self):
        self._serviciosDisponibles = []
        self._clientesAsociados = []
        self._cuentasCreadas = []
    
    def buscarClientePorNumeroDeCelular(self, numeroCelular):
        for cliente in self._clientesAsociados:
            if cliente.getNumeroCelular() == numeroCelular: 
                return cliente
        
        return None
    
    def filtrarTiposDeServiciosDisponibles(self):
        tiposDeServicios = []

        for servicio in self._serviciosDisponibles:
            if servicio.getTipo() not in tiposDeServicios:
                tiposDeServicios.append(servicio.getTipo())
        
        return tiposDeServicios
    
    def filtrarServiciosPorTipo(self, tipoServicio):
        return list(filter(lambda servicio: servicio.getTipo() == tipoServicio, self._serviciosDisponibles))

    def getServiciosDisponibles(self):
        return self._serviciosDisponibles
    
    def getClientesAsociados(self):
        return self._clientesAsociados
    
    def getCuentasCreadas(self):
        return self._cuentasCreadas