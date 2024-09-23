import unittest

#Solucionamos las importaciones
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clases.servicio import Servicio

class serviciosTest(unittest.TestCase):

    def testCrearServicio(self):

        #Creamos un servicio por cada tipo de servicio que tendrá nuestro programa

        servicioStreaming = Servicio('Netflix', 'Streaming', {
            '1 Pantalla' : 16900,
            '2 Pantallas' : 26900,
            '4 Pantallas' : 36900
        })

        self.assertEqual(servicioStreaming.getNombre(), 'Netflix')
        self.assertEqual(servicioStreaming.getTipo(), 'Streaming')
        self.assertEqual(servicioStreaming.getPlanesMensuales()['1 Pantalla'], 16900)
        self.assertEqual(servicioStreaming.getPlanesMensuales()['2 Pantallas'], 26900)
        self.assertEqual(servicioStreaming.getPlanesMensuales()['4 Pantallas'], 36900)

        servicioHogar = Servicio('Movistar', 'Hogar', {
            'Wifi: 300MB, Canales: 200, Llamadas ilimitadas' : 128000,
            'Wifi: 200MB, Canales: 100, Llamadas: 1080 Minutos' : 64000,
            'Wifi: 100MB, Llamadas: 640 Minutos' : 51000
        })

        self.assertEqual(servicioHogar.getNombre(), 'Movistar')
        self.assertEqual(servicioHogar.getTipo(), 'Hogar')
        self.assertEqual(servicioHogar.getPlanesMensuales()['Wifi: 300MB, Canales: 200, Llamadas ilimitadas'], 128000)
        self.assertEqual(servicioHogar.getPlanesMensuales()['Wifi: 200MB, Canales: 100, Llamadas: 1080 Minutos'], 64000)
        self.assertEqual(servicioHogar.getPlanesMensuales()['Wifi: 100MB, Llamadas: 640 Minutos'], 51000)

        servicioTelefonia = Servicio('WOM', 'Telefonía', {
            'Datos: 100GB, Llamadas ilimitadas, Whatsapp ilimitado' : 58900,
            'Datos: 50GB, Llamadas ilimitadas' : 45600,
            'Datos: 30GB': 24000
        })

        self.assertEqual(servicioTelefonia.getNombre(), 'WOM')
        self.assertEqual(servicioTelefonia.getTipo(), 'Telefonía')
        self.assertEqual(servicioTelefonia.getPlanesMensuales()['Datos: 100GB, Llamadas ilimitadas, Whatsapp ilimitado'], 58900)
        self.assertEqual(servicioTelefonia.getPlanesMensuales()['Datos: 50GB, Llamadas ilimitadas'], 45600)
        self.assertEqual(servicioTelefonia.getPlanesMensuales()['Datos: 30GB'], 24000)
    
    def testServiciosDisponibles(self):

        Servicio.getServiciosDisponibles().clear()

        self.assertEqual(len(Servicio.getServiciosDisponibles()), 0)

        Servicio('WOM', 'Telefonía', {
            'Datos: 100GB, Llamadas ilimitadas, Whatsapp ilimitado' : 58900,
            'Datos: 50GB, Llamadas ilimitadas' : 45600,
            'Datos: 30GB': 24000
        })

        Servicio('Movistar', 'Hogar', {
            'Wifi: 300MB, Canales: 200, Llamadas ilimitadas' : 128000,
            'Wifi: 200MB, Canales: 100, Llamadas: 1080 Minutos' : 64000,
            'Wifi: 100MB, Llamadas: 640 Minutos' : 51000
        })

        Servicio('Netflix', 'Streaming', {
            '1 Pantalla' : 16900,
            '2 Pantallas' : 26900,
            '4 Pantallas' : 36900
        })

        self.assertEqual(len(Servicio.getServiciosDisponibles()), 3)

if __name__ == '__main__':
    unittest.main()



