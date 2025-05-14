from Funciones import datos_registro, solucion_error, habitaciones_registro

registro = datos_registro.RegistroClientes()

while True:
    print("\n1. Registrar nuevo cliente")
    print("2. Mostrar clientes registrados")
    print("3. Agregar habitaciones")
    print("4. Consultar habitaciones")
    print("5. Marcar como disponible")
    print("6. Salir")

    opcion = solucion_error.obtener_entrada("Selecciona una opción (1/2/3/4/5): ")

    if opcion == '1':
        nombre = solucion_error.obtener_entrada("Ingrese el nombre del cliente: ")
        apellido = solucion_error.obtener_entrada("Ingrese el apellido del cliente: ")
        dni = solucion_error.obtener_entrada("Ingrese el DNI del cliente: ")
        habitacion = solucion_error.obtener_entrada("Ingrese la habitacion del cliente: ")

        if habitacion in habitaciones_registro.habitaciones:
            if habitaciones_registro.habitaciones[habitacion] == 'Libre':
                habitaciones_registro.habitaciones[habitacion] = 'Ocupado'
                registro.registrar_cliente(nombre, apellido, dni, habitacion)
                print("Cliente registrado correctamente.")
            else:
                print("La habitación está ocupada. Elige otra habitación.")
        else:
            print("La habitación no existe. Registra la habitación antes de asignarla a un cliente.")

    elif opcion == '2':
        registro.mostrar_clientes()

    elif opcion == '3':
        habitaciones_registro.agregar_habitaciones()

    elif opcion == '4':
        habitaciones_registro.mostrar_habitaciones()

    elif opcion == '5':
        habitacion = solucion_error.obtener_entrada("Ingrese identificador de habitación: ")
        habitaciones_registro.habitacion_disponible(habitacion)

    elif opcion == '6':
        break

    else:
        print("Opción no válida.")