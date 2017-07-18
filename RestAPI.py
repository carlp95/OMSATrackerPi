import unirest
from Entidades import Coordenada

class RestAPI:
    url = "http://httpbin.org/post"
    ACCEPT_TYPE = "application/json"

    def postUbicacion(self, serialNummber, coordenada, fechaRegistrada ):
        response = unirest.post(self.url, headers={"Accept": self.ACCEPT_TYPE},
                                params={"numeroSerial": serialNummber, "latitud": coordenada.latitud,
                                        "longitud": coordenada.longitud,  "fecha": fechaRegistrada})

    def postChequeos(self, chequeo):
        response= unirest.post(self.url+"/api/chequeo/guardar", headers={"Accept": self.ACCEPT_TYPE},
                               params={"chequeo": chequeo})

    def postCantidadDePasajerosActual(self, fecha, cantidadPasajeros, numeroSerial):
        response = unirest.post(self.url+"/api/autobus/modificar/cantidadPasajeros", headers={"Accept": self.ACCEPT_TYPE},
                                params={"numeroSerial": numeroSerial, "cantidadPasajeros": cantidadPasajeros, "fecha": fecha})

    def postEstadoActualAndRuta(self, numeroSerial, coordenada, estadoActual,fecha):
        response= unirest.post(self.url, headers={"Accept":self.ACCEPT_TYPE}, params={
            "estadoActual": estadoActual, "fecha": fecha, "longitud": coordenada.longitud,
            "latitud": coordenada.latitud, "numeroSerial": numeroSerial
        })