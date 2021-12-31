from django.urls import path
from .views import Ordersapiview

urlpatterns = [
    path("orders/", Ordersapiview.as_view()),
    path("orders/<int:pk>", Ordersapiview.as_view())
]


