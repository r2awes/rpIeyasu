# rpIeyasu
A digital dash built with a Raspberry Pi Zero W, 3 i2c oled displays, a ramshackle voltage divider, and a 2001 Toyota MR2. And now @pbartek 's PyOBD package.

## Pinouts
* Left Display
	* GND
	* VCC
	* SCL
	* SDA
* Middle Display
	* GND
	* VCC
	* SCL
	* SDA
* Right Display
	* GND
	* VCC
	* SCL
	* SDA
* RPM Reader
	* OBD
* Speed Reader
	* OBD
* Fuel Reader
	* READ
	* GND

##Notes

Must use a version with debian with a desktop, otherwise no bluetooth connections.

Also uses Adafruit's Adafruit_SSD1306 python library, so make sure that is installed properly.