from threading import Thread
from time import sleep

def espera(n):
 sleep(n)
 print "Espero %s segundos." % n


subproceso = Thread(target=espera, args=(5,))

subproceso.start()

print "Yo espero menos."
subproceso.join()
print "Yo llego tarde."