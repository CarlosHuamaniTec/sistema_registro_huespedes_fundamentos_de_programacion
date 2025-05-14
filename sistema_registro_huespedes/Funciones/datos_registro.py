class RegistroClientes:
    def __init__(self):
        self.clientes = []

    def registrar_cliente(self, nombre, apellido, dni, habitacion):
        import datetime
        fecha = str(datetime.datetime.now())
        cliente = {'Nombre': nombre, 'Apellido': apellido, 'DNI': dni, 'Habitación': habitacion, 'Fecha': fecha}
        self.clientes.append(cliente)

    def mostrar_clientes(self):
        print("Lista de clientes registrados:")
        for cliente in self.clientes:
            print(f"Nombre: {cliente['Nombre']}, Apellido: {cliente['Apellido']}, DNI: {cliente['DNI']}, Habitación: {cliente['Habitación']}, Fecha: {cliente['Fecha']}")