class Coordenada:


    def __init__(self, longitud, latitude):
        self.longitud = longitud
        self.latitude = latitude

    def __init__(self):
        pass

    def __get__(self, instance, owner):
        return self.longitud

    def __set__(self, instance, value):
        self.longitud= value

    def __get__(self, instance, owner):
        return self.latitude

    def __set__(self, instance, value):
        self.latitude = value

    def __unicode__(self):
        return self.latitude + "," + self.longitud
