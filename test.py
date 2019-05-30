from render import Render
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup( 21, GPIO.OUT, initial=GPIO.HIGH )

a = Render(4)
b = Render(3)
c = Render(1)


a.update_text("Display ", "4")
b.update_text("Display ", "3")
c.update_text("Display ", "1")
