import unirest
from Entidades import Coordenada

class RestAPI:
    url = "http://httpbin.org/post"

    def postUbicacion(self, coordenada, hora ):
        response = unirest.post(self.url, headers={"Accept": "application/json"},
                                params={"coordenada": coordenada, "hora": hora})
