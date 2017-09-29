import unirest
from Entidades import Coordenada
import requests


class RestAPI:
    url = "https://omsa.herokuapp.com"
    ACCEPT_TYPE = "application/json"

    def postUbicacion(self, serialNummber, coordenada, fechaRegistrada):
        try:
            response = requests.put("http://omsa.herokuapp.com/api/autobus/modificar/posicion/",
                                    headers={"content-type": 'application/json;charset=utf-8',
                                             "Accept": "application/json"},
                                    json={
                                        "raspberryPiNumeroSerial": serialNummber,
                                        "coordenada": {
                                            "latitude": coordenada.latitude,
                                            "longitud": coordenada.longitud
                                        },
                                        "ultimaFechaModificada": fechaRegistrada
                                    }
                                    )

            print('posicion----->')
            print(response.status_code)
            print (response.json())
        except:
            pass

    def postChequeos(self, chequeo, numeroSerial):
        try:
            response = requests.post(self.url + "/api/chequeo/guardar",
                                     headers={'content-type': 'application/json', "Accept": self.ACCEPT_TYPE},
                                     json={
                                         "fechaRegistrada": chequeo._fechaRegistrada,
                                         "autobus": {
                                             "raspberryPiNumeroSerial": numeroSerial
                                         },
                                         "esEntrada": chequeo._esEntrada,
                                         "parada": {
                                             'coordenada': {
                                                 'longitud': chequeo.parada.coordenada.longitud,
                                                 'latitude': chequeo.parada.coordenada.latitude
                                             }
                                         }
                                     }
                                     )
            print('Coordenadas de chequeo -->', chequeo.parada.coordenada.longitud)
            print(chequeo.parada.coordenada.latitude)
            print(chequeo._esEntrada)
            print(chequeo._fechaRegistrada)
            print('chequeos---->')
            print(response.status_code)
            print(response.json())
        except:
            pass

    def postCantidadDePasajerosActual(self, fecha, cantidadPasajeros, numeroSerial):
        try:
            response = requests.put(self.url + "/api/autobus/modificar/cantidadPasajeros",
                                    headers={'content-type': 'application/json;charset=utf-8',
                                             "Accept": self.ACCEPT_TYPE},
                                    json={
                                        "raspberryPiNumeroSerial": numeroSerial,
                                        "cantidadDePasajerosActual": cantidadPasajeros,
                                        "ultimaFechaModificada": fecha
                                    }
                                    )
            print('cantidad de pasajeros----->')
            print(response.status_code)
        except:
            pass

    def postEstadoActualAndRuta(self, numeroSerial, coordenada, estadoActual, fecha):
        try:
            response = requests.put(self.url + "/api/autobus/modificar/estado",
                                    headers={'content-type': 'application/json', "Accept": self.ACCEPT_TYPE},
                                    json={
                                        "activo": estadoActual,
                                        "ultimaFechaModificada": fecha,
                                        "coordenada": {
                                            "longitud": coordenada.longitud,
                                            "latitude": coordenada.latitude
                                        },
                                        "raspberryPiNumeroSerial": numeroSerial
                                    }
                                    )
            print('estado----->')
            print(response.status_code)
        except:
            pass
