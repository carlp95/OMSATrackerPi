class Chequeo:
    def __init__(self, parada, _esEntrada, _fechaRegistrada, _autobus):
        self.parada = parada
        self._esEntrada = _esEntrada
        self._fechaRegistrada=_fechaRegistrada
        self._autobus = _autobus

    def __init__(self):
        pass

    def __get__(self, instance, owner):
        return self._autobus

    def __set__(self, instance, value):
        self._autobus = value

    def __get__(self, instance, owner):
        return self.parada

    def __set__(self, instance, value):
        self.parada = value

    def __get__(self, instance, owner):
        return self._esEntrada

    def __set__(self, instance, value):
        self._esEntrada = value


    def __get__(self, instance, owner):
        return self._fechaRegistrada

    def __set__(self, instance, value):
        self._fechaRegistrada = value
