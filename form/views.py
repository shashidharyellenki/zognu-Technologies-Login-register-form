from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name= request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password2']

        if password == password1: 
            if User.objects.filter(username=username).exists():
                return render(request, './pages/error.html')
            else:
                if User.objects.filter(email=email).exists(): #sai -> chand sir #sai->shashi
                    return render(request, './pages/error.html')
                else:
                    user= User.objects.create_user(first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password
                    )
                    user.save()
                    return render(request, './pages/success.html')
    return render(request, './pages/index.html')


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
           auth.login(user)
           return render(request, './pages/success.html')
        else:
            return redirect('register')
    return render(request, './pages/login.html')