import unittest

#Solucionamos problemas con las importaciones
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clases.bancoVirtual import BancoVirtual
from clases.servicio import Servicio
from clases.cuentaVirtual import CuentaVirtual
from clases.usuario import Usuario

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

        #Construimos los objetos usuarios
        usuario1 = Usuario(
            nombre = "Carlos", 
            edad = 24, 
            numeroCelular = 3011278978, 
            bancoVirtual = bancoVirtual1
        )

        usuario2 = Usuario(
            nombre = "Pepito", 
            edad = 99, 
            numeroCelular = 301123654, 
            bancoVirtual = bancoVirtual1
        )

        usuario3 = Usuario(
            nombre = "Isabella", 
            edad = 30, 
            numeroCelular = 3011235245, 
            bancoVirtual = bancoVirtual1
        )
        
        #Construimos los objetos cuentaVirtual
        cuentaVirtual1 = CuentaVirtual(
            usuario = usuario1,
            id = CuentaVirtual.crearId(bancoVirtual1),
            contraseña = '12345678',
            bancoVirtual = bancoVirtual1
        )

        cuentaVirtual2 = CuentaVirtual(
            usuario = usuario2,
            id = CuentaVirtual.crearId(bancoVirtual1),
            contraseña = 'contraseña',
            bancoVirtual = bancoVirtual1
        )

        cuentaVirtual3 = CuentaVirtual(
            usuario = usuario3,
            id = CuentaVirtual.crearId(bancoVirtual1),
            contraseña = 'nadieLaDescifrara',
            bancoVirtual = bancoVirtual1
        )

        #Le asignamos al cliente su respectiva cuenta
        usuario1.setCuenta(cuentaVirtual1)
        usuario2.setCuenta(cuentaVirtual2)
        usuario3.setCuenta(cuentaVirtual3)

        #Consultamos que se añaden efectivamente
        self.assertEqual(len(bancoVirtual1.getClientesAsociados()), 3)
        self.assertEqual(len(bancoVirtual1.getCuentasCreadas()), 3)
        self.assertEqual(len(bancoVirtual1.getServiciosDisponibles()), 3)

    def testBuscarClientePorNumeroDeCelular(self):

        bancoVirtual1 = BancoVirtual()

        usuario4 = Usuario(
            nombre = 'Alberto',
            numeroCelular = 3914504312,
            edad = 18,
            bancoVirtual = bancoVirtual1
        )

        clienteEncontrado1 = bancoVirtual1.buscarClientePorNumeroDeCelular(3914504312)

        self.assertIs(clienteEncontrado1, usuario4)

        clienteEncontrado2 = bancoVirtual1.buscarClientePorNumeroDeCelular(39145043129)

        self.assertEqual(clienteEncontrado2, None)
    
    def testFiltrarTiposDeServicios(self):

        bancoVirtual1 = BancoVirtual()

        tiposDeServiciosDisponibles = bancoVirtual1.filtrarTiposDeServiciosDisponibles()
        self.assertEqual(len(tiposDeServiciosDisponibles), 0)

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

        #1 servicio de un tipo
        tiposDeServiciosDisponibles = bancoVirtual1.filtrarTiposDeServiciosDisponibles()
        self.assertEqual(len(tiposDeServiciosDisponibles), 1)
        self.assertIn('Telefonía', tiposDeServiciosDisponibles)

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

        #Dos servicios del mismo tipo
        tiposDeServiciosDisponibles = bancoVirtual1.filtrarTiposDeServiciosDisponibles()
        self.assertEqual(len(tiposDeServiciosDisponibles), 1)
        self.assertIn('Telefonía', tiposDeServiciosDisponibles)

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

        #3 servicios, dos del mismo tipo y uno de otro
        tiposDeServiciosDisponibles = bancoVirtual1.filtrarTiposDeServiciosDisponibles()
        self.assertEqual(len(tiposDeServiciosDisponibles), 2)
        self.assertIn('Telefonía', tiposDeServiciosDisponibles)
        self.assertIn('Hogar', tiposDeServiciosDisponibles)

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

        #6 Servicios dos de cada tipo
        tiposDeServiciosDisponibles = bancoVirtual1.filtrarTiposDeServiciosDisponibles()
        self.assertEqual(len(tiposDeServiciosDisponibles), 3)
        self.assertIn('Streaming', tiposDeServiciosDisponibles)
        self.assertIn('Hogar', tiposDeServiciosDisponibles)
        self.assertIn('Telefonía', tiposDeServiciosDisponibles)
    
    def testFiltrarServiciosPorTipo(self):

        bancoVirtual1 = BancoVirtual()

        tiposDeServiciosDisponibles = bancoVirtual1.filtrarServiciosPorTipo('Telefonía')
        self.assertEqual(len(tiposDeServiciosDisponibles), 0)

        tiposDeServiciosDisponibles = bancoVirtual1.filtrarServiciosPorTipo('Hogar')
        self.assertEqual(len(tiposDeServiciosDisponibles), 0)

        tiposDeServiciosDisponibles = bancoVirtual1.filtrarServiciosPorTipo('Streaming')
        self.assertEqual(len(tiposDeServiciosDisponibles), 0)

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

        tiposDeServiciosDisponibles = bancoVirtual1.filtrarServiciosPorTipo('Telefonía')
        self.assertEqual(len(tiposDeServiciosDisponibles), 1)

        tiposDeServiciosDisponibles = bancoVirtual1.filtrarServiciosPorTipo('Hogar')
        self.assertEqual(len(tiposDeServiciosDisponibles), 0)

        tiposDeServiciosDisponibles = bancoVirtual1.filtrarServiciosPorTipo('Streaming')
        self.assertEqual(len(tiposDeServiciosDisponibles), 0)

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
            'WOM', 
            'Telefonía', 
            {
            'Datos: 100GB, Llamadas ilimitadas, Whatsapp ilimitado' : 58900,
            'Datos: 50GB, Llamadas ilimitadas' : 45600,
            'Datos: 30GB': 24000
            },
            bancoVirtual1
        )

        tiposDeServiciosDisponibles = bancoVirtual1.filtrarServiciosPorTipo('Telefonía')
        self.assertEqual(len(tiposDeServiciosDisponibles), 2)

        tiposDeServiciosDisponibles = bancoVirtual1.filtrarServiciosPorTipo('Hogar')
        self.assertEqual(len(tiposDeServiciosDisponibles), 1)

        tiposDeServiciosDisponibles = bancoVirtual1.filtrarServiciosPorTipo('Streaming')
        self.assertEqual(len(tiposDeServiciosDisponibles), 0)

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
            'WOM', 
            'Telefonía', 
            {
            'Datos: 100GB, Llamadas ilimitadas, Whatsapp ilimitado' : 58900,
            'Datos: 50GB, Llamadas ilimitadas' : 45600,
            'Datos: 30GB': 24000
            },
            bancoVirtual1
        )

        tiposDeServiciosDisponibles = bancoVirtual1.filtrarServiciosPorTipo('Telefonía')
        self.assertEqual(len(tiposDeServiciosDisponibles), 3)

        tiposDeServiciosDisponibles = bancoVirtual1.filtrarServiciosPorTipo('Hogar')
        self.assertEqual(len(tiposDeServiciosDisponibles), 2)

        tiposDeServiciosDisponibles = bancoVirtual1.filtrarServiciosPorTipo('Streaming')
        self.assertEqual(len(tiposDeServiciosDisponibles), 1)

if __name__ == '__main__':
    unittest.main()

        

