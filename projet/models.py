from django.db import models
from profil.models import Kategori ,Profile
from django.utils.text import slugify
import random
from django.contrib.auth.models import User
# Create your models here

class Projet(models.Model):
    categori=models.ManyToManyField(Kategori ,blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    slug=models.SlugField(max_length=200,unique=True)
    titre=models.CharField(max_length=200, blank=True, null=True)
    description=models.TextField(max_length=5000, blank=True)
    date=models.DateTimeField(auto_now_add=True)
    foto=models.ImageField(upload_to='image/',blank=True)
    is_delete=models.BooleanField(default=False)

    def save(self, *args,**kwargs) :
        if self.pk is None:
            slug_m= slugify(self.titre)
            while Projet.objects.filter(slug=slug_m):
                slug_m+=str(random.randrange(1,2500))
            self.slug=slug_m
        super(Projet,self).save(args,kwargs)

    def __str__(self):
        return self.titre
