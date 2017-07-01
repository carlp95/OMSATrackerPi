class Coordenada:
    def __init__(self, longitud, latitud):
        self.longitud = longitud
        self.latitud = latitud

    def __unicode__(self):
        return self.latitud + "," + self.longitud
