import serial

line = "18.36+22.00+35.00"


def GetData():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    ser.write(b'data')
    ser.close()
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        with open('readme.txt', 'w') as f:
            f.write("current SensorData:", line)
    return line
