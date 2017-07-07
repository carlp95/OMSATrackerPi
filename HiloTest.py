import threading
import time
import gps

import RPi.GPIO as io
import time
from RestAPI import RestAPI

io.setmode(io.BCM)
io.setup(7,io.IN)

man = 0
status =0
restAPI = RestAPI()

# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)



def espera():
 a =0
 while (a<=7):
  try:
   report = session.next()
   # Wait for a 'TPV' report and display the current time
   # To see all report data, uncomment the line below
   # print report
   if report['class'] == 'TPV':
    if hasattr(report, 'lat'):
     print report.lat
  except KeyError:
   pass
  except KeyboardInterrupt:
   quit()
  except StopIteration:
   session = None
   print "GPSD has terminated"
  time.sleep(5)
  print "Primer Hilo."
  a+=1

def segundoHilo():
 b=0
 while(b<=20):
  if io.input(7) == 1:
   man = man + 1
   restAPI.postUbicacion(2, 3)
   currentHour = time.localtime().tm_hour
   print " detecto %d" % (man)
   ##print "hora %d" %(currentHour)
   status = 1

  elif io.input(7) == 0:
   print "no dectetado"
   status = 0
  time.sleep(3)
  print "Segundo Hilo"
  b+=1

subproceso = threading.Thread(name='espera', target=espera)
subproceso.start()

Hilo2= threading.Thread(name='segundoHilo', target=segundoHilo)
Hilo2.start()
