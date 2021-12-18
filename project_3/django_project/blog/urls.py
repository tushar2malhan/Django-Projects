from django.urls import path
# from .views import (
#     PostListView,
#     PostDetailView,
#     PostCreateView,
#     PostUpdateView,
#     PostDeleteView
# )
from . import views

app_name= "blog"



urlpatterns = [
    
    path('', views.main, name='blog-home'),
    path('polls/', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
