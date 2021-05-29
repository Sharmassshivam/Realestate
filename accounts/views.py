from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def register(request):
    if request.method== "POST":
         first_name=request.POST['first_name']
         last_name=request.POST['last_name']
         email=request.POST['email']
         username=request.POST['username']
         password=request.POST['password']
         password2=request.POST['password2']
         #if password match
         if password==password2:
              #check user name username cannot be same
              if User.objects.filter(username=username).exists():
                  #return an error will add later
                  return redirect('register')
              else:
                  if User.objects.filter(email=email).exists():
                      #cannot have more than one email will add alert later on
                      return redirect('register')
                  else:
                      user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                      print("user created")
                      auth.login(request,user)
                      user.save()
                      return redirect('login')


         else:

             return redirect('register')
             #message will connect later



    else:

        return render(request,'accounts/register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            #a message should be displayed will add later
            return redirect('login')
    else:
        return  render(request,'accounts/login.html')

    return render(request,'accounts/login.html')
def logout(request):
    return  redirect(index)
def dashboard(request):
    return render(request,'accounts/dashboard.html')