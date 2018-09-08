from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def index(request):
    body_u = request.body.decode('utf-8')
    body = json.loads(body_u)
    data = body['data']


    return HttpResponse(data)