class Vehicle:

    def __init__(self,color,precio,motor,combustible):
         self.color = color
         self.precio = precio
         self.motor = motor
         self.combustible = combustible

    def moverse(self):
        return "Me estoy moviendo"
    
    def recargarCombustible(self):
        return "ya tengo el tanque lleno"


class Transport:

    def __init__(self,tipo):
        self.tipo = tipo
    
    def muestraTipo(self,tipo):
        return "Mi tipo es : %s" % tipo


print("Estoy en vehicle")
print("Este es main")
print(__name__)