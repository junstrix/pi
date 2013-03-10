# -*- coding: utf-8 -*-

from snsapi.snspocket import SNSPocket
from datetime import datetime
import time

sp = SNSPocket()
sp.load_config()
sp.auth()

while True:
    h, m = datetime.now().hour, datetime.now().minute
    if h == 22 and m == 50:
		t = '%s:%s, Pi要关机睡觉了，Goodnight everyone!' % (h,m)
	        print t
        # SNSAPI use unicode internally
	        sp.update(t.decode('utf-8'))
    if h == 6 and m == 10:
		t = '%s:%s, Pi 起床工作了哦，大家也起来吧，效率每一天，不要忘记梦想哦，Goodmorning everyong!' % (h,m)
		print t
		sp.update(t.decode('utf-8'))
    time.sleep(60)
