from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def home(req):
    return Response({'status':200,'message':'chutiya'})


