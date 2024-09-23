"""
Integrantes: 
• Juan José Gonzalez Morales, C.C. 1013458547
• Edinson Andres Ariza Mendoza, C.C. 1099737114

Aplicación: 

La aplicacion implementada es sobre un banco virtual como por ejemplo nequi, en donde el usuario podra acceder
a las siguientes funcionalidades:

• Inicio de sesion y creación de una nueva cuenta: En esta funcionalidad el usuario podra iniciar sesion en su
cuenta existente o crear una nueva cuenta a su nombre con su numero de telefono y una contraseña de 4 digitos numericos. 
(Para esto se usan las clases CuentaVirtual y Usuario ubicadas en sus respectivos módulos)

• Consignación, retiro y envio de dinero: Cada usuario creado tendra una cuenta virtual asociada a la cual podrá
consignar, retirar y enviar dinero a otro a usuario unicamente a otro usuario que este registrado en el banco 
virtual de la aplicacion. (Para esto se usan las clases BancoVirtual, CuentaVirtual, Usuario ubicadas en sus 
respectivos módulos).

• Pago de servicios: En esta funcionalidad, según los servicios con los que tengamos algún convenio, el usuario
podrá realizar el pago de planes mensuales asociados al servicio

Requisitos del sistema:

Para el correcto funcionamiento de la aplicacion es necesaria la previa creacion de una instancia de BancoVirtual
y las respectivas instancias de los servicios que se necesitan.

Nota: Se recomienda ejecutar la palicacion con la consola grande.

"""

#Solucionamos problemas con las importaciones
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clases.bancoVirtual import BancoVirtual
from clases.servicio import Servicio
from clases.cuentaVirtual import CuentaVirtual
from clases.usuario import Usuario


def mostrarOpcionesAplicacion(usuario):

    #booleano = True
    
    print(usuario.getCuenta().__str__())

    while True:

        opciones = ["Retirar dinero", "Consignar dinero", "Enviar dinero", "Pagar o adquirir servicios", "Cerrar Sesión"]
        print("¿Que deseas realizar?\n ")

        for i in range(1,6):
            print(f'{i}. {opciones[i-1]}')

        eleccionUsuario = 0

        try:
            eleccionUsuario = int(input("\nOpcion numero: "))
            if eleccionUsuario == 1:
                retirarDinero(usuario)
            elif eleccionUsuario == 2:
                pass
            elif eleccionUsuario == 3:
                pass
            elif eleccionUsuario == 4:
                pass
            elif eleccionUsuario == 5:
                cerrarSesion()
            else: 
                print("\nOpcion no valida, intente de nuevo\n")
        except ValueError:
            print("\nError: Debes ingresar un número válido.\n")

        


def retirarDinero(user):

    print(user.getCuenta().__str__())
    print(user.getCuenta().retirar(int(input("Digite el valor a retirar: "))))
    print(user.getCuenta().__str__())


def cerrarSesion():
    print("\nSesion Cerrada, Vuelva pronto\n")
    sys.exit()


banco = BancoVirtual()
user =  Usuario(cuenta= CuentaVirtual(saldo= 12, usuario= None, id = CuentaVirtual.crearId(banco), contraseña= 1234, bancoVirtual= banco), nombre="Oscar")
user.getCuenta().setUsuario(user)
mostrarOpcionesAplicacion(user)