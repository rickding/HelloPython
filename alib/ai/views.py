from django.core.management import call_command
from django.http import HttpResponse


def chk(request):
    return HttpResponse("ok, ai")


def ai(request):
    return HttpResponse('ai: %s' % call_command('change_pic'))
