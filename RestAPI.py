import unirest
from Entidades import Coordenada

class RestAPI:
    url = "https://omsa.herokuapp.com"
    ACCEPT_TYPE = "application/json"

    def postUbicacion(self, serialNummber, coordenada, fechaRegistrada ):
        unirest.post(self.url+"/api/autobus/modificar/posicion/", headers={"Accept": self.ACCEPT_TYPE},
                                params={
                                        "raspberryPiNumeroSerial": serialNummber,
                                        "coordenada":{
                                            "latitude": coordenada.latitud,
                                            "longitud": coordenada.longitud
                                        },
                                        "ultimaFechaModificada": fechaRegistrada
                                }
                     )

    def postChequeos(self, chequeo ,numeroSerial):
        unirest.post(self.url+"/api/chequeo/guardar", headers={"Accept": self.ACCEPT_TYPE},
                               params={
                                        "fechaRegistrada": chequeo._fechaRegistrada,
                                        "autobus":{
                                            "raspberryPiNumeroSerial":numeroSerial
                                        },
                                        "esEntrada":chequeo._esEntrada,
                                        "parada":chequeo._parada
                               }
                     )

    def postCantidadDePasajerosActual(self, fecha, cantidadPasajeros, numeroSerial):
        unirest.post(self.url+"/api/autobus/modificar/cantidadPasajeros", headers={"Accept": self.ACCEPT_TYPE},
                                params={
                                        "raspberryPiNumeroSerial": numeroSerial,
                                        "cantidadDePasajerosActual": cantidadPasajeros,
                                        "ultimaFechaModificada": fecha
                                }
                     )

    def postEstadoActualAndRuta(self, numeroSerial, coordenada, estadoActual,fecha):
        unirest.post(self.url+"/api/autobus/modificar/estado", headers={"Accept":self.ACCEPT_TYPE},
                             params={
                                    "activo": estadoActual,
                                    "ultimaFechaModificada": fecha,
                                    "coordenada":{
                                        "longitud":coordenada.longitud,
                                        "latitud": coordenada.latitud
                                    },
                                    "raspberryPiNumeroSerial": numeroSerial
                             }
                     )
