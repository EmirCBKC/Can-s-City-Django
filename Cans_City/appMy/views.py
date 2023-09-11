from django.shortcuts import redirect, render
from .models import *
from django.db.models import Q
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def detail(request, id):
    game = Game.objects.get(id=id)
    deluxe = Game.objects.get(title=game.title, edition=2)
    ultimate = Game.objects.get(title=game.title, edition=3)

    context = {
        'game': game,
        'deluxe': deluxe,
        'ultimate': ultimate
    }

    return render(request, 'detail.html', context)


def pc(request):
    pc = Game.objects.filter(platform=1, edition=1)
    order_by = request.GET.get("order_by")
    query = request.GET.get("searchInput")

    if query:
        pc = pc.filter(Q(title__icontains=query)).distinct

    if order_by == "low":
        pc = pc.order_by('price')

    if order_by == "high":
        pc = pc.order_by('-price')

    context = {
        'pc': pc,
    }

    return render(request, 'pc.html', context)


def ps5(request):
    ps5 = Game.objects.filter(platform=2, edition=1)
    query = request.GET.get("searchInput")

    if query:
        ps5 = ps5.filter(Q(title__icontains=query)).distinct

    context = {
        'ps5': ps5,
    }

    return render(request, 'ps5.html', context)


def xbox(request):
    xbox = Game.objects.filter(platform=3, edition=1)
    query = request.GET.get("searchInput")

    if query:
        xbox = xbox.filter(Q(title__icontains=query)).distinct

    context = {
        'xbox': xbox,
    }

    return render(request, 'xbox.html', context)

def profile(request):
    
    return render(request,'profile.html')

def register(request):
    if request.method=="POST":
        name=request.POST["name"]
        surName=request.POST["surName"]
        userName=request.POST["userName"]
        email=request.POST["email"]
        password=request.POST["password"]
        password2=request.POST["password2"]
        
        if password==password2:
            if User.objects.filter(username=userName).exists():
                context={
                    'information':'This username is used. Try a different username!'
                }
                return render(request,'user/register.html',context)
            
            if User.objects.filter(email=email).exists():
                context={
                    'information':'This e-mail address is used. Try a different email address!'
                }
                return render(request,'user/register.html',context)
            
            else:
                user=User.objects.create_user(first_name=name,last_name=surName,username=userName,email=email,password=password)
                user.save()
                pro=Profil(user_id=user.id,profileImg=None)
                pro.save()
                return redirect('/')
        else:
            context = {
                'information':'Your password does not match the replay password you entered!'
            }
            return render(request,'user/register.html',context)
    
    return render(request,'user/register.html')

def loginn(request):
    if request.method=="POST":
        userName=request.POST["userName"]
        password=request.POST["password"]
        
        user=authenticate(request,username=userName,password=password)
        
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            context={
                'information':'The username or password you entered is incorrect, try again!'
            }
            
            return render(request,'user/login.html',context)
        
    return render(request,'user/login.html')

def logoutt(request):
    logout(request)
    
    return redirect('/')

@login_required
def profile(request):
    
    profile=Profil.objects.get(user_id=request.user)
    
    if request.method=="POST" and 'profileImg-btn' in request.POST:
        filee=request.FILES.get("image")
        
        if filee:
            profile.profileImg=filee
            profile.save()
            
            context={
                'profile':profile
            }
            
            return render(request,'profile.html',context)
    
    context={
        'profile':profile
    }
    
    return render(request,'profile.html',context)