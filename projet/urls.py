from django.urls import path
from . import views
urlpatterns = [
    path('',views.acceuil ,name='acceuil'),
    path('yonproje/<str:slug>',views.one,name='youn'),
    path('kreyee',views.newProje, name='kreyee'),
    path('delete/<int:id>',views.suprime,name='delete')
]