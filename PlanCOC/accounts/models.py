from django.db import models

class Category (models.Model):
    name =models.CharField(max_length=50)
    slug = models.SlugField(max_length=200)
    affichage =models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name# Create your models here.
