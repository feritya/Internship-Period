from django.db import models

# Create your models here.

class Snake(models.Model):
    name = models.CharField(max_length=100)
    length = models.IntegerField()
    venomous = models.BooleanField()

    def __str__(self):
        return self.name
