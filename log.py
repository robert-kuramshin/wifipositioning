import subprocess
import re

proc = subprocess.Popen('sudo iwlist wlan0 scan', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
tmp = proc.stdout.read()

tmp = tmp.split("wlan0     Scan completed :\n")[1]
tmp = tmp.split("Cell ")
tmp.pop(0)

for wifi in tmp:
    address_start = wifi.index("Address: ")
    address_end = wifi.index("\n",address_start)

    strength_start = wifi.index("Signal level=")
    strength_end = wifi.index("dBm",strength_start)
    
    quality_start = wifi.index("Quality=")
    quality_end = strength_start

    print wifi[address_start:address_end]
    print wifi[strength_start:strength_end]
    print wifi[quality_start:quality_end]
    
