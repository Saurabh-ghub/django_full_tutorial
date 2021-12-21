from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, login
# Create your views here.
def register(request):
    if(request.method=="POST"):
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        username=request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if(password1==password2):
            if User.objects.filter(username=username).exists():
                messages.info(request,'Useername exist')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.info(request,'email exist')
                    return redirect('register')
                else:
                    user= User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email)
                    user.save()
                    return redirect('/')
            
        else:
            messages.info(request,'password not matching')
            return redirect('register')

    else:   
        return render(request,"register.html")

def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        password=request.POST['password']
        user=authenticate(username=uname,password=password)
        if user is not None:
            login(request,user)
            return redirect('/index')
        else:
            messages.info(request,'Invalid username password')
            return redirect('login')
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/index')
