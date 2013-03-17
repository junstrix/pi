from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime
import commands

def Pi_Index(request):
    now = datetime.datetime.now()
    osuptime = commands.getoutput('uptime').split(',')[0]
    sosuptime = commands.getoutput('uptime')
    oscpuinfo = commands.getoutput('cat /proc/cpuinfo')
    sosfree = commands.getoutput('free -m')
    soslogo = commands.getoutput('linuxlogo -a -u')
    return render_to_response('pi/pi.html', {'current_date': now,'os_uptime': osuptime,'os_cpuinfo': oscpuinfo,'sos_uptime': sosuptime,'sys_free':sosfree,'sys_linuxlogo': soslogo})

def hello(request):
    return HttpResponse("Hello world")
