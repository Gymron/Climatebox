from threading import Thread
import Actions
from Actions import hummitity
from Actions import temp



t1 = Thread(target=Actions.temp)
threads = [t1]
t2 = Thread(target=Actions.hummitity)
threads += [t2]

t1.start()
t2.start()
