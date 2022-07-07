
from django.urls import path
from .views import  (interaction )
from django.http.response import HttpResponse,JsonResponse

urlpatterns = [
    path('get/', lambda request:HttpResponse('Test' )),                        
    path('<int:number>',interaction)       ,                
    path('home/',lambda request:HttpResponse('Message Created By Tushar Malhan ' ) )
    ]
