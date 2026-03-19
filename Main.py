if __name__ == "__main__":
    from HolaMundo import Mensaje
    from OperacionesMatematicas import OperacionesMatematicas
    from Persona import Persona
    from FigurasGeometricas import FigurasGeometricas

    print("Este es el programa principal")
    print("Selecciona las opcion que deseas ejecutar")
    print("1. Hola Mundo")
    print("2. Operaciones Matematicas")
    print("3. Calcular la edad de una persona")
    print("4. Calcular area y perimetro de una figura geometrica")
    opcion = int(input("Ingrese la opcion: "))
    print(f"DEBUG: Opcion seleccionada = {opcion}, tipo = {type(opcion)}")

    if opcion == 1:
        print("DEBUG: Entrando a opcion 1")
        mensaje = Mensaje("Programacion en clase")
        mensaje.mostrar_mensaje()

    elif opcion == 2:
        print("DEBUG: Entrando a opcion 2")
        a = int(input("Ingrese el primer numero: "))
        b = int(input("Ingrese el segundo numero: "))
        operaciones = OperacionesMatematicas()
        print("Suma:", operaciones.sumar(a, b))
        print("Resta:", operaciones.restar(a, b))
        print("Multiplicacion:", operaciones.multiplicar(a, b))
        print("Division:", operaciones.dividir(a, b))

    elif opcion == 3:
        print("DEBUG: Entrando a opcion 3")
        Mostrar = "Ingrese su nombre y año de nacimiento para calcular su edad"
        print(Mostrar)
        Nombre = input("Ingrese su nombre: ")
        AnoNacimiento = int(input("Ingrese su año de nacimiento: "))
        AnoActual = int(input("Ingrese el año actual: "))

        print("Los datos ingresados son:")

        print("Nombre:", Nombre)
        print("Año de nacimiento:", AnoNacimiento)

        CalcularEdad = AnoActual - AnoNacimiento
        print("Edad:", CalcularEdad)

    elif opcion == 4:
        print("DEBUG: Entrando a opcion 4")
        print("Seleccione la figura geometrica:")
        print("1. Cuadrado")
        print("2. Rectangulo")
        print("3. Circulo")
        print("4. Triangulo")
        figura = int(input("Ingrese la opcion: "))
        if figura == 1:
            lado = float(input("Ingrese el lado del cuadrado: "))
            AreaCuadrado = lado ** 2
            PerimetroCuadrado = 4 * lado
            print("Area del cuadrado:", AreaCuadrado)
            print("Perimetro del cuadrado:", PerimetroCuadrado)
        elif figura == 2:
            base = float(input("Ingrese la base del rectangulo: "))
            altura = float(input("Ingrese la altura del rectangulo: "))
            AreaRectangulo = base * altura
            PerimetroRectangulo = 2 * (base + altura)
            print("Area del rectangulo:", AreaRectangulo)
            print("Perimetro del rectangulo:", PerimetroRectangulo)
        elif figura == 3:
            radio = float(input("Ingrese el radio del circulo: "))
            AreaCirculo = 3.14159 * radio ** 2
            PerimetroCirculo = 2 * 3.14159 * radio
            print("Area del circulo:", AreaCirculo)
            print("Perimetro del circulo:", PerimetroCirculo)
        elif figura == 4:
            base = float(input("Ingrese la base del triangulo: "))
            altura = float(input("Ingrese la altura del triangulo: "))
            AreaTriangulo = 0.5 * base * altura
            PerimetroTriangulo = base + altura + (base ** 2 + altura ** 2) ** 0.5
            print("Area del triangulo:", AreaTriangulo)
            print("Perimetro del triangulo:", PerimetroTriangulo)

        else:
             print("Opcion no valida")         




