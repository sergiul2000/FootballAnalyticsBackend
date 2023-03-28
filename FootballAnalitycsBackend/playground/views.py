from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json
from models import Player
from rest_framework import serializers

# Create your views here.
def say_hello(request):
    obj = {'name':'Ioana','age':18,'country':'Romania'}
           
    return JsonResponse(json.loads(json.dumps(obj)))

def say_bye(request):
    obj = {'name':'Sebi','age':23,'country':'Romania'}
           
    return JsonResponse(json.loads(json.dumps(obj)))

def all_players(request):
    # print(Player.objects.all().values)
    players_json = []
    players_objects = Player.objects.values()
    # print(players_objects)
    for i in players_objects:
        player = {'id':i['id'],'name':i['name'],'position':i['position'],'height':i['height'],'weight':i['weight']}
        players_json.append(player)
        # print(i)
    response = JsonResponse(players_json,safe = False)
    return response
    # print(response)
    # jsonResponse = json.loads(response.text)
    # return JsonResponse({'player':Player.objects.all().values})
    # return HttpResponse(list_response)