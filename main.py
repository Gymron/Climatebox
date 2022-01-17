from threading import Thread
import Actions
from Actions import hummitity
from GetDataFromArduino import *

t1 = Thread(target=Actions.temp)
threads = [t1]
t2 = Thread(target=Actions.hummitity)
threads += [t2]
t3 = Thread(target=Actions.watertemp)

t1.start()
t2.start()
t3.Start()


