from dataclasses import fields
from distutils.command.upload import upload
from logging import PlaceHolder
from random import choice
from django import forms
from .models import Projet


class projetForm(forms.ModelForm):
        class Meta:
            model=Projet
            fields=('categori','titre','description','foto')
            widgets={
                'categori':forms.SelectMultiple(attrs={'class':'form-control'}),
                'titre':forms.TextInput(attrs={'class':'form-control'}),
                'description':forms.Textarea(attrs={'class':'form-control'}),
                'foto':forms.FileInput(attrs={'class':'form-control'})
            }
