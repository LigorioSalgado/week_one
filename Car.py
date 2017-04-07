from Vehicle import Vehicle,Transport


class Car(Vehicle,Transport):

    def __init__(self,color,precio,motor,combustible,placas,caballos,num_puertas):
        super().__init__(color,precio,motor,combustible)
        self.placas = placas
        self.caballos = caballos
        self.num_puertas = num_puertas
    


print("Estoy en car")
print("Este es main")
print(__name__)

if __name__ == '__main__':
    car = Car("Rojo","121212121","V8","Dissel","345ert",150,2)
    print(car.moverse())
    print(car.precio)
    print(car.muestraTipo("Deportivo"))
    