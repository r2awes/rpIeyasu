from render import Render
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup( 21, GPIO.OUT, initial=GPIO.HIGH )

a = Render(4)
b = Render(3)
c = Render(1)

av = GPIO.input(21)

a.update_text( str(av), "a")
b.update_text("B", "b")
c.update_text("C", "c")
