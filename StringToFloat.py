import GetDataFromArduino
from GetDataFromArduino import *

#Sensordata = "nothing in it yet"
temp = 00.00
waterTemp = 00.00
hummitity = 00.00


def StringToFloat():
    line = GetDataFromArduino.Sensordata
    SplittedSensordata = [int(x) for x in line.split('+') if x.strip()]
    val1, val2, val3 = [SplittedSensordata[i] for i in (1, 2, 3)]
    waterTemp = float(val1)
    temp = float(val2)
    hummitiy = float(val3)