from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.shop),
    path('jeju/', views.jeju),
]