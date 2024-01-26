class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola estoy hablando un poco")

class Empleado(Persona):
    pass

roberto = Empleado("Roberto",43,"argentino")

roberto.hablar()
print(roberto.nacionalidad)