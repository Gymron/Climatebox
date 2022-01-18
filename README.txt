# Climatebox
Little school project:

Objectives Of The Project:
	-controls the climate in a small space like a terrarium
	-monitors the values of different sensors to control the climate accordingly
	-using a connection between an Arduino and raspberry-pi

You will need:
	-some model of a raspberry-pi,
	-an Arduino (if it uses 5v logic levels, you will need a logic-level-shifter),
	-TMP36 sensor for measuring water temperature,
	-DHT11 sensor for measuring air humidity and temperature,
	-and various cables

Arduino-Pinout (Arduino Mega)
A15			TMP36 signal output
D42			DHT11 temperature/humidity sensor
D51			piezo fogger control output
D52			heating element control Ooutput
D53			heating lamp control output
D0(RX)		HV_1 on logic-level-shifter	
D1(TX)		LV_2 on logic-level-shifter
GND			HV_GND on logic-level-shifter
5V			HV_VDD on logic-level-shifter

Rapberry-Pi-Pinout (raspberry-pi 4)
GND			LV_GND on logic-level-shifter
3.3V		LV_VDD on logic-level-shifter
GPIO14(TX)	LV_1 on logic-level-shifter
GPIO15(RX)	LV_2 on logic-level-shifter

First-Use-Instructions:
	-change fail-save values inside the Arduino controller code (min/max AirTemp, AirHum and WaterTemp) accordingly to the requirements of your pets.
	-check connection of all sensors
	-connect Arduino to the raspberry-pi
	-TODO

Arduino-Features:
	-serial communication (9600 Baud) over USB or serial pins(read note below)
	-send "data" to get a string in the following format, seperated by "+": watertemperature+airtemperature+airhumidity
	-send "debug" to get the current values as human-readable strings
	-send "control" to control the three outputs in the following way: "control+PIEZOFOGGER+HEATINGELEMENT+HEATINGLAMP".
		Replace capitalized words with "0" or "1" instead of the placeholders to turn the outputs off or on.
	-error-handling
		-will output error messages in the following format: "error+ERRORMESSAGE"
		-will output "error+errorcount_" followed by the total number of errors after all error messages

	Important Note: serial over Arduino Pins D0/D1 might require the following fix (tested on Arduino Mega 2560):
		-hardware modification on the RESET_EN solder-pads
		-cut the small trace between the pads to fix the otherwise not working serial connection
		-you will need to reconnect the pads for flashing a software update onto the Arduino
		-we recommend to solder a jumper or switch onto the two solder-pads
		
		-circuit diagram of the logic-level-shifter and corresponding CAD-files are located in the LLS_Diagram folder

Rapberry-Pi-Features:
	-TODO

Descripton Of Files:
	-LLC_diagram		Logic Level Converter circuit
	-Project.ino		Arduino controller program
	-TODO