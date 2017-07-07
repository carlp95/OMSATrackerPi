import RPi.GPIO as io
import time
<<<<<<< HEAD
####from RestAPI import RestAPI
=======
from RestAPI import RestAPI

>>>>>>> 20c6e4e85556d31305bc51a1479e56b43ab162e8
io.setmode(io.BCM)
io.setup(7,io.IN)

man = 0
status =0
##restAPI = RestAPI()
while 1:
	if io.input(7) == 1 :
		man =man+1
		##restAPI.postUbicacion(2,3)
		currentHour = time.localtime().tm_hour
		print " detecto %d" %(man)
		##print "hora %d" %(currentHour)
		status =1

	elif io.input(7) ==0:
		print "no dectetado"
		status =0
	time.sleep(3)
