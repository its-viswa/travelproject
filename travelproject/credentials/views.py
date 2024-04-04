from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def login(request):
      if request.method =='POST':
          username=request.POST['username']
          password=request.POST['password']
          user=auth.authenticate(request,username=username,password=password)
          if user is not None:
              auth.login(request,user)
              return redirect('/')
          else:
              messages.info(request,"invalid login")
              return redirect('login')
      return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def register(request):
     if request.method == "POST":
        username = request.POST["username"]
        firstname = request.POST["first_name"]
        lastname = request.POST["last_name"]
        password = request.POST["password"]
        email = request.POST["email"]
        cpassword = request.POST["password1"]
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "user name already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,password=password, email=email)
                user.save();
                return redirect('login')
        else:
                messages.info(request, "password not matched")
                return redirect('register')
     return render(request, 'register.html')

