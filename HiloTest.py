import threading
import time

def espera():
 a =0
 while (a<=7):

  time.sleep(5)
  print "Primer Hilo."
  a+=1

def segundoHilo():
 b=0
 while(b<=7):
  time.sleep(3)
  print "Segundo Hilo"
  b+=1

subproceso = threading.Thread(name='espera', target=espera)
subproceso.start()

Hilo2= threading.Thread(name='segundoHilo', target=segundoHilo)
Hilo2.start()
