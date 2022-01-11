from time import sleep
from pitop import Pitop
import ray

Temp = 0
Selectedtemp = 60
TempCounter = 0
Hummitity = 0  # is current sensor data that provides hummitity
Selectedhummitity = 60  # Will be value set on dashboard
Powerbuttontrue = 1  # value will be set to 1 when feature is turned on in dashboard
Powerbuttonfalse = 0  # value will be set to 1 when featur is turned of in dashboard
HummitityCounter = 0  # value will be set to determinate the current under value

def hummitity():
    Hummitity = 0
    Selectedhummitity = 60
    HummitityCounter = 0

    while Powerbuttontrue > Powerbuttonfalse:
        if Hummitity < Selectedhummitity:
            HummitityCounter = HummitityCounter + 1
            if HummitityCounter == 10:
                HummitityCounter = 0
                print("rising Hummidity, Current Hummidity", Hummitity,"  ")
                pitop.miniscreen.display_text("Current Hummitity")
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

