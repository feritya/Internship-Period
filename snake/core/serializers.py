from rest_framework import serializers
from .models import Snake

class SnakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snake
        fields = '__all__'