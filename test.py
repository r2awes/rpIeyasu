#! /usr/bin/env python

from render import Render
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup( 21, GPIO.OUT, initial=GPIO.HIGH )

l = Render(4)
m = Render(3)
r = Render(1)

def grow( num, ite ):
	return num + ite

con = True
f1 = 0
f2 = 0
try:
	while con:
		l.update_text( str(f1), "mph" )
		m.update_text( str(f2), "rpm" )
		r.update_text( "Walk It Like I Talk It", "Migos" )
		f1 = grow( f1, 10 )
		f2 = grow( f2, 100 )
		con = f2 < 8000
		time.sleep(.1)
	l.clear()
	m.clear()
	r.clear()
except KeyboardInterrupt:
		l.clear()
		m.clear()
		r.clear()