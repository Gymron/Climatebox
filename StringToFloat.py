import GetDataFromArduino

class StringToFloat:

    waterTemp = 00.00
    temp = 00.00
    hummitity = 00.00

    def parseString(self, line):
        SplittedSensordata = [float(x) for x in line.split('+') if x.strip()]
        val1, val2, val3 = [SplittedSensordata[i] for i in (0, 1, 2)]
        self.waterTemp = float(val1)
        self.temp = float(val2)
        self.hummitity = float(val3)

    def getWtemp(self):
        return self.waterTemp

    def gettemp(self):
        return self.temp

    def gethummitity(self):
        return self.hummitity
