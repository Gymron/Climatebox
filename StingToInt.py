from GetDataFromArduino import line
Sensordata = "nothing in it yet"
line = Sensordata

SplittedSensordata = [int(x) for x in line.split('+') if x.strip()]

val1, val2, val3 = [SplittedSensordata[i] for i in (1, 2, 3)]
WaterTemp = float(val1)
Temp = float(val2)
Hummitiy = (val3)