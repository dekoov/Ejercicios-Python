class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

celular1 = Celular("Samsung","S23","48MP")
celular2 = Celular("Apple","iPhone 15 Pro","96MP")

print(celular2.marca)
print(celular1.modelo)