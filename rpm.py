import random

import RPi.GPIO as GPIO

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

regular = ImageFont.truetype(font="BarlowCondensed-Regular.ttf", size=35, index=0 )
light = ImageFont.truetype(font="BarlowCondensed-Light.ttf", size=15, index=0 )

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.IN)

def rpmRead():
	#testing read
	if GPIO.Input(40) == 0:
		return 1
	else:
		return 0
	#random testing only return random.randint(400, 6800)

while True: 
	rpm = rpmRead()
	draw.rectangle((0, 0, width, height), outline=0, fill=0)
	draw.text((x, top), str(rpm), font=regular, fill=255 )
	draw.text((x+100, top+15), "rpm", font=light, fill=255 )

	disp.image(image)
	disp.display()
	time.sleep(.1)
