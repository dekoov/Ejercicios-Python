class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad

#metodo getter
    def get_nombre(self):
        return self._nombre

#metodo setter
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

dalto = Persona("Lucas",21)

nombre = dalto.get_nombre()
print(nombre)

dalto.set_nombre("Pepito")

nombre = dalto.get_nombre()
print(nombre)