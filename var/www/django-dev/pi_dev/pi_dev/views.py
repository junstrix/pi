from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime
import commands

def Pi_Index(request):
    now = datetime.datetime.now()
    osuptime = commands.getoutput('uptime').split(',')[0]
    return render_to_response('pi/pi.html', {'current_date': now,'os_uptime': osuptime})

def hello(request):
    return HttpResponse("Hello world")
