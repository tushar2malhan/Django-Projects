
from django.urls import path
from .views import  (interaction )
from django.http.response import HttpResponse,JsonResponse

urlpatterns = [
    path('', interaction),
    path('get/', lambda request:HttpResponse('Test' )),                        
    path('post/<username>',interaction),                        
    path('home/',lambda request:HttpResponse('Message Created By Tushar Malhan ' ) )
    ]
