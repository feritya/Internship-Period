from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from .models import Snake
from .serializers import SnakeSerializer    
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def home(request):
    api_urls = {
        'List':'/snake-list/',
        'Detail View':'/snake-detail/<str:pk>/',
        'Create':'/snake-create/',
        'Update':'/snake-update/<str:pk>/',
        'Delete':'/snake-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET', 'POST'])
def snake_list(request):
    snakes = Snake.objects.all()
    serializer = SnakeSerializer(snakes, many=True)

    return Response(serializer.data)


@api_view(['POST', 'GET'])
def snake_create(request):
    serializer = SnakeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)