from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.
def say_hello(request):
    obj = {'name':'Ioana','age':18,'country':'Romania'}
           
    return JsonResponse(json.loads(json.dumps(obj)))

def say_bye(request):
    obj = {'name':'Sebi','age':23,'country':'Romania'}
           
    return JsonResponse(json.loads(json.dumps(obj)))