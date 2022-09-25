from django.urls import path
from . import views
urlpatterns = [
    path('',views.acceuil ,name='aceuil'),
    path('onProfile/<int:id>',views.itilizate, name='onprofile'),
    path('create/',views.newItilizate,name='create'),
    path('dekonekte/',views.dekonekte,name='dekonekte'),
    path('newprofil/',views.newprofil,name='newprofil'),
    path('konekuser/',views.konekUser,name='konekuser'),
    
    

]