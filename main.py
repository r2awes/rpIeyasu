import os
from threading import Thread

from obd_capture import OBD_Capture
from obd_sensors import SENSORS
from obd_sensors import *
from obd_io import OBDPort
from render import Render

def obd_connect(o):
	o.connect()

class OBDConnection(object):
	def __init__(self):
		self.c = OBD_Capture()
		def get_capture(self):
			return self.c

		def connect(self):
			self.t = Thread(target=obd_connect, args=(self.c,))
			self.t.start()

		def is_connected(self):
			return self.c.is_connected()

		def get_output(self):
			if self.c and self.c.is_connected():
				return self.c.capture_data()
			return ""

		def get_port(self):
			return self.c.is_connected()

		def get_port_name(self):
			if self.c:
				port = self.c.is_connected()
				if port:
					try:
						return port.port.name
					except:
						pass
				return None

		def get_sensors(self):
			sensors = []
			if self.c:
				sensors = self.c.getSupportedSensorList()
			return sensors

	obd = OBDPort()