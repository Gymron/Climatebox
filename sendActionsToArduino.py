import serial

def RiseTemp():
    if __name__ == '__main__':
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        ser.reset_input_buffer()
        ser.write(b'contro+l0+0+1')
        ser.close()


def RiseWTemp():
    if __name__ == '__main__':
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        ser.reset_input_buffer()
        ser.write(b'control+0+1+0')
        ser.close()


def RiseHummitity():
    if __name__ == '__main__':
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        ser.reset_input_buffer()
        ser.write(b'control+1+0+0')
        ser.close()

