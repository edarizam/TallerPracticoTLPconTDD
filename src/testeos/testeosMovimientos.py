import unittest
import sys

import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clases.usuario import Usuario
from clases.cuentaVirtual import CuentaVirtual
from clases.bancoVirtual import BancoVirtual

class TesteosMovimientos(unittest.TestCase):

    bancoVirtual1 = BancoVirtual()

    #Testeos de retiro de dinero

    def testRetirarDineroExitosamente(self):

        usuario = Usuario(CuentaVirtual(500000.0)) # Creamos un usuario con una cuenta con 500000 de saldo
        usuario.getCuenta().setUsuario(usuario)
        mensaje = usuario.getCuenta().retirar(499999.0)
        self.assertEqual(usuario.getCuenta().getSaldo(), 1.0)  # El saldo debe ser 1
        self.assertEqual(mensaje, "Se han retirado 499999.0$ exitosamente de tu cuenta")

    def testRetirarDineroInsuficiente(self):

        usuario = Usuario(CuentaVirtual(10000.0))
        usuario.getCuenta().setUsuario(usuario)
        mensaje = usuario.getCuenta().retirar(11000.0)
        self.assertEqual(usuario.getCuenta().getSaldo(), 10000.0)  # El saldo no debe cambiar
        self.assertEqual(mensaje, "Error: Fondos insuficientes, te hacen falta 1000.0$")

    def testRetirarDineroNegativo(self):

        usuario = Usuario(CuentaVirtual(123456789.0))
        usuario.getCuenta().setUsuario(usuario)
        mensaje = usuario.getCuenta().retirar(-987654321.0)
        self.assertEqual(usuario.getCuenta().getSaldo(), 123456789.0)  # El saldo no debe cambiar
        self.assertEqual(mensaje, "Error: No se puede retirar un monto negativo")

    def testRetirarDineroNulo(self):

        usuario = Usuario(CuentaVirtual(4000.0))
        usuario.getCuenta().setUsuario(usuario)
        mensaje = usuario.getCuenta().retirar(0.0)
        self.assertEqual(usuario.getCuenta().getSaldo(), 4000.0)  # El saldo no debe cambiar
        self.assertEqual(mensaje, "Error: No se puede retirar un monto nulo")


    #Testeos de consignar dinero

    def testConsignarDineroExitosamente(self):

        usuario = Usuario(CuentaVirtual(0.0))
        usuario.getCuenta().setUsuario(usuario)
        mensaje = usuario.getCuenta().consignar(5000.0)
        self.assertEqual(mensaje, "Se han consignado 5000.0$ exitosamente a tu cuenta")
        self.assertEqual(usuario.getCuenta().getSaldo(), 5000.0)
    
    def testConsignarDineroNulo(self):

        usuario = Usuario(CuentaVirtual(80000.0))
        usuario.getCuenta().setUsuario(usuario)
        mensaje = usuario.getCuenta().consignar(0.0)
        self.assertEqual(usuario.getCuenta().getSaldo(), 80000.0) #No cambia el saldo
        self.assertEqual(mensaje, "Error: No puedes consignar un valor nulo")
    
    def testConsignarDineroNegativo(self):

        usuario = Usuario(CuentaVirtual(69000.0))
        usuario.getCuenta().setUsuario(usuario)
        mensaje = usuario.getCuenta().consignar(-1000.0)
        self.assertEqual(usuario.getCuenta().getSaldo(), 69000.0) #No cambia el saldo
        self.assertEqual(mensaje, "Error: No puedes consignar un valor negativo")
    

    #testeos del envio de dinero

    def testEnviarDineroContraseñaIncorrecta(self):

        usuario = Usuario(cuenta = CuentaVirtual(saldo = 70000.0, contraseña=1234), numeroCelular = 3016534290, nombre="Juan Jose")
        usuario.getCuenta().setUsuario(usuario)

        mensaje = usuario.getCuenta().enviarDinero(contraseña = 1478)

        self.assertEqual(usuario.getCuenta().getSaldo(), 70000) #No cambia el saldo
        self.assertEqual(mensaje, "Contraseña incorrecta, vuelva a intentarlo")

    def testEnviarDineroCuentaInexistente(self):

        usuario = Usuario(cuenta = CuentaVirtual(saldo = 70000.0, contraseña=1234, bancoVirtual= TesteosMovimientos.bancoVirtual1), numeroCelular = 3016534290, nombre="Juan Jose", bancoVirtual= TesteosMovimientos.bancoVirtual1)
        usuario.getCuenta().setUsuario(usuario)
        
        mensaje = usuario.getCuenta().enviarDinero(contraseña = 1234, numeroCuenta = 123456789)

        self.assertEqual(usuario.getCuenta().getSaldo(), 70000) #No cambia el saldo
        self.assertEqual(mensaje, "El numero de cuenta ingresado no existe, intentalo de nuevo")

    def testEnviarDineroNulo(self):

        TesteosMovimientos.bancoVirtual1.getClientesAsociados().clear()
        TesteosMovimientos.bancoVirtual1.getCuentasCreadas().clear()

        usuario = Usuario(cuenta = CuentaVirtual(saldo = 70000.0, contraseña=1234, bancoVirtual= TesteosMovimientos.bancoVirtual1), numeroCelular = 3016534290, nombre="Juan Jose", bancoVirtual= TesteosMovimientos.bancoVirtual1)
        usuario.getCuenta().setUsuario(usuario)
        
        usuario2 = Usuario(cuenta = CuentaVirtual(saldo = 80000.0, contraseña=1217, bancoVirtual= TesteosMovimientos.bancoVirtual1), numeroCelular = 3116274690, nombre="Maria", bancoVirtual= TesteosMovimientos.bancoVirtual1)
        usuario2.getCuenta().setUsuario(usuario2)

        mensaje = usuario.getCuenta().enviarDinero(contraseña = 1234, numeroCuenta = 3116274690, valor = 0.0)

        self.assertEqual(usuario.getCuenta().getSaldo(), 70000) #No cambia el saldo
        self.assertEqual(mensaje, "No se puede enviar un valor nulo")

    def testEnviarDineroNegativo(self):

        TesteosMovimientos.bancoVirtual1.getClientesAsociados().clear()
        TesteosMovimientos.bancoVirtual1.getCuentasCreadas().clear()

        usuario = Usuario(cuenta = CuentaVirtual(saldo = 70000.0, contraseña=1234, bancoVirtual= TesteosMovimientos.bancoVirtual1), numeroCelular = 3016534290, nombre="Juan Jose", bancoVirtual= TesteosMovimientos.bancoVirtual1)
        usuario.getCuenta().setUsuario(usuario)
        
        usuario2 = Usuario(cuenta = CuentaVirtual(saldo = 80000.0, contraseña=1217, bancoVirtual= TesteosMovimientos.bancoVirtual1), numeroCelular = 3116274690, nombre="Maria", bancoVirtual= TesteosMovimientos.bancoVirtual1)
        usuario2.getCuenta().setUsuario(usuario2)
        
        mensaje = usuario.getCuenta().enviarDinero(contraseña = 1234, numeroCuenta = 3116274690, valor = -10000)

        self.assertEqual(usuario.getCuenta().getSaldo(), 70000) #No cambia el saldo
        self.assertEqual(mensaje, "No se puede enviar un valor negativo")

    def testEnviarDineroSaldoInsuficiente(self):

        TesteosMovimientos.bancoVirtual1.getClientesAsociados().clear()
        TesteosMovimientos.bancoVirtual1.getCuentasCreadas().clear()

        usuario = Usuario(cuenta = CuentaVirtual(saldo = 70000.0, contraseña=1234, bancoVirtual= TesteosMovimientos.bancoVirtual1), numeroCelular = 3016534290, nombre="Juan Jose", bancoVirtual= TesteosMovimientos.bancoVirtual1)
        usuario.getCuenta().setUsuario(usuario)
        
        usuario2 = Usuario(cuenta = CuentaVirtual(saldo = 80000.0, contraseña=1217, bancoVirtual= TesteosMovimientos.bancoVirtual1), numeroCelular = 3116274690, nombre="Maria", bancoVirtual= TesteosMovimientos.bancoVirtual1)
        usuario2.getCuenta().setUsuario(usuario2)
        
        mensaje = usuario.getCuenta().enviarDinero(contraseña = 1234, numeroCuenta = 3116274690, valor = 75000)

        self.assertEqual(usuario.getCuenta().getSaldo(), 70000) #No cambia el saldo
        self.assertEqual(mensaje, "No tienes saldo suficiente, te hacen falta 5000.0$")

    def testEnviarDineroAsimismo(self):
        TesteosMovimientos.bancoVirtual1.getClientesAsociados().clear()
        TesteosMovimientos.bancoVirtual1.getCuentasCreadas().clear()

        usuario = Usuario(cuenta = CuentaVirtual(saldo = 70000.0, contraseña=1234, bancoVirtual= TesteosMovimientos.bancoVirtual1), numeroCelular = 3016534290, nombre="Juan Jose", bancoVirtual= TesteosMovimientos.bancoVirtual1)
        usuario.getCuenta().setUsuario(usuario)

        mensaje = usuario.getCuenta().enviarDinero(contraseña = 1234, numeroCuenta = 3016534290, valor = 50000.0)

        self.assertEqual(usuario.getCuenta().getSaldo(), 70000.0) #No cambia el saldo
        self.assertEqual(mensaje, "Error: No puedes enviarte dinero a tu misma cuenta, utiliza la opcion de consignar")


    def testEnviarDineroExitosamente(self):

        TesteosMovimientos.bancoVirtual1.getClientesAsociados().clear()
        TesteosMovimientos.bancoVirtual1.getCuentasCreadas().clear()

        usuario = Usuario(cuenta = CuentaVirtual(saldo = 70000.0, contraseña=1234, bancoVirtual= TesteosMovimientos.bancoVirtual1), numeroCelular = 3016534290, nombre="Juan Jose", bancoVirtual= TesteosMovimientos.bancoVirtual1)
        usuario.getCuenta().setUsuario(usuario)
        
        usuario2 = Usuario(cuenta = CuentaVirtual(saldo = 80000.0, contraseña=1217, bancoVirtual= TesteosMovimientos.bancoVirtual1), numeroCelular = 3116274690, nombre="Maria", bancoVirtual= TesteosMovimientos.bancoVirtual1)
        usuario2.getCuenta().setUsuario(usuario2)
        
        mensaje = usuario.getCuenta().enviarDinero(contraseña = 1234, numeroCuenta = 3116274690, valor = 50000.0)

        self.assertEqual(usuario.getCuenta().getSaldo(), 20000) 
        self.assertEqual(usuario2.getCuenta().getSaldo(), 130000.0) 
        self.assertEqual(mensaje, "Se han enviado 50000.0$ exitosamente a Maria")


if __name__ == "__main__":
    unittest.main()



