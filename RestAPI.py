import unirest
from Entidades import Coordenada

class RestAPI:
    url = "https://omsa.herokuapp.com"
    ACCEPT_TYPE = "application/json"

    def postUbicacion(self, serialNummber, coordenada, fechaRegistrada ):
<<<<<<< HEAD
	print(serialNummber)
        response = unirest.post(self.url+"/api/autobus/modificar/posicion/", headers={"Accept": "application/json"},
                                params={"numeroSerial": serialNummber, "latitud": coordenada.latitud,
                                        "longitud": coordenada.longitud,  "fecha": fechaRegistrada})
        print (response.body)
        print(response.code)

=======
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
>>>>>>> d841f9675e8adeb2ceaf98b9872f6907794f8454

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
<<<<<<< HEAD
        unirest.post(self.url, headers={"Accept":self.ACCEPT_TYPE}, params={
            "estadoActual": estadoActual, "fecha": fecha, "longitud": coordenada.longitud,
            "latitud": coordenada.latitud, "numeroSerial": numeroSerial
        })
=======
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
>>>>>>> d841f9675e8adeb2ceaf98b9872f6907794f8454
