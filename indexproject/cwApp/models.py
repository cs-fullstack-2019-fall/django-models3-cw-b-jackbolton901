from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=30)
    pageNumber = models.IntegerField()
    genre = models.CharField(max_length=20)
    publishDate = models.DateField()

