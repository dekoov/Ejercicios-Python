class Gato():
    def sonido(self):
        return "Miau"

#mismo metodo diferente sonido
class Perro():
    def sonido(self):
        return "Guau"

gato = Gato()
perro = Perro()

print(perro.sonido())