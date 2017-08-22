class Autobus:
    def __init__(self, _modelo,_cantidadDeAsientos, _numeroSerial,_peso,_ruta, _ultimaParada, _anoFabricacion,_activo, _conductor, _fechaCreada, _ultimaFechaModificada, _precio, _tieneAireAcondicionado,_cantidadDePasajerosActual, _coordenada):
        self._modelo=_modelo
        self._cantidadDeAsientos=_cantidadDeAsientos
        self._peso=_peso
        self._numeroSerial=_numeroSerial
        self._ultimaParada=_ultimaParada
        self._ruta=_ruta
        self._anoFabicacion =_anoFabricacion
        self._activo=_activo
        self._conductor = _conductor
        self._fechaCreada=_fechaCreada
        self._ultimaFechaModificado = _ultimaFechaModificada
        self._precio = _precio
        self._tieneAireAcondicionado=_tieneAireAcondicionado
        self._cantidadDePasajerosActual=_cantidadDePasajerosActual
        self._coordenada=_coordenada

    def __init__(self):
        pass
    def __get__(self, instance, owner):
        return self._modelo
    def __set__(self, instance, value):
        self._modelo=value

    def __get__(self, instance, owner):
        return self._cantidadDeAsientos
    def __set__(self, instance, value):
        self._cantidadDeAsientos = value

    def __get__(self, instance, owner):
        return self._peso
    def __set__(self, instance, value):
        self._peso=value

    def __get__(self, instance, owner):
        return self._raspberryPiAPI

    def __set__(self, instance, value):
        self._raspberryPiAPI=value

    def __get__(self, instance, owner):
        return self._ultimaParada
    def __set__(self, instance, value):
        self._ultimaParada=value

    def __get__(self, instance, owner):
        return self._ruta
    def __set__(self, instance, value):
        self._ruta=value

    def __get__(self, instance, owner):
        return self._anoFabicacion
    def __set__(self, instance, value):
        self._anoFabicacion=value

    def __get__(self, instance, owner):
        return self._activo
    def __set__(self, instance, value):
        self._activo=value

    def __get__(self, instance, owner):
        return self._conductor
    def __set__(self, instance, value):
        self._conductor=value

    def __get__(self, instance, owner):
        return self._fechaCreada
    def __set__(self, instance, value):
        self._fechaCreada=value

    def __get__(self, instance, owner):
        return self._ultimaFechaModificado
    def __set__(self, instance, value):
        self._ultimaFechaModificado=value

    def __get__(self, instance, owner):
        return self._precio
    def __set__(self, instance, value):
        self._precio=value

    def __get__(self, instance, owner):
        return self._cantidadDePasajerosActual
    def __set__(self, instance, value):
        self._cantidadDePasajerosActual=value

    def __get__(self, instance, owner):
        return self._coordenada
    def __set__(self, instance, value):
        self._coordenada = value

    def __get__(self, instance, owner):
        return self._tieneAireAcondicionado
    def __set__(self, instance, value):
        self._tieneAireAcondicionado = value

