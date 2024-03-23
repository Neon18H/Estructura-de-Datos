class Articulo:
    tipo: str
    anio: int
    referencia: str
    nombre: str
    precio: float

    def __init__(self, nombre, precio) :
        self.nombre = nombre
        self.precio = precio

    def asiganar_nombre(self, nombre)->str:
        self.nombre = nombre
    
    def asignar_precio(self, precio)-> float:
        self.precio= precio

    def asignar_tipo(self, tipo) -> None:
        self.tipo = tipo

    def asignar_anio(self, anio) -> None:
        self.anio = anio

    def asignar_referencia(self, referencia)-> None:
        self.referencia = referencia

#################################################################
    def obtener_nombre(self, nombre)->str:
        return self.nombre 
    
    def obtener_precio(self, precio)-> float:
        return self.precio

    def obtener_tipo(self, tipo) -> None:
        return self.tipo

    def obtener_anio(self, anio) -> None:
        return self.anio 

    def obtener_referencia(self, referencia)-> None:
        return self.referencia 


    
    @staticmethod
    def procesar():
        pass



class Monitor (Articulo):
    resolucion: str
    alto: int
    ancho: int
    tasa_refresco: int

    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)
        self.tipo = "Monitor"
    
    def asignar_resolucion(self, resolucion) ->None:
        self = resolucion
    
    def asignar_ancho(self, ancho) ->int:
       self = ancho

    def asignar_alto(self, alto) ->int:
        self= alto

    def asignar_tasa_refresco(self, tasa_refresco) ->None:
        self.tasa_refresco = tasa_refresco

############################################################################
    def obtener_resolucion(self, resolucion) ->None:
        return self.resolucion
    
    def obtener_ancho(self, ancho) ->int:
       return self.ancho

    def obtener_alto(self, alto) ->int:
        return self.alto

    def obtener_tasa_refresco(self, tasa_refresco) ->None:
        return self.tasa_refresco
    
    


Monitor_dell = Monitor("Monitor Dell", 1000)
Monitor_dell.asignar_resolucion("1920x10.180")
Monitor_dell.obtener_nombre() #pantalla Dell
