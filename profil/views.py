from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,redirect 
from projet.models import Projet
from profil.models import Profile,Kategori
from django.contrib.auth.models import User
from .forms import ProfileForm
from django.db.models import Prefetch

from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def acceuil(request):
    Lis_itilizate=User.objects.select_related('profile').prefetch_related(Prefetch ('projet_set',queryset=Projet.objects.all().order_by('date')))
    #Lis_itilizate=User.objects.select_related('profile').all()
    context={
        'Lis_itilizate':Lis_itilizate
    }
    return render(request,'user/acceuil.html',context)




def itilizate(request,id):
    user=User.objects.select_related('profile').prefetch_related(Prefetch('projet_set',queryset=Projet.objects.all())).filter(id=id)
        
    context={
        'user':user
        
    }
    return render(request,'user/itilizate.html',context)
  
def newItilizate(request):
    if request.method == 'POST':
        nom=request.POST.get('nom')
        modpas=request.POST.get('modpas')
        confirm=request.POST.get('confirm')
        if modpas != confirm:
            pass
        else:
            user=User.objects.create_user(username=nom,password=modpas)
            login(request,user)
            return redirect(acceuil)


    return render(request,'user/kont.html')


def konekUser(request):
    if request.method== 'POST':
        nom=request.POST['nom']
        modpas=request.POST['modpas']
        user=authenticate(username=nom,password=modpas)
        if user is not None:
            login (request,user)
            return redirect(acceuil)
    
    return render(request,'user/konekte.html')



def newprofil(request):
    if request.method=='POST':
        form=ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user=request.user
            profile.save()
        return redirect(acceuil)
    else:
        form= ProfileForm()

    context={
        'form':form
    }
    return render(request,'user/kreyemoun.html',context)
 


def dekonekte(request):
    logout(request)
    return redirect(acceuil)

