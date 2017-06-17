#!/usr/bin/env python
import time
import serial
from pynmea import nmea
import subprocess

def getNetworks():
    networks = []
    proc = subprocess.Popen('sudo iwlist wlan0 scan', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    
    iwlist_result = proc.stdout.read()
    iwlist_result = iwlist_result.split("wlan0     Scan completed :\n")[1]
    iwlist_result = iwlist_result.split("Cell ")
    iwlist_result.pop(0)

    for wifi in iwlist_result:
        address_start = wifi.index("Address: ")
        address_end = wifi.index("\n",address_start)

        strength_start = wifi.index("Signal level=")
        strength_end = wifi.index("dBm",strength_start)
        
        quality_start = wifi.index("Quality=")
        quality_end = strength_start

        networks.append([wifi[address_start:address_end],wifi[strength_start:strength_end],wifi[quality_start:quality_end]])
    return networks


data_pairs = []

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
    line=ser.readline()
    if (line.startswith('$GPGGA')):
        gpgga.parse(line)
        coordinates = [gpgga.latitude,gpgga.longitude,gpgga.antenna_altitude]
        networks = getNetworks()
        data_pairs.append([coordinates,networks])
        print [coordinates,networks]
        time.sleep(5)
        
    



