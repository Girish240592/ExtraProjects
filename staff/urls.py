from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('token/', views.token, name='token'),
    # path('token/', views.gettokendata, name='token'),
    
]