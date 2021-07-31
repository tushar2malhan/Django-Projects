from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Mammal , Bird , Fish
import json 

@csrf_exempt
def func1(request):
    return HttpResponse('all ok lets start !')

@csrf_exempt
def mammals(request):
    if request.method == 'GET':
        f =[]
        actual=[]
        obj = Mammal.objects.all()
        for animal in obj:
            result={
                'name':animal.name,
                'species':animal.species,
                'gender':animal.gender,
                'food':animal.food}
            f.append(result)
        for i in f:
            actual.append(i['name'])
            actual.append(i['species'])
            actual.append(i['food'])
        return JsonResponse({'data' :[actual]})
    
        
    elif request.method == 'POST':
        name = request.GET['name']
        species = request.GET['species']
        gender = request.GET['gender']
        food = request.GET['food']
        get , created  = Mammal.objects.get_or_create(name=name, species=species,gender=gender,food=food)
        print('get =',get)
        print('created = ',created)
        if created:
            return JsonResponse({'created':{'name':name}})
        else:
            return HttpResponse(' Mammal already exists')



@csrf_exempt
def birds(request):
    if request.method == 'GET':
        f=[]
        actual=[]
        obj2 = Bird.objects.all()
        for bird in obj2:
            result={
                'name':bird.name,
                'species':bird.species,
                'food':bird.food}
            f.append(result)
        for i in f:
            actual.append(i['name'])
            actual.append(i['species'])
            actual.append(i['food'])
        return JsonResponse({'data' :[actual]})

    elif request.method == 'POST':
        nameo =request.GET['name']
        species2 =request.GET['species']
        food2 =request.GET['food']

        get ,crt = Bird.objects.get_or_create(name =nameo , species =species2 ,food =food2)
        if crt:
            return JsonResponse({'data' :[nameo,species2,food2]})
        else:
            return HttpResponse('already created')


@csrf_exempt
def fishes(request):
    if request.method == 'GET':
        f=[]
        actual =[]
        obj3 = Fish.objects.all()
        for fish in obj3:
            result={
                'color':fish.color,
                'species':fish.species,
                'food':fish.food}
            f.append(result)
        for i in f:
            actual.append(i['color'])
            actual.append(i['species'])
            actual.append(i['food'])
        return JsonResponse({'data' :[actual]})

    elif request.method == 'POST':
        color =request.GET['color']
        species =request.GET['species']
        food =request.GET['food']

        get ,crt = Fish.objects.get_or_create(color=color , species =species ,food =food)
        if crt:
            return JsonResponse({'data' :[color,species,food]})
        else:
            return HttpResponse('already created')
