from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Mammal , Bird , Fish
import json 

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view,permission_classes
# from rest_framework.permissions import IsAuthenticated

@csrf_exempt
def func1(request):
    return HttpResponse('all ok lets start !')

# @csrf_exempt
@api_view(['GET','POST','DELETE','PUT'])
def mammals(request,name=None):
    if request.method == 'GET':
        if name:
            obj2 = Mammal.objects.filter(name=name)
            print(obj2)
            for animal in obj2:
                result={
                    'name':animal.name,
                    'species':animal.species,
                    'gender':animal.gender,
                    'food':animal.food,
                    'last_feed':animal.last_feed}
                return Response(result)
        f =[]
        actual=[]
        obj = Mammal.objects.all()
        for animal in obj:
            result={
                'name':animal.name,
                'species':animal.species,
                'gender':animal.gender,
                'food':animal.food,
                'last_feed':animal.last_feed}
            f.append(result)

        for i in f:
            actual.append(i['name'])
            actual.append(i['species'])
            actual.append(i['food'])
            actual.append(i['last_feed'])
        return JsonResponse({'data' : actual })
    
        
    elif request.method == 'POST':
        name = request.GET['name']
        species = request.GET['species']
        gender = request.GET['gender']
        food = request.GET['food']
        get , created  = Mammal.objects.get_or_create(name=name, species=species,gender=gender,food=food)
   
        if created:
            return JsonResponse({'created':{'name':name}})
        else:
            return HttpResponse(' Mammal already exists')

    elif request.method == 'PUT':
        obj = Mammal.objects.all()

        for animal in obj:
            animal.name = request.GET['name']    # here name is Primary key  , if name is same then it changes else , it POST requests
            animal.species = request.GET['species']
            animal.gender = request.GET['gender']
            animal.food = request.GET['food']
            animal.last_feed= request.GET['last_feed']
            animal.save()

        return Response('PUT called and objects changed')
    
    elif request.method == 'DELETE':
        try:
            name = request.GET['name']
            mammals = Mammal.objects.get(name=name)
            # print(mammals)
            mammals.delete()
            return Response('mammal delete')
        except:
            return Response('mammal name not found')


@api_view(['GET','POST','DELETE','PUT'])
def birds(request,name=None):
    if request.method == 'GET':
        if name :
            obj2 = Bird.objects.filter(name=name)
            print(obj2)
            for birds in obj2:
                result={
                    'name':birds.name,
                    'species':birds.species,
                    'food':birds.food,
                    'last_feed':birds.last_feed}
                return Response(result)
        f=[]
        actual=[]
        obj2 = Bird.objects.all()
        for bird in obj2:
            result={
                'name':bird.name,
                'species':bird.species,
                'food':bird.food,
                'last_feed':bird.last_feed}
            
            f.append(result)
        for i in f:
            actual.append(i['name'])
            actual.append(i['species'])
            actual.append(i['food'])
            actual.append(i['last_feed'])
        return Response({'data' :[actual]})

    elif request.method == 'POST':
        nameo =request.GET['name']
        species2 =request.GET['species']
        food2 =request.GET['food']

        get ,crt = Bird.objects.get_or_create(name =nameo , species =species2 ,food =food2)
        if crt:
            return JsonResponse({'data' :[nameo,species2,food2]})
        else:
            return HttpResponse('already created')

    
    elif request.method == 'PUT':
        obj = Bird.objects.all()

        for bird in obj:
            bird.name = request.GET['name']               # here name is Primary key  , if name is same then it changes else , it POST requests
            bird.species = request.GET['species']
            bird.food = request.GET['food']
            bird.last_feed= request.GET['last_feed']
            bird.save()

        return Response('PUT called and objects changed')
    
    elif request.method == 'DELETE':
        try:
            name = request.GET['name']
            Birds = Bird.objects.get(name=name)
        
            Birds.delete()
            return Response('Bird delete')
        except:
            return Response('Bird name not found')


@api_view(['GET','POST','DELETE','PUT'])
def fishes(request,species=None):
    if request.method == 'GET':
        if species:
            # print(species)
            obj2 = Fish.objects.filter(species=species)
            # print(obj2)
            for animal in obj2:
                result={
                    'species':animal.species,
                    'food':animal.food,
                    'last_feed':animal.last_feed,
                    'count':animal.count}
                return Response(result)

        f=[]
        actual =[]
        obj3 = Fish.objects.all()
        # print(obj3)
        for fish in obj3:
            result={
                'color':fish.color,
                'species':fish.species,
                'food':fish.food
                }
            f.append(result)
        for i in f:
            actual.append(i['color'])
            actual.append(i['species'])
            actual.append(i['food'])
            actual.append('')
        return Response({'data' :actual})

    elif request.method == 'POST':
        color =request.GET['color']
        species =request.GET['species']
        food =request.GET['food']

        get ,crt = Fish.objects.get_or_create(color=color , species =species ,food =food)
        if crt:
            return JsonResponse({'data' :[color,species,food]})
        else:
            return HttpResponse('already created')

    elif request.method == 'PUT':
            obj = Fish.objects.all()
            for animal in obj:
          # here species is Primary key  , if name is same then it changes else , it POST requests
                    animal.species = request.GET['species']
                    animal.food = request.GET['food']
                    animal.last_feed= request.GET['last_feed']
                    animal.count= request.GET['count']
                    animal.save()
               
            return Response('PUT called and objects changed')

    
    elif request.method == 'DELETE':
        try:
            species = request.GET['species']
            fish = Fish.objects.get(species=species)
            fish.delete()
            return Response('Fish delete')
        except:
            return Response('Fish speices not found')
