import email
from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import storefront_db,MyUser
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()

class DetailView(DetailView):
        model = storefront_db


def homepage(request):
    cards = storefront_db.objects.all()
    return render(request,'homepage.html',{'cards': cards})

def logout(request):
    auth.logout(request)
    return redirect("/")


def register(request):

    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(email = email).exists():
            messages.info(request,'email taken')
            return redirect('create-account.html')
        else:
            user = User.objects.create_user(email,password1)
            user.save();
            print("user created")
            return redirect('login.html')
        
    else:
        return render(request, 'create-account.html')



def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(email=email,password=password)
        if user is not None:
            messages.success(request,"welcome", user)
            auth.login(request,user)
            return redirect("homepage.html")
        else:
            messages.info(request,'Invalid credentials')
            return redirect("homepage.html")
    else:
        return render(request,'login.html')