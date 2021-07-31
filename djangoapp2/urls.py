from django.http import HttpResponse
from django.urls import path
from .views import func1 , mammals , birds , fishes

urlpatterns =[
    path('',func1 , name='APP'),
    path('mammals/',mammals),
    path('mammals/<str:name>',mammals),
    path('birds/',birds),
    path('birds/<str:name>',birds),
    path('fishes/',fishes),
    path('fishes/<str:species>',fishes)
]


'''
Run makeMigrations command
Finally, run migrate command to create tables in the database
Create views to Get and POST Data for Mammals, Bird, Fish Models Hint: Use ORM
For Views and Urls More Details are given below


'''