from time import sleep

import sendActionsToArduino
from sendActionsToArduino import *
import GetDataFromArduino
import StringToFloat

class Actions:

    stf = StringToFloat.StringToFloat()
    SelectedWtemp = 0
    Selectedtemp = 60
    Hummitity = 0  # is current sensor data that provides hummitity
    Selectedhummitity = 60  # Will be value set on dashboard
    Powerbuttontrue = 1  # value will be set to 1 when feature is turned on in dashboard
    Powerbuttonfalse = 0  # value will be set to 1 when featur is turned of in dashboard

    def getValuesAndParseData(self):
        HummitityCounter = 0  # value will be set to determinate the current under value
        WTempCounter = 0
        TempCounter = 0

        while self.Powerbuttontrue != self.Powerbuttonfalse:
            line = GetDataFromArduino.GetData()
            self.stf.parseString(line)
            HummitityCounter = self.hummitity(self.stf, HummitityCounter)
            TempCounter = self.temp(self.stf, TempCounter)
            WTempCounter = self.watertemp(self.stf, WTempCounter)

            if HummitityCounter == 0 or TempCounter == 0 or WTempCounter == 0:
                # nothing to do
                return

            if HummitityCounter == 10 or TempCounter == 10 or WTempCounter == 10:
                sendString = "control+"
                if WTempCounter == 10:
                    WTempCounter = 0
                    print("rising Water Temp, Current Temp: ", self.stf.getWtemp(), "  ")
                    sendString = sendString + "1+"
                else:
                    sendString = sendString + "0+"

                if TempCounter == 10:
                    TempCounter = 0
                    print("rising Temp, Current Temp: ", self.stf.gettemp(), "  ")
                    sendString = sendString + "1+"
                else:
                    sendString = sendString + "0+"

                if HummitityCounter == 10:
                    HummitityCounter = 0
                    print("rising Hummidity, Current Hummidity", self.stf.gethummitity(), "  ")
                    sendString = sendString + "1"
                else:
                    sendString = sendString + "0"

                print("sending to arduino", sendString)
                sendActionsToArduino.sendCommand(sendString)
                sleep(5)
                sendActionsToArduino.sendCommand("control+0+0+0")


    def hummitity(self, stf, HummitityCounter):

        #        StringToFloat.StringToFloat()
        Hummitity = stf.gethummitity()
        if stf.gethummitity() < self.Selectedhummitity:
            HummitityCounter = HummitityCounter + 1

            # Do something

        return HummitityCounter


    def temp(self, stf, TempCounter):

        Temp = stf.gettemp()
        if stf.gettemp() < self.Selectedtemp:
            TempCounter = TempCounter + 1
            # Do something
        return TempCounter


    def watertemp(self, stf, WTempCounter):

        WTemp = stf.getWtemp()
        if stf.getWtemp() < self.SelectedWtemp:
            WTempCounter = WTempCounter + 1
            # Do something
        return WTempCounter

    def setWTemp(self, val):
        self.SelectedWtemp = val

    def setTemp(self, val):
        self.Selectedtemp = val

    def setHumidity(self, val):
        self.Selectedhummitity = val

