#! /usr/bin/env python

from render import Render
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup( 21, GPIO.OUT, initial=GPIO.HIGH )

l = Render(4)
m = Render(3)
r = Render(1)

def grow( num ):
	return num + 100

con = True
field = 0
try:
	while con:
		l.update_text( str(field), "L" )
		m.update_text( str(field), "M" )
		r.update_text( str(field), "R" )
		field = grow( field )
		con = field < 8000
		time.sleep(.1)
except KeyboardInterrupt:
		l.clear()
		m.clear()
		r.clear()