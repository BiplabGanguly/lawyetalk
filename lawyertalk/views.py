from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse

@api_view()
def home(req):
    return Response({'status':200,'message':'hello'})


def data(req):
    return HttpResponse("hello")