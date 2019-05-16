import os
from threading import Thread

from obd_capture import OBD_Capture
from obd_sensors import SENSORS
from obd_sensors import *
from obd_io import OBDPort
from render import Render

from obd_utils import scanSerial

import signal
import time
import sys


obd = None
portnames = scanSerial()
for port in portnames:
	obd = OBDPort( port, None, 2, 2)
	if( obd.State == 0 ):
		obd.close()
		obd.port = None
	else:
		break
		
RPM = 12
SPEED = 13
#MPG = 2
TEMP = 5

rpm_screen = Render(1)
speed_screen = Render(3)
temp_screen = Render(4)
#mpg_screen = Render(3)

def parse_sensor_data(self):
	rpm = obd.sensor( RPM )
	speed = obd.sensor( SPEED )
	temp = obd.sensor( TEMP )
	#mpg = obd.sensor( MPG )

	rpm_screen.update_text(rpm[1], rpm[0])
	speed_screen.update_text(speed[1], speed[0])
	temp_screen.update_text(temp[1], temp[0])
	#mpg_screen.update_text(mpg[1], mpg[0])
	
while True:
	parse_sensor_data()
	time.sleep(.1)

""" 
def run_program():
  while True:
    time.sleep(1)
    print("a")

def exit_gracefully(signum, frame):
	# restore the original signal handler as otherwise evil things will happen
	# in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
	signal.signal(signal.SIGINT, original_sigint)

	try:
			if raw_input("\nReally quit? (y/n)> ").lower().startswith('y'):
					sys.exit(1)

	except KeyboardInterrupt:
			print("Ok ok, quitting")
			sys.exit(1)

	# restore the exit gracefully handler here    
	signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    # store the original SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
    run_program() """