import unittest
import sys

import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clases.usuario import Usuario
from clases.cuentaVirtual import CuentaVirtual


class testeosMovimientos(unittest.TestCase):

    #Testeos de retiro de dinero

    def testRetirarDineroExitosamente(self):

        usuario = Usuario(CuentaVirtual(500000.0)) # Creamos un usuario con una cuenta con 500000 de saldo
        usuario.getCuenta().setUsuario(usuario)
        usuario.getCuenta().retirar(499999.0)
        self.assertEqual(usuario.getCuenta().getSaldo(), 1.0)  # El saldo debe ser 1

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
        usuario.getCuenta().consignar(5000.0)
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
    





    

if __name__ == "__main__":
    unittest.main()



