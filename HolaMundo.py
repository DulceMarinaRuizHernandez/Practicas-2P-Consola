class Mensaje:
    def __init__(self, mensaje):
        self.mensaje = mensaje
    def mostrar_mensaje(self):
        print("Hola Mundo")

        
if __name__ == "__main__":
    mensaje = Mensaje("Programacion en clase")
    mensaje.mostrar_mensaje()