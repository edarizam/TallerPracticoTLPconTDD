class CuentaVirtual:

    def __init__(self, saldo = 0, id = 0, usuario = None):

        self.saldo = saldo
        self.usuario = usuario
        self.id = id
    

    def retirar(self, valor):

        if valor > 0 and valor < self.saldo:
            self.saldo -= valor

        elif valor > 0 and valor > self.saldo:
            return f"Error: Fondos insuficientes, te hacen falta {valor - self.saldo}$"

        elif valor < 0:
            return "Error: No se puede retirar un monto negativo"
        
        elif valor ==0:
            return "Error: No se puede retirar un monto nulo"
        
    def consignar(self, valor):

        if valor > 0:
            self.saldo += valor
        elif valor ==0:
            return "Error: No puedes consignar un valor nulo"
        elif valor <0:
            return "Error: No puedes consignar un valor negativo"
        
        



    def getSaldo(self):
        return self.saldo

    def setSaldo(self, saldo):
        self.saldo = saldo

    def getUsuario(self):
        return self.usuario

    def setUsuario(self, usuario):
        self.usuario = usuario

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id
    