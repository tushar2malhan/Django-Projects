from django.urls import path
from .views import Productapiview

urlpatterns = [
    path("products/", Productapiview.as_view()),
    path("products/<int:pk>", Productapiview.as_view())
]