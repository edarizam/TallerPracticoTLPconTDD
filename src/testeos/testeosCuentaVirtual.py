import unittest
import sys

import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clases.usuario import Usuario
from clases.cuentaVirtual import CuentaVirtual

class TesteosCuentaVirtual(unittest.TestCase):

    def testCrearCuentaVirtual(self):

        #Testeamos diferentes formas de crear una cuenta virtual

        cuenta1 = CuentaVirtual()

        self.assertEqual(cuenta1.getSaldo(), 0)
        self.assertEqual(cuenta1.getId(), 0)
        self.assertEqual(cuenta1.getUsuario(), None)
        self.assertEqual(cuenta1.getContraseña(), "")

        cuenta2 = CuentaVirtual(25000.0)

        self.assertEqual(cuenta2.getSaldo(), 25000.0)
        self.assertEqual(cuenta2.getId(), 0)
        self.assertEqual(cuenta2.getUsuario(), None)
        self.assertEqual(cuenta2.getContraseña(), "")

        cuenta3 = CuentaVirtual(1200, 976259)

        self.assertEqual(cuenta3.getSaldo(), 1200.0)
        self.assertEqual(cuenta3.getId(), 976259)
        self.assertEqual(cuenta3.getUsuario(), None)
        self.assertEqual(cuenta3.getContraseña(), "")

        cuenta4 = CuentaVirtual(1111, 12345, Usuario())

        self.assertEqual(cuenta4.getSaldo(), 1111)
        self.assertEqual(cuenta4.getId(), 12345)
        self.assertEqual(cuenta4.getUsuario() is not None, True)
        self.assertEqual(cuenta4.getContraseña(), "")

        cuenta5 = CuentaVirtual(1789, 123456, Usuario(), "1217")

        self.assertEqual(cuenta5.getSaldo(), 1789)
        self.assertEqual(cuenta5.getId(), 123456)
        self.assertEqual(cuenta5.getUsuario() is not None, True)
        self.assertEqual(cuenta5.getContraseña(), "1217")

    def test


if __name__ == "__main__":
    unittest.main()