class CuentaVirtual:

    def __init__(self, saldo = 0, id = 0, usuario = None, contraseña = "", bancoVirtual = None):

        self._saldo = saldo
        self._usuario = usuario
        self._id = id
        self._contraseña = contraseña
        self._bancoVirtual = bancoVirtual

        if self._bancoVirtual is not None:
            self._bancoVirtual.getCuentasCreadas().append(self) 
    

    def retirar(self, valor):

        if valor > 0 and valor < self._saldo:
            self._saldo -= valor

        elif valor > 0 and valor > self._saldo:
            return f"Error: Fondos insuficientes, te hacen falta {valor - self._saldo}$"

        elif valor < 0:
            return "Error: No se puede retirar un monto negativo"
        
        elif valor == 0:
            return "Error: No se puede retirar un monto nulo"
        
    def consignar(self, valor):

        if valor > 0:
            self._saldo += valor
        elif valor ==0:
            return "Error: No puedes consignar un valor nulo"
        elif valor <0:
            return "Error: No puedes consignar un valor negativo"
        
    @classmethod
    def crearId(cls, bancoVirtual):
        return f'ID-{len(bancoVirtual.getCuentasCreadas())}'

    def getSaldo(self):
        return self._saldo

    def setSaldo(self, saldo):
        self._saldo = saldo

    def getUsuario(self):
        return self._usuario

    def setUsuario(self, usuario):
        self._usuario = usuario

    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id

    def getContraseña(self):
        return self._contraseña
    
    def setContraseña(self, contraseña):
        self._contraseña = contraseña
    
    def getBancoVirtual(self):
        return self._bancoVirtual
    
    def setBancoVirtual(self, bancoVirtual):
        self._bancoVirtual = bancoVirtual