class Persona:
    def __init__(self, nombre, ano_nacimiento, edad):
        self.nombre = nombre
        self.ano_nacimiento = ano_nacimiento
        self.edad = edad

    def calcular_edad(self, ano_actual):
        self.edad = ano_actual - self.ano_nacimiento
        return self.edad