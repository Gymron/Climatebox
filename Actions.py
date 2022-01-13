from time import sleep
import ray

import StingToInt
from StingToInt import *
WTemp = StingToInt.WaterTemp
SelectedWtemp = 0
WTempCounter = 0
Temp = StingToInt.Temp
Selectedtemp = 60
TempCounter = 0
Hummitity = StingToInt.Hummitiy  # is current sensor data that provides hummitity
Selectedhummitity = 60  # Will be value set on dashboard
Powerbuttontrue = 1  # value will be set to 1 when feature is turned on in dashboard
Powerbuttonfalse = 0  # value will be set to 1 when featur is turned of in dashboard
HummitityCounter = 0  # value will be set to determinate the current under value

def hummitity():
    Hummitity = 0
    Selectedhummitity = 60
    HummitityCounter = 0

    while Powerbuttontrue != Powerbuttonfalse:
        if Hummitity < Selectedhummitity:
            HummitityCounter = HummitityCounter + 1
            if HummitityCounter == 10:
                HummitityCounter = 0
                print("rising Hummidity, Current Hummidity", Hummitity,"  ")
            # Do something
            sleep(1.5)
def temp():
    Temp = 0
    Selectedtemp = 60
    TempCounter = 0
    while Powerbuttontrue > Powerbuttonfalse:
        if Temp < Selectedtemp:
            TempCounter = TempCounter + 1
            if TempCounter == 10:
                TempCounter = 0
                print("rising Temp, Current Temp: ",Temp,"  ")
            # Do something
            sleep(2)
def watertemp():
    WTemp = 0
    SelectedWtemp = 60
    WTempCounter = 0
    while Powerbuttontrue > Powerbuttonfalse:
        if WTemp < SelectedWtemp:
            WTempCounter = WTempCounter + 1
            if WTempCounter == 10:
                WTempCounter = 0
                print("rising Water Temp, Current Temp: ",WTemp,"  ")
            # Do something
            sleep(2)
