def obtener_entrada(mensaje):
    while True:
        try:
            entrada = input(mensaje)
            return entrada
        except KeyboardInterrupt:
            exit()
        except Exception as e:
            print(f"Error: {e}")