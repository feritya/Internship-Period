from django.urls import path
from . import views

urlpatterns = [
    path('/', views.home, name='home'),  
    path('snake_list', views.snake_list, name='snake_list'),  
    path('snake_create', views.snake_create, name='snake_create'),

]

