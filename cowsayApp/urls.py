from django.urls import path
from cowsayApp import views

urlpatterns = [
    path('', views.index, name = 'homepage'),
    path('history', views.history, name='history'),
]
