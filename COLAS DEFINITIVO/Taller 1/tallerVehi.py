#EJERCICIO 1
class Vehiculo: 
    def __init__(self, marca, combustible):
        self.marca= marca
        self.combustible= combustible
    
    def encender(self):
        print("encendiendo")
    
    def arrancar(self):
        print("🚗")

    def __str__(self):
        return "Vehiculo: Es un Vehiculo de Marca {}, y usa Combustible {} ".format(self.marca, self.combustible)

vehiculo = Vehiculo("BMW", "DIESEL")
print(vehiculo)

#EJERCICIO 2
class Moto(Vehiculo):
    def __init__(self, marca, combustible, motor, valor):
        self.marca= marca
        self.combustible= combustible
        self.motor = motor 
        self.valor = valor
    
    def __str__(self): 
        return "La moto es de marca {}, usa combustible tipo {}, tiene un motor {}, y cuesta {}".format(self.marca, self.combustible, self.motor, self.valor)

moto =Moto("Yamaha", "Gasolina", "4 tiempos", "10.000.000")
print(moto)

#EJERCICIO 3
class Carro(Vehiculo):
    def __init__(self, marca, combustible, motor, color, valor):
        self.marca= marca
        self.combustible= combustible
        self.motor = motor 
        self.valor = valor
        self.color = color
    
    def __str__(self): 
        return "El carro es de marca {}, usa combustible tipo {}, tiene un motor {}, es de color  {} y cuesta {}".format(self.marca, self.combustible, self.motor, self.color, self.valor)

carro =Carro("Toyota🚗(Prado)", "Gasolina", "VVT - I DUAL", "Gris Metalico", "360.000.000",)
print(carro)

#EJERCICIO 4 

class Vehículo2:
    tipo = str
    cantidadCombustiple = int
    def __init__(self, marca, combustible, tipo):
        self.marca = marca
        self.combustible = combustible
        self.tipo = tipo

    def encender(self):
        if (self.cantidadCombustible < 30):
            print("Nivel de gasolina bajo, dirijete a una gasolineria lo antes posible")
        else:
            print("El vehículo está encendido.")

    def arrancar(self):
        print("El vehículo está arrancando.")

    def __str__(self):
        return f"Tipo: Marca: {self.marca}, Combustible: {self.combustible}, Tipo: {self.tipo}"

class Moto(Vehículo2):
    def __init__(self, marca, combustible, motor, valor,):
        self.marca= marca
        self.combustible= combustible
        self.motor = motor 
        self.valor = valor
        self.tipo = "🏍️"
        self.cantidadCombustible = 40
    
    def __str__(self): 
        return "La moto es de marca {}, usa combustible tipo {}, tiene un motor {}, y cuesta {}".format(self.marca, self.combustible, self.motor, self.valor)

class Carro(Vehículo2):
    def __init__(self, marca, combustible, motor, color, valor):
        self.marca= marca
        self.combustible= combustible
        self.motor = motor 
        self.valor = valor
        self.color = color
        self.tipo = "🚗"
        self.cantidadCombustible = 20
    
    def __str__(self): 
        return "El carro es de marca {}, usa combustible tipo {}, tiene un motor {}, es de color  {} y cuesta {}".format(self.marca, self.combustible, self.motor, self.color, self.valor)


carro =Carro("Toyota🚗(Prado)", "Gasolina", "VVT - I DUAL", "Gris Metalico", "360.000.000",)
carro.encender()    
moto =Moto("Yamaha", "Gasolina", "4 tiempos", "10.000.000")
moto.encender()

#EJERCICIO 5


class Vehículo3:
    tipo = str
    cantidadCombustiple = int
    def __init__(self, marca, combustible, tipo):
        self.marca = marca
        self.combustible = combustible
        self.tipo = tipo

    def encender(self):
        if (self.cantidadCombustiple < 30):
            print("Nivel de gasolina bajo, dirijete a una gasolineria lo antes posible")
        else:
            print("El vehículo está encendido.")

    def marcha(self, kilometros):
        gasto = kilometros *0.5
        r = self.cantidadCombustiple- gasto

        if r <=0:
            print("por falta de gasolina el vehiculo se ha detenido")
        else:
            print("el vehiculo ha avanzado {}")

    def arrancar(self):
        print("El vehículo está arrancando.")

    def __str__(self):
        return f"Tipo: Marca: {self.marca}, Combustible: {self.combustible}, Tipo: {self.tipo}"

class Moto(Vehículo3):
    def __init__(self, marca, combustible, motor, valor,):
        self.marca= marca
        self.combustible= combustible
        self.motor = motor 
        self.valor = valor
        self.tipo = "🏍️"
        self.cantidadCombustiple = 20
       
    
    def __str__(self): 
        return "La moto es de marca {}, usa combustible tipo {}, tiene un motor {}, y cuesta {}".format(self.marca, self.combustible, self.motor, self.valor)

class Carro(Vehículo3):
    def __init__(self, marca, combustible, motor, color, valor):
        self.marca= marca
        self.combustible= combustible
        self.motor = motor 
        self.valor = valor
        self.color = color
        self.tipo = "🚗"
        self.cantidadCombustiple = 50
        
    
    def __str__(self): 
        return "El carro es de marca {}, usa combustible tipo {}, tiene un motor {}, es de color  {} y cuesta {}".format(self.marca, self.combustible, self.motor, self.color, self.valor)


carro =Carro("Toyota🚗(Prado)", "Gasolina", "VVT - I DUAL", "Gris Metalico", "360.000.000",)
carro.encender()
carro.marcha(40)   


moto =Moto("Yamaha", "Gasolina", "4 tiempos", "10.000.000")
moto.encender()
moto.marcha(70)