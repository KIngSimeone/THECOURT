from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'thecourt/index.html')

def signup(request):
    return render(request,'thecourt/signup.html')

def login(request):
    return render(request,'thecourt/login.html')

def chat(request):
    return render(request,'thecourt/chat.html')

def profile(request):
    return render(request,'thecourt/profile.html')