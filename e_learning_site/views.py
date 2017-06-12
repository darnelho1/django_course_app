from django.http import HttpResponse

def hello_world(req):
    return HttpResponse('Hello World')
