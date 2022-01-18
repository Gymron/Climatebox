import GetDataFromArduino


waterTemp = 00.00
temp = 00.00
hummitity = 00.00

def StringToFloat():
    line = GetDataFromArduino.GetData()
    SplittedSensordata = [float(x) for x in line.split('+') if x.strip()]
    val1, val2, val3 = [SplittedSensordata[i] for i in (0, 1, 2)]
    waterTemp = float(val1)
    temp = float(val2)
    hummitity = float(val3)