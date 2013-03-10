#! /usr/bin/env python
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

# 每日一句
def English_Everyday():
    page = urllib2.urlopen("http://www.iciba.com/").read()
    start_eq = page.find('"',page.find('title=',page.find('<a onclick'))) + 1
    end_eq = page.find('"',page.find('"',page.find('title=',page.find('<a onclick')))+1)
    e_day = page[start_eq:end_eq]
    return e_day
# 每天晚安
def EveryGoodNight():
    GoodNingFile = 'mingyan.txt'
    f_mingyan = open(GoodNingFile).read()
    mingyan_lists = f_mingyan.split()
    word_mingyan = random.choice(mingyan_lists)
    mingyan_deletelist = "sed -i '/%s/d' %s" % (word_mingyan,GoodNingFile) # system command: delete a word form list
    os.system(mingyan_deletelist)
    return word_mingyan
    
# get translate from dict.youdao.com api
def Send_Weibo():
    type = 'json'
    key = '564056047'
    keyfrom = 'pirobot'
    baseurl= 'http://fanyi.youdao.com/openapi.do?keyfrom=%s&key=%s&type=data&doctype=%s&version=1.1&q='%(keyfrom,key,type)
    cet4_src = 'cet4.txt' # file to translate
    f_cet4 = open(cet4_src)
    d_cet4 = f_cet4.read()
    word_lists = d_cet4.split()
    keyword = random.choice(word_lists)
    youdaourl= ' ' + 'http://dict.youdao.com/search?le=eng&q=%s&keyfrom=dict.index' % keyword
    get_data = urllib2.urlopen(baseurl+keyword)
    data = get_data.read()
    json_data = json.loads(data)
    yinbiao_data = json_data.get('basic',[]).get('phonetic') # 音标
    num_str = len(json_data.get('basic',[]).get('explains')[:])
    if num_str == 1:
        t_update = keyword + ': ' + '[%s] ' % (yinbiao_data) + json_data.get('basic',[]).get('explains')[0] + youdaourl
    if num_str == 2:
        t_update = keyword + ': ' + '[%s] ' % (yinbiao_data) + json_data.get('basic',[]).get('explains')[0]+' ' + json_data.get('basic',[]).get('explains')[1] + youdaourl
    if num_str == 3:
        t_update = keyword + ': ' + '[%s] ' % (yinbiao_data) + json_data.get('basic',[]).get('explains')[0]+' ' + json_data.get('basic',[]).get('explains')[1] + ' ' + json_data.get('basic',[]).get('explains')[2] + youdaourl
    if num_str == 4:
        t_update = keyword + ': ' + '[%s] ' % (yinbiao_data) + json_data.get('basic',[]).get('explains')[0]+' ' + json_data.get('basic',[]).get('explains')[1] + ' ' + json_data.get('basic',[]).get('explains')[2] + ' ' + json_data.get('basic',[]).get('explains')[3] + youdaourl
    deletelist = "sed -i '/%s/d' %s" % (keyword,cet4_src) # system command: delete a word form list
    os.system(deletelist)
    return t_update

while True:
    h, m = datetime.now().hour, datetime.now().minute
#    nowtime = datetime.now().strftime('%b-%d-%y %H:%M:%S')
    if h == 22 and m == 50:
    	t = '%s 晚安,远方的星。' %(EveryGoodNight())
    	sp.update(t.decode('utf-8'))
        quit()
    if h == 6 and m == 10:
    	t = '%s 早安，璀璨。' % (English_Everyday())
    	sp.update(t.decode('utf-8'))
    if m == 0 or m == 30:
        sp.update(Send_Weibo())
    time.sleep(60)
