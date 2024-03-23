from .cdamodel import Vehicle, Tests

class Nodo:
    def __init__(self, valor: Vehicle):
        self.valor = valor
        self.siguiente = None

class Vehiclemanager:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def esta_vacia(self):
        return self.primero is None

    def encolar(self, valor: Vehicle):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.primero = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
        self.ultimo = nuevo_nodo
    
    def desencolar(self):
        if self.esta_vacia():
            return None
        valor = self.primero.valor
        self.primero = self.primero.siguiente
        if self.primero is None:
            self.ultimo = None
        return valor
    
    def agregar_pruebas_tecnicas(self, tipo: str):
        tipos_tests = {
            'moto': ['frenos', 'luces', 'gases', 'llantas'],
            'carro': ['frenos', 'luces', 'gases', 'llantas'],
            'camion': ['frenos', 'luces', 'aceite', 'aire', 'frenos_de_aire']
        }
        tests = []
        for test_name in tipos_tests.get(tipo, []):
            tests.append(Tests(nombre=test_name, resultado=False))
        return tests
     
    def ver_listado(self):
        if self.esta_vacia():
            return []

        elementos = []
        current = self.primero
        while current is not None:
            elementos.append(current.valor)
            current = current.siguiente
        return elementos

    def ver_primero(self):
        if self.esta_vacia():
            return None
        return self.primero.valor

    def ver_ultimo(self):
        if self.esta_vacia():
            return None
        return self.ultimo.valor

    def contar(self) -> int:
        count = 0
        current = self.primero
        while current is not None:
            count += 1
            current = current.siguiente
        return count
