class Gato():
    def sonido(self):
        return "Miau"

#mismo metodo diferente sonido
class Perro():
    def sonido(self):
        return "Guau"

def hacer_sonido(animal):
    print(animal.sonido())

gato = Gato()
perro = Perro()

hacer_sonido(gato)
hacer_sonido(perro)

print(perro.sonido())
