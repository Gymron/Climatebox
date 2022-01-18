import serial


def RiseTemp():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    ser.write(b'control+0+0+1')
    ser.close()


def RiseWTemp():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    ser.write(b'control+0+1+0')
    ser.close()


def RiseHummitity():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    ser.write(b'control+1+0+0')
    ser.close()