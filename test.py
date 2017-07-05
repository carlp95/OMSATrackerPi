import RPi.GPIO as io
import time
from RestAPI import RestAPI

io.setmode(io.BCM)
io.setup(7,io.IN)

man = 0
status =0
restAPI = RestAPI()
while 1:
	if io.input(7) == 1 :
		man =man+1
		restAPI.postUbicacion(2,3)
		currentHour = time.localtime().tm_hour
		print " detecto %d" %(man)
		##print "hora %d" %(currentHour)
		status =1

	elif io.input(7) ==0:
		print "no dectetado"
		status =0
	time.sleep(3)
