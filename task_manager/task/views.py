from django.shortcuts import render, redirect
from .forms import CreateUserforms, ProjectForm, TaskForm, AssignForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from task_app.models import Reporter, Reportee
from .models import *

# Create your views here.
def SignInView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            try:
                reporter = Reporter.objects.get(admin=user)
                context = {
                'msg': "I am a reporter"
                }
                return redirect('home')
            except Reporter.DoesNotExist as e:
                try:
                    reportee = Reportee.objects.get(Reportee=user)
                    context = {
                            'msg': "I am a reportee"
                    }
                    return redirect('home')
                except Reportee.DoesNotExist:
                    return redirect('question')
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


@login_required(login_url='/signin/')
def QuestionView(request):
    if request.method == "POST":
        flag = request.POST.get('flag')
        if flag == 'Reporter':
            Reporter.objects.create(admin=request.user)
            request.user.is_admin = True
            request.user.save()
            return render(request, 'home.html')
        else:
            Reportee.objects.create(Reportee=request.user)
            return render(request, 'home.html')
    return render(request, 'question.html')


@login_required(login_url='/signin/')
def HomeView(request):
    context = {
        'name': request.user
    }
    return render(request, 'home.html', context)


@login_required(login_url='/signin/')
def CreateProjectView(request):
    reporter = Reporter.objects.get(admin=request.user)
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            project = Project.objects.get(title=title)
            Project_Has_Reporter.objects.create(Project_Reporter=reporter, Project_Name = Project.objects.get(title=project))
            return redirect('home')
    context={
        'form': form
    }
    return render(request, 'create_project.html', context)

@login_required(login_url='/signin/')
def CreateTaskView(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form' : form
    }
    return render(request, 'create_task.html', context)

@login_required(login_url='/signin/')
def AssignTaskView(request):
    form = AssignForm()
    context = {
        'form' : form
    }
    return render(request, 'assign.html', context)

    
