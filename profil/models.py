from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nom=models.CharField(max_length=200 ,null=True,)
    siyati=models.CharField(max_length=200, null=True)
    email=models.EmailField(max_length=100, null=True)
    telefon=models.CharField(max_length=40, null=True, blank=True)
    foto=models.ImageField(upload_to='my_picture/', blank=True, null=True)


    def __str__(self):
        return str(self.nom)
    


class Kategori(models.Model):
    kate=(
        ('design','design'),
         ('food','food'),
         ('education','education'),
         ('energy','energy'),
         ('technology','technology'),
         ('programming','programming'),
         ('health','health'),
         ('finance','finance'),
         ('money','money') 
    )
    nom=models.CharField(max_length=150, choices=kate)
    def __str__(self):
        return self.nom
