habitaciones = {}

def agregar_habitaciones():
    from Funciones import solucion_error
    habitacion = solucion_error.obtener_entrada("Ingrese identificador de la habitación: ")
    habitaciones[habitacion]='Libre'
    print("Habitación agregada correctamente.")

def mostrar_habitaciones():
    print("Lista de habitaciones:")
    for identificador, estado in habitaciones.items():
        print(f"Identificador: {identificador}, Estado: {estado}")

def habitacion_disponible(habitacion):
    habitaciones[habitacion]='Libre'
    print("Habitación marcada como disponible.")