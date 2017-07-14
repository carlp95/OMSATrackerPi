class Parada:
    def __init__(self,_nombre,_ruta,_paradaAnterior, _paradaSiguiente, _coordenada):
        self._nombre= _nombre
        self._ruta = _ruta
        self._paradaAnterior=_paradaAnterior
        self._paradaSiguiente= _paradaSiguiente
        self._coordenada = _coordenada
    def __get__(self, instance, owner):
        return self._nombre
    def __set__(self, instance, value):
        self._nombre = value

    def __get__(self, instance, owner):
        return self._ruta

    def __set__(self, instance, value):
        self._ruta = value

    def __get__(self, instance, owner):
        return self._paradaAnterior

    def __set__(self, instance, value):
        self._paradaAnterior = value

    def __get__(self, instance, owner):
        return self._paradaSiguiente

    def __set__(self, instance, value):
        self._paradaSiguiente = value

    def __get__(self, instance, owner):
        return self._coordenada

    def __set__(self, instance, value):
        self._coordenada = value

