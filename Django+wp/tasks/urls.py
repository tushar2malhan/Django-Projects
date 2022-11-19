from django.urls import path
from . import views

app_name = 'app'


urlpatterns = [
    path('app/', views.index, name="list"),
    path('update_task/<str:pk>', views.updatetask, name="update_task"),
    path('delete/<str:pk>', views.deletetask, name="delete"),
    path('', views.homepage, name="homepage"),
    


]
