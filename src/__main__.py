
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

        print(f'\nEl dato ingresado es: {datoIngresadoPorUsuario}, ¿Desea Continuar?')

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
       
    while(True):
        print('\nRecordatorio: La edad mínima de registro es de 12 años')
        edadCliente = ingresarCualquierDatoNumerico('\nDigite su edad: ')

        if edadCliente >= 12 and edadCliente <= 100:
            break
        elif edadCliente > 100:
            print('Digite un valor real que sea acorde a su edad (Menor a 100 años)')
        else:
            print('La edad mínima para registarse es de 12 años')

    while(True):
        print('\nRecordatorio: La clave es un número de 4 digitos')
        contraseñaCuentaVirtual = str(ingresarCualquierDatoNumerico('\nDigite la clave para su cuenta: '))
        if len(str(contraseñaCuentaVirtual)) == 4: 
            break
        else:
            print('Error, la contraseña debe ser de 4 digitos')

    
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
        bancoVirtual = bancoVirtual,
        id = CuentaVirtual.crearId(bancoVirtual)
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
        contraseñaCuentaVirtual = 0

        try:
            numeroDeCelular = int(input('Digite su número telefónico: '))

        except ValueError:
            print('Debes ingresar un dato numérico')
            continue

        while(True):
            print('\nRecordatorio: La clave es un número de 4 digitos')
            contraseñaCuentaVirtual = str(ingresarCualquierDatoNumerico('\nDigite la clave para su cuenta: '))
            if len(str(contraseñaCuentaVirtual)) == 4: 
                break
            else:
                print('Error, la contraseña debe ser de 4 digitos')

        clienteProceso = bancoVirtual.buscarClientePorNumeroDeCelular(numeroDeCelular)

        if clienteProceso is None:

            print('\nNo hemos encontrado un cliente asociado a este número telefónico')

            eleccionUsuario = eleccionBinaria('Volver a intentar', 'Regresar al menú de ingreso')
            
            if eleccionUsuario == 1:
                continue
            elif eleccionUsuario == 2:
                break

        else: 
            
            if clienteProceso.getCuenta().getContraseña() == contraseñaCuentaVirtual:
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
                consignarDinero(usuario)
            elif eleccionUsuario == 3:
                enviarDinero(usuario)
            elif eleccionUsuario == 4:
                adquirirServicio(usuario)
            elif eleccionUsuario == 5:
                cerrarSesion()
            else: 
                print("\nOpcion no valida, intente de nuevo\n")
        except ValueError:
            print("\nError: Debes ingresar un número válido.\n")

def retirarDinero(user):

    print(user.getCuenta().__str__())
    print(user.getCuenta().retirar(int(input("Digite el valor a retirar: "))))
    print("")
    print(user.getCuenta().__str__())

def consignarDinero(user):
    print(user.getCuenta().__str__())
    print(user.getCuenta().consignar(int(input("Digite el valor a consignar: "))))
    print("")
    print(user.getCuenta().__str__())

def enviarDinero(user):

    print(user.getCuenta().__str__())
    constraseña = input("\nIngrese la contraseña de su cuenta: ")
    destinatario = int(input("Ingrese el numero de cuenta del destinatario: "))
    valor = int(input("Digite el valor a enviar: "))
    print("")   
    print(user.getCuenta().enviarDinero(constraseña, destinatario, valor))
    print(user.getCuenta().__str__())

def adquirirServicio(usuario):

    eleccionUsuario = 0
    servicioProceso = None
    tipoDeServicioSeleccionado = ''
    pagoRealizado = False
    
    print('Bienvenido al sistema de pago o adquisición de serivicios\n')

    tiposDeServicio = usuario.getBancoVirtual().filtrarTiposDeServiciosDisponibles()

    tiposDeServiciosEnumerados = [f'{index + 1}. {tipoDeServicio}' for index, tipoDeServicio in enumerate(tiposDeServicio)]

    mostrarTiposDeServicio = '\n'.join(tiposDeServiciosEnumerados)

    while(True):
        print('Seleccione uno de los tipos de servicios disponibles\n')

        print(mostrarTiposDeServicio)

        try:
            eleccionUsuario = int(input('\nDigite un único valor numérico entre los disponibles: '))
        except ValueError:
            print('Error, debe ingresar un dato numérico entre los disponibles')
            continue

        if eleccionUsuario > 0 and eleccionUsuario <= len(tiposDeServicio):
            tipoDeServicioSeleccionado = tiposDeServicio[eleccionUsuario - 1]

            print(f'\nEl tipo de servicio seleccionado es: {tipoDeServicioSeleccionado}, ¿Desea continuar?')

            eleccionUsuario = eleccionBinaria('SI', 'NO')

            if eleccionUsuario == 1:
                break
    
    serviciosPorTipo = bancoVirtual.filtrarServiciosPorTipo(tipoDeServicioSeleccionado)

    serviciosPorTipoEnumerados = [f'{i + 1}. {servicio.getNombre()}' for i, servicio in enumerate(serviciosPorTipo)]

    mostrarServiciosPorTipo = '\n'.join(serviciosPorTipoEnumerados)

    while(True):

        print('\nSeleccione uno de los servicios disponibles\n')
        print(mostrarServiciosPorTipo)

        try:
            eleccionUsuario = int(input('\nDigite un único valor numérico entre los disponibles: '))
        except ValueError:
            print('Error, debe ingresar un dato numérico entre los disponibles')
            continue
        
        if eleccionUsuario > 0 and eleccionUsuario <= len(serviciosPorTipo):
            
            servicioProceso = serviciosPorTipo[eleccionUsuario - 1]

            print(f'\nEl servicio seleccionado es: {servicioProceso.getNombre()}, ¿Desea continuar?')

            eleccionUsuario = eleccionBinaria('SI', 'NO')

            if eleccionUsuario == 1:
                break

    listaPlanesMensuales = list(servicioProceso.getPlanesMensuales().keys())
    
    while(True):

        print('Seleccione uno de los planes mensuales disponibles\n')
        print(str(servicioProceso))

        try:
            eleccionUsuario = int(input('\nDigite un único valor numérico entre los disponibles: '))
        except ValueError:
            print('Error, debe ingresar un dato numérico entre los disponibles')
            continue
        
        if eleccionUsuario > 0 and eleccionUsuario <= len(listaPlanesMensuales):
            
            planSeleccionado = listaPlanesMensuales[eleccionUsuario - 1]

            print(f'\nEl plan mensual seleccionado es: {planSeleccionado}, ¿Desea continuar?')

            eleccionUsuario = eleccionBinaria('SI', 'NO')

            if eleccionUsuario == 1:
                pagoRealizado = True if 'exitosamente' in usuario.getCuenta().retirar(servicioProceso.getPlanesMensuales()[planSeleccionado]) else False
                break
    
    if pagoRealizado:
        print('El pago del servicio se ha realizado de forma exitosa\nRedireccinando al menú principal...\n')
    else:
        print('No se ha podido realizar el pago, debido a que no tienes saldo suficiente\nTe invitamos amablemente a recargar tu tarjeta\nRedireccionando al menú principal...\n')

def cerrarSesion():
    print("\nSesion Cerrada, Vuelva pronto\n")
    sys.exit()

def requisitosDeSistema(bancoVirtual):
    Servicio(
            'Netflix', 
            'Streaming', 
            {
            '1 Pantalla' : 16900,
            '2 Pantallas' : 26900,
            '4 Pantallas' : 36900
            },
            bancoVirtual
        )
    Servicio(
            'Crunchyroll', 
            'Streaming', 
            {
            '1 Pantalla' : 13900,
            '2 Pantallas' : 22900,
            '4 Pantallas' : 33900
            },
            bancoVirtual
        )
    Servicio(
            'Disney+', 
            'Streaming', 
            {
            '1 Pantalla' : 19900,
            '2 Pantallas' : 28900,
            '4 Pantallas' : 39900
            },
            bancoVirtual
        )
    
    Servicio(
            'Movistar', 
            'Hogar', 
            {
            'Wifi: 300MB, Canales: 200, Llamadas ilimitadas' : 128000,
            'Wifi: 200MB, Canales: 100, Llamadas: 1080 Minutos' : 64000,
            'Wifi: 100MB, Llamadas: 640 Minutos' : 51000
            },
            bancoVirtual
        )
    Servicio(
            'DirectTv', 
            'Hogar', 
            {
            'Wifi: 400MB, Canales: 250, Llamadas ilimitadas' : 118000,
            'Wifi: 250MB, Canales: 100, Llamadas: 1080 Minutos' : 74000,
            'Wifi: 100MB, Llamadas: 640 Minutos' : 49000
            },
            bancoVirtual
        )
    Servicio(
            'Claro', 
            'Hogar', 
            {
            'Wifi: 250MB, Canales: 150, Llamadas ilimitadas' : 138000,
            'Wifi: 1500MB, Canales: 100, Llamadas: 1080 Minutos' : 84000,
            'Wifi: 80MB, Llamadas: 640 Minutos' : 47000
            },
            bancoVirtual
        )
    
    Servicio(
            'WOM', 
            'Telefonía', 
            {
            'Datos: 100GB, Llamadas ilimitadas, Whatsapp ilimitado' : 58900,
            'Datos: 50GB, Llamadas ilimitadas' : 45600,
            'Datos: 30GB': 24000
            },
            bancoVirtual
        )
    Servicio(
            'Movistar', 
            'Telefonía', 
            {
            'Datos: 150GB, Llamadas ilimitadas, Whatsapp ilimitado' : 60900,
            'Datos: 70GB, Llamadas ilimitadas' : 47600,
            'Datos: 25GB': 23900
            },
            bancoVirtual
        )
    Servicio(
            'Tigo', 
            'Telefonía', 
            {
            'Datos: 90GB, Llamadas ilimitadas, Whatsapp ilimitado' : 59900,
            'Datos: 60GB, Llamadas ilimitadas' : 44600,
            'Datos: 20GB': 18000
            },
            bancoVirtual
        )
    
    #Crear usuario para el profe
    clientePrueba =  Usuario(cuenta= CuentaVirtual(saldo= 100000, usuario= None, id = CuentaVirtual.crearId(bancoVirtual), contraseña= "1234", bancoVirtual= bancoVirtual), nombre="Oscar", bancoVirtual = bancoVirtual, numeroCelular=123456789, edad = 18)
    clientePrueba.getCuenta().setUsuario(clientePrueba)

bancoVirtual = BancoVirtual()
requisitosDeSistema(bancoVirtual)

clienteProceso = ingresoBancoVirtual(bancoVirtual)

mostrarOpcionesAplicacion(clienteProceso)
