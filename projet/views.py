from django.shortcuts import render,redirect
from .models import Projet
from profil.views import konekUser ,itilizate
from profil.models import Kategori , Profile
from .forms import projetForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def acceuil(request):
    return render(request,'pwoje/acceuil.html')

def one(request,slug):
    un=Projet.objects.filter(is_delete=False).get(slug=slug)
    context={
        'un':un,

        }
    return render(request,'pwoje/unprojet.html',context)

@login_required(login_url='konekuser')
def newProje(request):

    if request.method=='POST':
            form=projetForm(data=request.POST,files=request.FILES)
            if form.is_valid():
                proje=form.save(commit=False)
                proje.user = request.user
                proje.save()
                return redirect('/')
            else:
                pass
    else:
        form=projetForm()
    context={
        'form':form
    }
    return render(request,'pwoje/kreye.html',context)

@login_required(login_url='konekuser')
def suprime(request,id ):
    referer_url=request.META.get('HTTP_REFERER','/')
    efase=Projet.objects.get(id=id)
    efase.delete()
   
    return redirect(referer_url)
        
        
    