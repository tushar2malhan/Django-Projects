from django.http.response import HttpResponse,JsonResponse
from django.urls import path
from .views import app ,indexx  , palindrome_chk 


urlpatterns=[
    path('simpleapp/', app,name='simpleapp'),
    path('simpleapp/<number>', app,name='with_string'),
    path('palindrome_check/',palindrome_chk,name='palindrome'),
    path('palindrome_check/<strr>',palindrome_chk,name='palindrome_with_string'),
    path('array_addition',indexx,name='index'),

]

