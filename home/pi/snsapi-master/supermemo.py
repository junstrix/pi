#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import json
import chardet
import random
import os
import time

i = 21
while i > 0:
    cet4_src = 'supermemo.txt' # file to translate
    supermem_english = 'supermemo.apk'
    ttype = 'json'
    key = '1081942323'
    keyfrom = 'fanmemo'
#    key = '564056047'
#    keyfrom = 'pirobot'
    baseurl= 'http://fanyi.youdao.com/openapi.do?keyfrom=%s&key=%s&type=data&doctype=%s&version=1.1&q='%(keyfrom,key,ttype)
    f_cet4 = open(cet4_src,'r')
    supermem = open(supermem_english,'a')
    d_cet4 = f_cet4.read()
    word_lists = d_cet4.split()
    keyword = random.choice(word_lists)
    youdaourl= ' ' + 'http://dict.youdao.com/search?le=eng&q=%s&keyfrom=dict.index' % keyword
    get_data = urllib2.urlopen(baseurl+keyword).read()
    json_data = json.loads(get_data)
    # yinbiao_data = json_data.get('basic',[]).get('phonetic') # 音标
    yinbiao_data = json_data.get('basic').get('phonetic') # 音标
    num_str = len(json_data.get('basic',[]).get('explains')[:])
    if num_str == 1:
        A_data = 'A: ' + json_data.get('basic',[]).get('explains')[0] + '\n'
    if num_str == 2:
        A_data = 'A: ' + json_data.get('basic',[]).get('explains')[0] +' ' + json_data.get('basic',[]).get('explains')[1] + '\n'
    if num_str == 3:
        A_data = 'A: ' + json_data.get('basic',[]).get('explains')[0] +' ' + json_data.get('basic',[]).get('explains')[1] + ' ' + json_data.get('basic',[]).get('explains')[2] + '\n'
    if num_str == 4:
        A_data = 'A: ' + json_data.get('basic',[]).get('explains')[0] +' ' + json_data.get('basic',[]).get('explains')[1] + ' ' + json_data.get('basic',[]).get('explains')[2] + ' ' + json_data.get('basic',[]).get('explains')[3] + '\n'
    Q_data = 'Q: '+ keyword + ' ' + '[%s]' % (yinbiao_data) + '\n'
    neline = '\n'
    supermem.write(Q_data.encode('utf-8'))
    supermem.write(A_data.encode('utf-8'))
    supermem.write(neline.encode('utf-8'))
    deletelist = "sed -i '/%s/d' %s" % (keyword,cet4_src) # system command: delete a word form list
    os.system(deletelist)
    supermem.close()
    f_cet4.close()
    i = i - 1
    print i
    print ' '
exit()
#    t_update = keyword + ': ' + '[%s] ' % (yinbiao_data) + json_data.get('basic',[]).get('explains')[0] + youdaourl
#if num_str == 2:
#    t_update = keyword + ': ' + '[%s] ' % (yinbiao_data) + json_data.get('basic',[]).get('explains')[0]+' ' + json_data.get('basic',[]).get('explains')[1] + youdaourl
#if num_str == 3:
#    t_update = keyword + ': ' + '[%s] ' % (yinbiao_data) + json_data.get('basic',[]).get('explains')[0]+' ' + json_data.get('basic',[]).get('explains')[1] + ' ' + json_data.get('basic',[]).get('explains')[2] + youdaourl
#if num_str == 4:
#    t_update = keyword + ': ' + '[%s] ' % (yinbiao_data) + json_data.get('basic',[]).get('explains')[0]+' ' + json_data.get('basic',[]).get('explains')[1] + ' ' + json_data.get('basic',[]).get('explains')[2] + ' ' + json_data.get('basic',[]).get('explains')[3] + youdaourl
