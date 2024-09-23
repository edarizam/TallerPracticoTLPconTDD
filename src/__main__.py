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

"""
#Solucionamos problemas con las importaciones
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clases.bancoVirtual import BancoVirtual
from clases.servicio import Servicio
from clases.cuentaVirtual import CuentaVirtual
from clases.usuario import Usuario

def eleccionBinaria(datoPara1, datoPara2):

    eleccionUsuario = 0

    while(True):
                
        print(f'\n1.{datoPara1}\n2.{datoPara2}\n')

        try:
            eleccionUsuario = int(input('Seleccione un valor numérico entre los disponibles: '))
        except ValueError:
            print('Debes ingresar un dato numérico entre los disponibles')
        
        if eleccionUsuario == 1 or eleccionUsuario == 2:
            break
        else:
            print('Debes ingresar un dato numérico entre los disponibles')
            continue
            
    return eleccionUsuario

def ingresarCualquierDatoNumerico(textoDatoASeleccionar):

    datoIngresadoPorUsuario = 0

    while(True):

        try:
            datoIngresadoPorUsuario = int(input(textoDatoASeleccionar))
        except ValueError:
            print('Error, debe ingresar un dato numérico')
            continue

        print(f'\nEl dato seleccionado es: {datoIngresadoPorUsuario}, ¿Desea Continuar?')

        eleccionUsuario = eleccionBinaria('SI', 'NO')

        if eleccionUsuario == 1:
            break
        else:
            continue
    
    return datoIngresadoPorUsuario

def registrarUsuario(bancoVirtual):
    
    clienteProceso = None
    nombreCliente = ''
    edadCliente = 0
    numeroDeCelularCliente = 0
    contraseñaCuentaVirtual = 0
    cuentaVirtualCliente = None

    #Pedimos los datos pertinentes para el registro
    print('\nRegistrarse\nA continuación solicitaremos los datos pertinentes para realizar un proceso de registro')

    while(True):
        
        nombreCliente = input('\nDigite su nombre: ')

        print(f'\nEl nombre seleccionado es: {nombreCliente}, ¿Desea Continuar?')

        eleccionUsuario = eleccionBinaria('SI', 'NO')

        if eleccionUsuario == 1:
            break
        else:
            continue
    
    while(True):
        numeroDeCelularCliente = ingresarCualquierDatoNumerico('\nDigite su número de celular: ')

        #Revisamos que el número de celular no se encuentra asociado a un cliente ya existente
        clienteExistente = bancoVirtual.buscarClientePorNumeroDeCelular(numeroDeCelularCliente)

        if clienteExistente is not None:
            print('\nHemos detectado que este número de teléfono ya se encuentra asociado a un cliente')

            eleccionUsuario = eleccionBinaria('Regresar al menú de ingreso', 'Ingresar de nuevo el número de celular')
            
            if eleccionUsuario == 1:
                clienteProceso = None
                break
            else:
                continue
        
        else: 
            break
       
    edadCliente = ingresarCualquierDatoNumerico('\nDigite su edad: ')

    while(True):
        print('\nRecordatorio: La clave es un número de 4 digitos')
        contraseñaCuentaVirtual = ingresarCualquierDatoNumerico('\nDigite la clave para su cuenta: ')
        if len(str(contraseñaCuentaVirtual)) == 4: 
            print('Error, la contraseña debe ser de 4 digitos')
            break

    
    #Creamos el cliente y le asociamos una cuenta
    clienteProceso = Usuario(
        nombre = nombreCliente,
        numeroCelular = numeroDeCelularCliente,
        edad = edadCliente,
        bancoVirtual = bancoVirtual 
    )

    cuentaVirtualCliente = CuentaVirtual(
        usuario = clienteProceso,
        contraseña = contraseñaCuentaVirtual,
        bancoVirtual = bancoVirtual
    )

    clienteProceso.setCuenta(cuentaVirtualCliente)

    print('¡Registro exitoso!')

    return clienteProceso

def iniciarSesion(bancoVirtual):
    
    eleccionUsuario = 0
    clienteProceso = None

    print('\nIniciar sesión\n')

    while(True):

        numeroDeCelular = 0
        contraseña = 0

        try:
            numeroDeCelular = int(input('Digite su número telefónico: '))

        except ValueError:
            print('Debes ingresar un dato numérico')
            continue

        while(True):
            print('\nRecordatorio: La clave es un número de 4 digitos')
            contraseñaCuentaVirtual = ingresarCualquierDatoNumerico('\nDigite la clave para su cuenta: ')
            if len(str(contraseñaCuentaVirtual)) == 4: 
                print('Error, la contraseña debe ser de 4 digitos')
                break

        clienteProceso = bancoVirtual.buscarClientePorNumeroDeCelular(numeroDeCelular)

        if clienteProceso is None:

            print('\nNo hemos encontrado un cliente asociado a este número telefónico')

            eleccionUsuario = eleccionBinaria('Volver a intentar', 'Regresar al menú de ingreso')
            
            if eleccionUsuario == 1:
                continue
            elif eleccionUsuario == 2:
                break

        else: 

            if clienteProceso.getCuentaVirtual().getContraseña() == contraseña:
                print('\nInicio de sesión exitoso\n')
                break

            else:
                print('Contraseña incorrecta')

                print('\nNo hemos encontrado un cliente asociado a este número telefónico')
            
                eleccionUsuario = eleccionBinaria('Volver a intentar', 'Regresar al menú de ingreso')
                
                if eleccionUsuario == 1:
                    continue
                elif eleccionUsuario == 2:
                    break
    
    return clienteProceso

def ingresoBancoVirtual(bancoVirtual):

    eleccionUsuario = 0
    clienteProceso = None

    #Seleccionar iniciar sesion o registrarse
    print('Bienvenido al banco virtual')

    while(True):
        print('\n1. Iniciar Sesión\n2. Registrarse\n')
        try:
            eleccionUsuario = int(input('Seleccione un valor numérico entre los disponibles: '))
        except ValueError:
            print('Error, debe seleccionar un dato numérico entre los disponibles')
            continue

        if eleccionUsuario == 1:
            clienteProceso = iniciarSesion(bancoVirtual)
        elif eleccionUsuario == 2:
            clienteProceso = registrarUsuario(bancoVirtual)
        else: 
            print('Error, debe ingresar un dato numérico entre los disponibles')
        
        if clienteProceso is not None:
            break
    
    return clienteProceso

bancoVirtual = BancoVirtual()
clienteProceso = ingresoBancoVirtual(bancoVirtual)


