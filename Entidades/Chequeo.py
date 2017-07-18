class Chequeo:
    def __init__(self, _parada, _esEntrada, _raspberryPi, _fechaRegistrada):
        self._parada = _parada
        self._esEntrada = _esEntrada
        self._raspberryPiAPI = _raspberryPi
        self._fechaRegistrada=_fechaRegistrada

    def __init__(self):
        pass
    def __get__(self, instance, owner):
        return self._parada

    def __set__(self, instance, value):
        self._parada = value

    def __get__(self, instance, owner):
        return self._esEntrada

    def __set__(self, instance, value):
        self._esEntrada = value

    def __get__(self, instance, owner):
        return self._raspberryPiAPI

    def __set__(self, instance, value):
        self._raspberryPiAPI = value

    def __get__(self, instance, owner):
        return self._fechaRegistrada

    def __set__(self, instance, value):
        self._fechaRegistrada = value
