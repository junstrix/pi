#! /usr/bin/python
import serial
import time
import json
import os

cosm_data = {'datastreams': [{'id': 'ds18b20', 'current_value': 'value'}]}
serialport = '/dev/ttyACM0'
baudrate = 9600
f = open('ds18b20.json', 'w')
s = serial.Serial(serialport, baudrate)
s.flushInput()
data = s.readline()
time.sleep(0.1)
data = s.readline().split()[0]
cosm_data['datastreams'][0]['current_value'] = data
f.write(json.dumps(cosm_data))
f.close()
send_cosm = 'curl --request PUT --data-binary @ds18b20.json --header "X-ApiKey: oXsirKpAjZwkkZNzuZ_tAdDnDTeSAKxyVzgyYTFnWC9DRT0g" http://api.cosm.com/v2/feeds/117008?timezone=+8'
os.system(send_cosm)
s.close()
exit()
