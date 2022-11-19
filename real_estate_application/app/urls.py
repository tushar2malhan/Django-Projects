
from django.urls import path
from .views import  *
from django.http.response import HttpResponse,JsonResponse

urlpatterns = [
    path('myhome/',lambda request:HttpResponse('Message Created By Tushar Malhan'  ) ),
    path('',view_homes ),
    path('search/<str:value>',view_homes ),
    path('sell/',sell_home ),
    path('offers/',get_offers ),
    path('sold_offers/',offers_for_sold_home ),
]
