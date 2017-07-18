class RaspberryPi:
    def __init__(self,_numeroSerial,_ipAddress,_macAddress,_autobus ):
        self._numeroSerial = _numeroSerial
        self._ipAddress = _ipAddress
        self._macAddress = _macAddress
        self._autobus = _autobus

    def __init__(self):
        pass

    def __get__(self, instance, owner):
        return self._numeroSerial

    def __set__(self, instance, value):
        self._numeroSerial = value

    def __get__(self, instance, owner):
        return self._ipAddress

    def __set__(self, instance, value):
        self._ipAddress = value

    def __get__(self, instance, owner):
        return self._autobus

    def __set__(self, instance, value):
        self._autobus = value


p = RaspberryPi()

p._numeroSerial=13
p._puerto = 1532


print p._numeroSerial,p._puerto