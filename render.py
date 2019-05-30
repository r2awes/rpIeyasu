import time

"""
Uncomment to use I2C OLEDs that work with Adafruit's SSD1306 package
"""
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class Render:
	RST = None
	
	def __init__(self, bus_number):
		self.debug = True
		self.conn = True
		self.text = " "
		self.title = " "
		self.bus_number = bus_number
		self.disp = Adafruit_SSD1306.SSD1306_128_32(rst=Render.RST, i2c_bus=bus_number)
		
		try:
			self.disp.begin()
		except IOError: 
			print ("Check if the ports to see if the display on " + str(bus_number) + " is connected properly")
			self.conn = False
		
		self.handle_debug(self.debug, self.conn)
		
	def handle_debug(self, debug, conn):
		if( debug ):
			self.log_text()

		if( debug and conn ):
			print("Check the connection to the ports for bus number " + str(self.bus_number) +".")

		if( conn ):
			self.print_text()

	def log_text(self):
		print self.text + " " + self.title

	def print_text(self):
		
		self.disp.clear()
		self.disp.display()

		width = self.disp.width
		height = self.disp.height
		image = Image.new('1', (width, height))
		draw = ImageDraw.Draw(image)
		draw.rectangle((0,0,width,height), outline=0, fill=0)
		padding = -2
		top = padding
		#bottom = height-padding

		x = 0

		regular = ImageFont.truetype(font="BarlowCondensed-Regular.ttf", size=35, index=0 )
		light = ImageFont.truetype(font="BarlowCondensed-Light.ttf", size=15, index=0 )
		
		try:
			draw.rectangle((0, 0, width, height), outline=0, fill=0)
			draw.text((x, top), self.text, font=regular, fill=255 )
			draw.text((x+100, top+15), self.title, font=light, fill=255 )

			self.disp.image(image)
			self.disp.display()
			time.sleep(.1)
		finally: 
			draw.rectangle((0, 0, width, height), outline=0, fill=0)
		

	def update_text(self, text, title):
		self.text = text
		if( title != "" ):
			self.title = title
		if( text == "clear" ):
			self.title = ""
			self.text = ""

		if(self.debug):
			self.log_text()
		if(self.conn):
			self.print_text()

	def clear(self):
		self.update_text("clear", "")
		
