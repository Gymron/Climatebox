import serial


def sendCommand(cmd):
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    ser.write(cmd)
    ser.close()