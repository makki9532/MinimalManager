import json
from django.core.serializers import serialize


def getBody(request):
    """ Requests are sent as byte code. This function 
    converts a request body from byte code to unicode 
    and finally to json"""
    unicode = request.body.decode('utf-8')
    return json.loads(unicode)
    
