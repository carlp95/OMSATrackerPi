class Coordenada:
    def __init__(self):
        pass

    def __init__(self, longitud, latitud):
        self.longitud = longitud
        self.latitud = latitud

    def __get__(self, instance, owner):
        return self.longitud

    def __set__(self, instance, value):
        self.longitud= value

    def __get__(self, instance, owner):
        return self.latitud

    def __set__(self, instance, value):
        self.latitud = value

    def __unicode__(self):
        return self.latitud + "," + self.longitud
