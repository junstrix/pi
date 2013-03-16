from django.http import HttpResponse
import datetime

def current_datetime(request):
    """docstring for current_datetime"""
    now = datetime.datetime.now()
    html = "<html><body>Now time is : %s.</body></html>" % now
    return HttpResponse(html)
