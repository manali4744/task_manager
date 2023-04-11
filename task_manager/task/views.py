from django.shortcuts import render, redirect
from .forms import CreateUserforms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def SignInView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return render(request,'home.html')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return render(request, 'signin.html')
    return render(request,'signin.html')

def SignUpView(request):
    form = CreateUserforms()
    if request.method == "POST":
        form = CreateUserforms(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            messages.success(request, 'Account was created for ' + username)
            print(messages)
            return redirect('signin')
    context = {'form': form}
    return render(request, 'signup.html', context)
    
