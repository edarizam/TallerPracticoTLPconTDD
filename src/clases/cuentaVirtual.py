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
            return f"Se han retirado {valor}$ exitosamente de tu cuenta"

        elif valor > 0 and valor > self._saldo:
            return f"Error: Fondos insuficientes, te hacen falta {valor - self._saldo}$"

        elif valor < 0:
            return "Error: No se puede retirar un monto negativo"
        
        elif valor == 0:
            return "Error: No se puede retirar un monto nulo"
        
    def consignar(self, valor):

        if valor > 0:
            self._saldo += valor
            return f"Se han consignado {valor}$ exitosamente a tu cuenta"
        elif valor ==0:
            return "Error: No puedes consignar un valor nulo"
        elif valor <0:
            return "Error: No puedes consignar un valor negativo"
        
    @classmethod
    def crearId(cls, bancoVirtual):
        return f'ID-{len(bancoVirtual.getCuentasCreadas())}'
    
    def enviarDinero(self, contraseña = "", numeroCuenta = 0, valor = 0):

        if self._contraseña == contraseña:
            listaNumeros = list(usuario.getNumeroCelular() for usuario in self._usuario.getBancoVirtual().getClientesAsociados())
            if numeroCuenta in listaNumeros:
                indice = listaNumeros.index(numeroCuenta)
                if valor == 0:
                    return "No se puede enviar un valor nulo"
                elif valor < 0:
                    return "No se puede enviar un valor negativo"
                elif valor > 0 and valor > self._saldo:
                    return f"No tienes saldo suficiente, te hacen falta {valor-self._saldo}$"
                else:
                    self._saldo-=valor
                    self._usuario.getBancoVirtual().getClientesAsociados()[indice].getCuenta().setSaldo(self._usuario.getBancoVirtual().getClientesAsociados()[indice].getCuenta().getSaldo()+valor)
                    return f"Se han enviado {valor}$ exitosamente"
            else: 
                return "El numero de cuenta ingresado no existe, intentalo de nuevo"
        else:
            return "Contraseña incorrecta, vuelva a intentarlo"

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