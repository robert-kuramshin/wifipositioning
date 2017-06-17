#!/usr/bin/env python
import time
import serial
from pynmea import nmea


ser = serial.Serial(
    port='/dev/serial0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

counter = 0
gpgga = nmea.GPGGA()

while 1:
    x=ser.readline()
    if (x.startswith('$GPGGA')):
         gpgga.parse(x)
         print 'Lat: ', gpgga.latitude
         print 'Long: ', gpgga.longitude
         print 'Alt: ', gpgga.antenna_altitude, ' ', gpgga.altitude_units
         print 'No of sats: ', gpgga.num_sats
        
