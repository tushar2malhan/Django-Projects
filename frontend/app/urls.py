
from django.urls import path
# from .views import  (Posts )
from .views import  *
from django.http.response import HttpResponse,JsonResponse
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', base, name='home'),                        
    path('profile/', login_required(profile), name='profile'),
    
    path('posts/', posts, name='posts'),
    path('posts/<int:pk>', posts, name='posts'),
    path('register/', registerView, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('update/<int:pk>', update, name='update'),
    path('delete/<int:pk>', delete, name='delete'),
    ]
