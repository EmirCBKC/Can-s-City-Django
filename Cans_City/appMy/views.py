from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def detail(request):
    return render(request, 'detail.html')

def pc(request):
    return render(request, 'pc.html')

def ps5(request):
    return render(request, 'ps5.html')

def xbox(request):
    return render(request, 'xbox.html')