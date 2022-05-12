import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Pokemon
from django.core import serializers
# Create your views here.

def index(request):
    if request.method == 'GET':
        print(request.body)
        data = list(Pokemon.objects.values())
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        gh = Pokemon(name=body['name'], type=body['type'])
        gh.save()
        lastOne = list(Pokemon.objects.values())[-1]
        return JsonResponse(lastOne, safe=False)


def show(request, id):
    if request.method == 'GET':
        data = list(Pokemon.objects.filter(pk=id).values())
        print(data)
        return JsonResponse(data, safe=False)
    elif request.method == 'PATCH' or request.method == 'PUT':
        data = Pokemon.objects.get(pk=id)
        request_body = json.loads(request.body.decode('utf-8'))
        data.name = request_body['name']
        data.type = request_body['type']
        data.save()
        updated_pokemon = list(Pokemon.objects.filter(pk=id).values())
        return JsonResponse(updated_pokemon, safe=False)
    elif request.method == 'DELETE':
        delete_pokemon = list(Pokemon.objects.filter(pk=id).values())
        data = Pokemon.objects.get(pk=id)
        data.delete()
        return JsonResponse(delete_pokemon, safe=False)