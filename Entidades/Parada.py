class Parada:
    def __init__(self,nombre,ruta,paradaAnterior, paradaSiguiente, coordenada):
        self.nombre= nombre
        self.ruta= ruta
        self.paradaAnterior= paradaAnterior
        self.paradaSiguiente= paradaSiguiente
        self.coordenada=coordenada
    def __init__(self):
        pass
    def __get__(self, instance, owner):
        return self.nombre
    def __set__(self, instance, value):
        self.nombre = value

    def __get__(self, instance, owner):
        return self.ruta

    def __set__(self, instance, value):
        self.ruta = value

    def __get__(self, instance, owner):
        return self.paradaAnterior

    def __set__(self, instance, value):
        self.paradaAnterior = value

    def __get__(self, instance, owner):
        return self.paradaSiguiente

    def __set__(self, instance, value):
        self.paradaSiguiente = value

    def __get__(self, instance, owner):
        return self.coordenada

    def __set__(self, instance, value):
        self.coordenada = value

