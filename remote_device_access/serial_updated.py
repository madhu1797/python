import serial
import time
ser = serial.Serial('/dev/ttyUSB0',  timeout=30)         # check which port was really used
ser.write(b'show version')     # write a string


line = ser.readline()

print(line)
"""

time.sleep(5)

result = ser.read(100)
print(result)

"""
ser.close()     
