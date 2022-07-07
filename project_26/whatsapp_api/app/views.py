
# Imported almost everything , create your view accordingly , if anything missed kindly add it manually
import pywhatkit
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from requests import api
import json,time,pyautogui,sys

from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User          # get all the users  in ur account 

from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework. parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token             # just like User table we import the Token table 
from rest_framework.generics import ListAPIView
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login (request):
    # if request.method == 'POST':
        data = JSONParser().parse(request)
        username =data['username']
        password = data['password']
        user = User.objects.get(username=username)
        if user.check_password(password):
            token, obj=Token.objects.get_or_create(user=user)       # if user is right , we create token by passing this user object
            print(token , obj)
            return Response({'message':f'Login successful {username} ','token':token.key})
        else:
            return Response({'message':'Login unsuccessful'})

@api_view(('GET',))
def interaction(request,number=None):
    if request.method == 'GET':
        print(number)
        if len(str(number)) < 10 or len(str(number) ) > 10:
            return Response({'message':'Please enter valid number'})
        number = "+91"+str(number)
        pywhatkit.sendwhatmsg_instantly(number,'Hello')
        pyautogui.press('enter')
        return Response(f' Whatsappp message sent to this number  {number} ')

