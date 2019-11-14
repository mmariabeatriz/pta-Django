from django.db import models

# Create your models here.

class Classes(models.Model):
    nome = models.CharField(max_length=15)
    caracteristica = models.CharField(max_length=50)