import unittest

#Solucionamos problemas con las importaciones
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clases.bancoVirtual import BancoVirtual
from clases.servicio import Servicio

class bancoVirtualTest(unittest.TestCase):
    
    def testCrearBancoVirtual(self):

        bancoVirtual1 = BancoVirtual()

        self.assertEqual(len(bancoVirtual1.getClientesAsociados()), 0)
        self.assertEqual(len(bancoVirtual1.getCuentasCreadas()), 0)
        self.assertEqual(len(bancoVirtual1.getServiciosDisponibles()), 0)

        #Creamos los objetos de servicio
        Servicio(
            'WOM', 
            'Telefonía', 
            {
            'Datos: 100GB, Llamadas ilimitadas, Whatsapp ilimitado' : 58900,
            'Datos: 50GB, Llamadas ilimitadas' : 45600,
            'Datos: 30GB': 24000
            },
            bancoVirtual1
        )

        Servicio(
            'Movistar', 
            'Hogar', 
            {
            'Wifi: 300MB, Canales: 200, Llamadas ilimitadas' : 128000,
            'Wifi: 200MB, Canales: 100, Llamadas: 1080 Minutos' : 64000,
            'Wifi: 100MB, Llamadas: 640 Minutos' : 51000
            },
            bancoVirtual1
        )

        Servicio(
            'Netflix', 
            'Streaming', 
            {
            '1 Pantalla' : 16900,
            '2 Pantallas' : 26900,
            '4 Pantallas' : 36900
            },
            bancoVirtual1
        )

        #Construimos los objetos cuenta

        #Construimos los objetos cliente

        #Consultamos que se añaden efectivamente
        #self.assertEqual(len(bancoVirtual1.getClientesAsociados()), 3)
        #self.assertEqual(len(bancoVirtual1.getCuentasCreadas()), 3)
        self.assertEqual(len(bancoVirtual1.getServiciosDisponibles()), 3)

if __name__ == '__main__':
    unittest.main()

        

