class FigurasGeometricas:
    def __init__(self, triangulo,Triangulo, cuadrado, Cuadrado, rectangulo, Rectangulo):
        self.triangulo = triangulo  - Triangulo     
        self.cuadrado = cuadrado - Cuadrado
        self.rectangulo = rectangulo - Rectangulo

        Mostrar = "Ingresa el nombre de la figura geometrica para calcular su area y perimetro"
        print(Mostrar)
        Figura = input("Ingrese la figura geometrica (triangulo, cuadrado, rectangulo): ")
        if Figura == "triangulo":
            Base = float(input("Ingrese la base del triangulo: "))
            Altura = float(input("Ingrese la altura del triangulo: "))
            Lado1 = float(input("Ingrese el primer lado del triangulo: "))
            Lado2 = float(input("Ingrese el segundo lado del triangulo: "))
            AreaTriangulo = (Base * Altura) / 2
            PerimetroTriangulo = Base + Lado1 + Lado2
            print("El area del triangulo es:", AreaTriangulo)
            print("El perimetro del triangulo es:", PerimetroTriangulo)
        elif Figura == "cuadrado":
            Lado = float(input("Ingrese el lado del cuadrado: "))
            AreaCuadrado = Lado * Lado
            PerimetroCuadrado = 4 * Lado
            print("El area del cuadrado es:", AreaCuadrado)
            print("El perimetro del cuadrado es:", PerimetroCuadrado)
        elif Figura == "rectangulo":
            Base = float(input("Ingrese la base del rectangulo: "))
            Altura = float(input("Ingrese la altura del rectangulo: "))
            AreaRectangulo = Base * Altura
            PerimetroRectangulo = 2 * (Base + Altura)
            print("El area del rectangulo es:", AreaRectangulo)
            print("El perimetro del rectangulo es:", PerimetroRectangulo)
        else:
            print("Figura geometrica no valida")

if __name__ == "__main__":
    figuras = FigurasGeometricas(triangulo=0, Triangulo=0, cuadrado=0, Cuadrado=0, rectangulo=0, Rectangulo=0)
