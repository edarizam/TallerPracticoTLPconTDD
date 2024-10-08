import unittest
import sys

import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clases.usuario import Usuario
from clases.cuentaVirtual import CuentaVirtual
from clases.bancoVirtual import BancoVirtual

class TesteosCuentaVirtual(unittest.TestCase):


    bancoVirtual1 = BancoVirtual()

    def testCrearCuentaVirtual(self):

        #Testeamos diferentes formas de crear una cuenta virtual

        cuenta1 = CuentaVirtual()

        self.assertEqual(cuenta1.getSaldo(), 0)
        self.assertEqual(cuenta1.getId(), 0)
        self.assertEqual(cuenta1.getUsuario(), None)
        self.assertEqual(cuenta1.getContraseña(), "")
        self.assertEqual(cuenta1.getBancoVirtual(), None)

        cuenta2 = CuentaVirtual(25000.0)

        self.assertEqual(cuenta2.getSaldo(), 25000.0)
        self.assertEqual(cuenta2.getId(), 0)
        self.assertEqual(cuenta2.getUsuario(), None)
        self.assertEqual(cuenta2.getContraseña(), "")
        self.assertEqual(cuenta2.getBancoVirtual(), None)

        cuenta3 = CuentaVirtual(1200, 976259)

        self.assertEqual(cuenta3.getSaldo(), 1200.0)
        self.assertEqual(cuenta3.getId(), 976259)
        self.assertEqual(cuenta3.getUsuario(), None)
        self.assertEqual(cuenta3.getContraseña(), "")
        self.assertEqual(cuenta3.getBancoVirtual(), None)

        cuenta4 = CuentaVirtual(1111, 12345, Usuario())

        self.assertEqual(cuenta4.getSaldo(), 1111)
        self.assertEqual(cuenta4.getId(), 12345)
        self.assertEqual(cuenta4.getUsuario() is not None, True)
        self.assertEqual(cuenta4.getContraseña(), "")
        self.assertEqual(cuenta4.getBancoVirtual(), None)

        cuenta5 = CuentaVirtual(1789, 123456, Usuario(), "1217")

        self.assertEqual(cuenta5.getSaldo(), 1789)
        self.assertEqual(cuenta5.getId(), 123456)
        self.assertEqual(cuenta5.getUsuario() is not None, True)
        self.assertEqual(cuenta5.getContraseña(), "1217")
        self.assertEqual(cuenta5.getBancoVirtual(), None)

        cuenta6 = CuentaVirtual(20000, 321, Usuario(), "1712", TesteosCuentaVirtual.bancoVirtual1)

        self.assertEqual(cuenta6.getSaldo(), 20000)
        self.assertEqual(cuenta6.getId(), 321)
        self.assertEqual(cuenta6.getUsuario() is not None, True)
        self.assertEqual(cuenta6.getContraseña(), "1712")
        self.assertEqual(cuenta6.getBancoVirtual(), TesteosCuentaVirtual.bancoVirtual1)

    def testCuentasDisponibles(self):

        #Testeamos que las instancias se añadan correctamente a el banco virtual
         
        TesteosCuentaVirtual.bancoVirtual1.getCuentasCreadas().clear()

        self.assertEqual(len(TesteosCuentaVirtual.bancoVirtual1.getCuentasCreadas()), 0)

        for i in range(20):
            CuentaVirtual(
            (i**5) + 999,
             int(f'{i+1}{i+2}{i+3}'), 
             Usuario(), 
             f'{i+3}{i+2}{i+1}{i}', 
             TesteosCuentaVirtual.bancoVirtual1
             )

        
        self.assertEqual(len(TesteosCuentaVirtual.bancoVirtual1.getCuentasCreadas()), 20)
    
    def testCrearId(self):

        idParaCuenta = CuentaVirtual.crearId(TesteosCuentaVirtual.bancoVirtual1)

        self.assertIn('ID-', idParaCuenta)
        self.assertIn(str(len(TesteosCuentaVirtual.bancoVirtual1.getCuentasCreadas())), idParaCuenta)

    def testStr(self):

        TesteosCuentaVirtual.bancoVirtual1.getCuentasCreadas().clear()

        cuentaStr = CuentaVirtual(12000.0, 
                    CuentaVirtual.crearId(TesteosCuentaVirtual.bancoVirtual1), 
                    Usuario(nombre="Oscar"), 
                    "1234", 
                    TesteosCuentaVirtual.bancoVirtual1)

        mensaje = cuentaStr.__str__()

        self.assertEqual(mensaje, f"\n-----Cuenta Virtual-----\n    Usuario: Oscar\n    Saldo: 12000.0\n    ID: ID-0\n")

if __name__ == "__main__":
    unittest.main()