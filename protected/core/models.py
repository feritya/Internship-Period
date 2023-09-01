from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    birthdate = models.DateField()
    is_protected = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    def __str__(self):
        return self.title
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    article = models.ForeignKey(Author, on_delete=models.PROTECT)
    text = models.TextField()
    def __str__(self):
        return self.title