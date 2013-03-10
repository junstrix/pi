# -*- coding: utf-8 -*-

import urllib2
import json
import chardet
import random
import os
import snsapi
import time
from snsapi.snspocket import SNSPocket
from datetime import datetime

# social auth with snsapi
sp = SNSPocket()
sp.load_config()
sp.auth()

# youdao translation
type = 'json'
key = '564056047'
keyfrom = 'pirobot'
baseurl= 'http://fanyi.youdao.com/openapi.do?keyfrom=%s&key=%s&type=data&doctype=%s&version=1.1&q='%(keyfrom,key,type)
cet4_src = 'cet4.txt' # file to translate
f_cet4 = open(cet4_src)
d_cet4 = f_cet4.read()
word_lists = d_cet4.split()
keyword = random.choice(word_lists)
youdaourl= 'http://dict.youdao.com/search?le=eng&q=%s&keyfrom=dict.index' % keyword
print keyword
get_data = urllib2.urlopen(baseurl+keyword)
data = get_data.read()
json_data = json.loads(data)
deletelist = "sed -i '/%s/d' %s" % (keyword,cet4_src) # system command: delete a word form list
os.system(deletelist)
num_str = len(json_data.get('basic',[]).get('explains')[:])
if num_str == 1:
    t_update = json_data.get('basic',[]).get('explains')[0]
if num_str == 2:
    t_update = json_data.get('basic',[]).get('explains')[0]+' ' + json_data.get('basic',[]).get('explains')[1]
if num_str == 3:
    t_update = json_data.get('basic',[]).get('explains')[0]+' ' + json_data.get('basic',[]).get('explains')[1] + ' ' + json_data.get('basic',[]).get('explains')[2]
if num_str == 4:
    t_update = json_data.get('basic',[]).get('explains')[0]+' ' + json_data.get('basic',[]).get('explains')[1] + ' ' + json_data.get('basic',[]).get('explains')[2] + ' ' + json_data.get('basic',[]).get('explains')[3]

while True:
    h, m = datetime.now().hour, datetime.now().minute
    if h == 22 and m == 50:
		t = '%s:%s, Pi要关机睡觉了，Goodnight everyone!' % (h,m)
        # SNSAPI use unicode internally
		sp.update(t.decode('utf-8'))
    if h == 6 and m == 10:
		t = '%s:%s, Pi 起床工作了哦，大家也起来吧，效率每一天，不要忘记梦想哦，Goodmorning everyong! http://junstrix.oicp.net' % (h,m)
    if m == 20:
        sp.update(t_update.decode('utf-8'))
    time.sleep(60)
