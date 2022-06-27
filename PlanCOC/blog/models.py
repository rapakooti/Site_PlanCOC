import re
from unicodedata import name
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


#classe pour gerer les articules en corbeille
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='publier')


# creation des catégory
class Category (models.Model):
    name =models.CharField(max_length=50)
    slug = models.SlugField(max_length=200)
    affichage =models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name


# Create your models here.
class PostPlan(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="Category_post")
    STATUS_CHOICES = (
        ('attente', 'Attente'),
        ('publier', 'publier'),
    )
 

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    adresse = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    Description = models.TextField()
    nb_affichage = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)
    niveau = models.CharField(max_length=10)
    status = models.CharField(choices=STATUS_CHOICES,
                              default='attente', max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    publication = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='posted')
    objects = models.Manager() #manager par default
    published=PublishedManager() #custom manager
    def __str__(self) -> str:
        return self.title
    def get_absolute_url(self):
        return reverse("Detail_Plan", args=[self.publication.year, self.publication.month, self.publication.day,self.slug])


class comment(models.Model):
    post =models.ForeignKey(PostPlan, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=100)
    email =  models.EmailField(max_length=200)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
       return self.post.title
