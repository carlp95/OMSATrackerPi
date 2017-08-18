import RPi.GPIO as io
import time
import socket
from RestAPI import RestAPI
from GPS import GpsPoller
from Entidades import Autobus, Chequeo, Coordenada, Parada, RaspberryPi

io.setmode(io.BCM)
io.setup(7, io.IN)
io.setup(8, io.IN)

#
# def getMAC(interface):
#     # Return the MAC address of interface
#     try:
#         str = open('/sys/class/net/' + interface + '/address').read()
#     except:
#         str = "00:00:00:00:00:00"
#     return str[0:17]


# getting the serial number
def getserial():
    # Extract serial from cpuinfo file
    cpuserial = "0000000000000000"
    try:
        f = open('/proc/cpuinfo', 'r')
        for line in f:
            if line[0:6] == 'Serial':
                cpuserial = line[10:26]
        f.close()
    except:
        cpuserial = "ERROR000000000"

    return cpuserial


# getting the raspberrypi Ip
# def get_ip():
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     try:
#         # doesn't even have to be reachable
#         s.connect(('10.255.255.255', 1))
#         IP = s.getsockname()[0]
#     except:
#         IP = '127.0.0.1'
#     finally:
#         s.close()
#     return IP

# raspberry = RaspberryPi.RaspberryPi()
# raspberry._numeroSerial = getserial()
# raspberry._macAddress = getMAC("wlan0")
# raspberry._ipAddress = get_ip()
#raspberry._autobus = "to be used";

#autobus = Autobus.Autobus()

# main variable
man = 0
status = 0
restAPI = RestAPI()
chequeos = []
contadorDeNodeteccion = 0

gpsc = GpsPoller()  # create the thread
gpsc.start()  # start it up
cont=0
estadoActual = True
while 1:
    cont += 1
    if(cont==5):
        try:
            coor = Coordenada.Coordenada()
            coor.latitud = gpsc.fix.latitude
            coor.longitud = gpsc.fix.longitude
            restAPI.postEstadoActualAndRuta(getserial(), coor, estadoActual, int(time.time()))
            cont = 0
        except:
            cont = 0
            pass

    if io.input(7) == 1:
        man += 1
        print " detecto una subida%d" % (man)

        # registrando un chequeo
        chequeo = Chequeo.Chequeo()
        chequeo._esEntrada = True
        chequeo._raspberryPiAPI = raspberry
        chequeo._fechaRegistrada = int(time.time())
        coordenada = Coordenada.Coordenada()

        gpsd = GpsPoller()
        gpsd.start()
        # time.sleep(1)

        coordenada.latitud = gpsd.fix.latitude
        coordenada.longitud = gpsd.fix.longitude
        gpsd.stopController()
        parada = Parada.Parada()
        parada._coordenada = coordenada
        chequeo._parada = parada
        chequeos.append(chequeo)

        status = 1
        contadorDeNodeteccion = 0
    elif io.input(8) == 1:
        man -= 1
        if man < 0:
            man = 0
        print "detecto una bajada %d" % (man)
        # registrando un chequeo
        chequeo = Chequeo.Chequeo()
        chequeo._esEntrada = True
        chequeo._raspberryPi = raspberry
        chequeo._fechaRegistrada = int(time.time())
        coordenada = Coordenada.Coordenada()

        gpsd = GpsPoller()
        gpsd.start()
        # time.sleep(1)

        coordenada.latitud = gpsd.fix.latitude
        coordenada.longitud = gpsd.fix.longitude
        gpsd.stopController()

        parada = Parada.Parada()
        parada._coordenada = coordenada
        chequeo._parada = parada
        chequeos.append(chequeo)
        status = 1
        contadorDeNodeteccion =0
    elif io.input(7) == 0 or io.input(8) == 0:
        print "no dectetado"
        contadorDeNodeteccion += 1
        status = 0
    time.sleep(3)

    if(contadorDeNodeteccion==60):
        for chequeodetectado in chequeos:
            restAPI.postChequeos(chequeodetectado, getserial())
        contadorDeNodeteccion=0

        #actualizando cantidad de pasajeros
        restAPI.postCantidadDePasajerosActual(int(time.time()), man, getserial())
