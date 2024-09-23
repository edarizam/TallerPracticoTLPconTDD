import unittest
import sys

import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clases.usuario import Usuario
from clases.cuentaVirtual import CuentaVirtual
from clases.bancoVirtual import BancoVirtual

class TesteosUsuario(unittest.TestCase):

    bancoVirtual1 = BancoVirtual()

    def testCrearUsuario(self):

        #Testeamos diferentes formas de crear un usuario

        usuario1 = Usuario()

        self.assertEqual(usuario1.getCuenta(), None)
        self.assertEqual(usuario1.getNombre(), "")
        self.assertEqual(usuario1.getEdad(), 0)
        self.assertEqual(usuario1.getNumeroCelular(), 0)
        self.assertEqual(usuario1.getBancoVirtual(), None)

        usuario2 = Usuario(CuentaVirtual())

        self.assertEqual(usuario2.getCuenta() is not None, True)
        self.assertEqual(usuario2.getNombre(), "")
        self.assertEqual(usuario2.getEdad(), 0)
        self.assertEqual(usuario2.getNumeroCelular(), 0)
        self.assertEqual(usuario2.getBancoVirtual(), None)

        usuario3 = Usuario(CuentaVirtual(), "Oscar")

        self.assertEqual(usuario3.getCuenta() is not None, True)
        self.assertEqual(usuario3.getNombre(), "Oscar")
        self.assertEqual(usuario3.getEdad(), 0)
        self.assertEqual(usuario3.getNumeroCelular(), 0)
        self.assertEqual(usuario3.getBancoVirtual(), None)

        usuario4 = Usuario(CuentaVirtual(), "Juan José", 18)

        self.assertEqual(usuario4.getCuenta() is not None, True)
        self.assertEqual(usuario4.getNombre(), "Juan José")
        self.assertEqual(usuario4.getEdad(), 18)
        self.assertEqual(usuario4.getNumeroCelular(), 0)
        self.assertEqual(usuario4.getBancoVirtual(), None)

        usuario5 = Usuario(CuentaVirtual(), "Edinson", 19, 301698456)

        self.assertEqual(usuario5.getCuenta() is not None, True)
        self.assertEqual(usuario5.getNombre(), "Edinson")
        self.assertEqual(usuario5.getEdad(), 19)
        self.assertEqual(usuario5.getNumeroCelular(), 301698456)
        self.assertEqual(usuario5.getBancoVirtual(), None)

        usuario6 = Usuario(CuentaVirtual(), "Pepito", 99, 301123654, TesteosUsuario.bancoVirtual1)

        self.assertEqual(usuario6.getCuenta() is not None, True)
        self.assertEqual(usuario6.getNombre(), "Pepito")
        self.assertEqual(usuario6.getEdad(), 99)
        self.assertEqual(usuario6.getNumeroCelular(), 301123654)
        self.assertEqual(usuario6.getBancoVirtual() is None, False)

    def testUsuariosAsociados(self): 

        TesteosUsuario.bancoVirtual1.getClientesAsociados().clear() 

        self.assertEqual(len(TesteosUsuario.bancoVirtual1.getClientesAsociados()), 0)

        for i in range(10):
            Usuario(bancoVirtual= TesteosUsuario.bancoVirtual1)

        self.assertEqual(len(TesteosUsuario.bancoVirtual1.getClientesAsociados()), 10)







if __name__ == "__main__":
    unittest.main()

