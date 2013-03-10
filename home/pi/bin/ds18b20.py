#! /usr/bin/python
import serial
import time
serialport = '/dev/ttyACM0'
baudrate = 9600
f = open('temp.txt','w')
s = serial.Serial(serialport, baudrate)
s.flushInput()
data = s.readline()
time.sleep(0.1)
data = s.readline().split()[0]
f.write(data)
f.close()
s.close()
exit()

#import mechanize
#import time
#import json
#
#class PachubeFeedUpdate:
#    _url_base = "http://api.cosm.com/v2/feeds/"
#    _feed_id = None
#    _version = None
#    _data = None
#    _payload = None
#    _opener = None
#    
#    def __init__(self, feed_id, apikey):
#        self._feed_id = feed_id
#        self._apikey = apikey
#        self._version = "1.0.0"
#        self._opener = mechanize.build_opener()
#        self._opener.addheaders = [('X-Apikey',apikey)]
#        self._data = []
#        self._payload = {}
#
#    def addDatapoint(self,dp_id,dp_value):
#        self._data.append({'id':dp_id, 'current_value':dp_value})
#
#    def buildUpdate(self):
#        self._payload['version'] = self._version
#        self._payload['id'] = self._feed_id
#        self._payload['datastreams'] = self._data
#
#    def sendUpdate(self):
#        url = self._url_base + self._feed_id + "?_method=put"
#        print url
#        print json.dumps(self._payload)
#        try:
#            self._opener.open(url,json.dumps(self._payload))
#        except mechanize.HTTPError as e:
#            print "An HTTP Error occurred: %s " % e
#if __name__ == '__main__':
#    import serial
#    
#    cosmkey = "oXsirKpAjZwkkZNzuZ_tAdDnDTeSAKxyVzgyYTFnWC9DRT0g"
#    cosm_feed_id = "117008"
#    serialport = '/dev/ttyACM0'
#    baudrate = 9600
#    pfu = PachubeFeedUpdate(cosm_feed_id, cosmkey)
#    s = serial.Serial(serialport, baudrate)
#    s.flushInput()
#    data = s.readline()
#    time.sleep(0.1)
#    data = s.readline().split()[0]
#    pfu.addDatapoint('ds18b20', data)
#    pfu.buildUpdate()
#    pfu.sendUpdate()
#    s.close()
#    exit()
