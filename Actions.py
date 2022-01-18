from time import sleep

import sendActionsToArduino
from sendActionsToArduino import *
import GetDataFromArduino
import StringToFloat

SelectedWtemp = 0
Selectedtemp = 60
Hummitity = 0  # is current sensor data that provides hummitity
Selectedhummitity = 60  # Will be value set on dashboard
Powerbuttontrue = 1  # value will be set to 1 when feature is turned on in dashboard
Powerbuttonfalse = 0  # value will be set to 1 when featur is turned of in dashboard


def getValuesAndParseData():
    HummitityCounter = 0  # value will be set to determinate the current under value
    WTempCounter = 0
    TempCounter = 0

    while Powerbuttontrue != Powerbuttonfalse:
        stf = StringToFloat.StringToFloat()
        line = GetDataFromArduino.GetData()
        stf.parseString(line)
        HummitityCounter = hummitity(stf, HummitityCounter)
        TempCounter = temp(stf, TempCounter)
        WTempCounter = watertemp(stf, WTempCounter)
        if HummitityCounter == 10 or TempCounter == 10 or WTempCounter == 10:
            sendString = "b'control+"
            if WTempCounter == 10:
                WTempCounter = 0
                print("rising Water Temp, Current Temp: ", stf.getWtemp(), "  ")
                sendString = sendString + "1+"
            else:
                sendString = sendString + "0+"

            if TempCounter == 10:
                TempCounter = 0
                print("rising Temp, Current Temp: ", stf.gettemp(), "  ")
                sendString = sendString + "1+"
            else:
                sendString = sendString + "0+"

            if HummitityCounter == 10:
                HummitityCounter = 0
                print("rising Hummidity, Current Hummidity", stf.gethummitity(), "  ")
                sendString = sendString + "1"
            else:
                sendString = sendString + "0"

            sendActionsToArduino.sendCommand(sendString)
            sleep(5)
            sendActionsToArduino.sendCommand("b'control+0+0+0")


def hummitity(stf, HummitityCounter):
    Selectedhummitity = 60

    #        StringToFloat.StringToFloat()
    Hummitity = stf.gethummitity()
    if stf.gethummitity() < Selectedhummitity:
        HummitityCounter = HummitityCounter + 1

        # Do something

    return HummitityCounter


def temp(stf, TempCounter):
    Selectedtemp = 60

    Temp = stf.gettemp()
    if stf.gettemp() < Selectedtemp:
        TempCounter = TempCounter + 1
        # Do something
    return TempCounter


def watertemp(stf, WTempCounter):
    SelectedWtemp = 60

    WTemp = stf.getWtemp()
    if stf.getWtemp() < SelectedWtemp:
        WTempCounter = WTempCounter + 1
        # Do something
    return WTempCounter
