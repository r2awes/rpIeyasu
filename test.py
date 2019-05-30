from render import Render
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup( 21, GPIO.OUT, initial=GPIO.HIGH )

a = Render(1)
b = Render(3)
c = Render(4)

a.update_text("A", "a")
b.update_text("B", "b")
c.update_text("C", "c")

print GPIO.getmode()
