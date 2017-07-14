class Chequeo:
    def __init__(self, _parada, _esEntrada, _raspberryPi, _fechaRegistrada):
        self._parada = _parada
        self._esEntrada = _esEntrada
        self._raspberryPi= _raspberryPi
        self._fechaRegistrada=_fechaRegistrada

    def __get__(self, instance, owner):
        return self._parada

    def __set__(self, instance, value):
        self._parada = value

    def __get__(self, instance, owner):
        return self._esEntrada

    def __set__(self, instance, value):
        self._esEntrada = value

    def __get__(self, instance, owner):
        return self._raspberryPi

    def __set__(self, instance, value):
        self._raspberryPi = value

    def __get__(self, instance, owner):
        return self._fechaRegistrada

    def __set__(self, instance, value):
        self._fechaRegistrada = value
