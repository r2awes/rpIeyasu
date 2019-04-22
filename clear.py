import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

RST = None
bus_number = 3

disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, i2c_bus=bus_number)

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = -2
top = padding
bottom = height-padding

x = 0

while True: 
	draw.rectangle((0,0,width,height), outline=0, fill=0)

	disp.image(image)
	disp.display()
	time.sleep(.1)