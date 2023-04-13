from django.shortcuts import render, redirect
from .forms import CreateUserforms, ProjectForm, TaskForm, AssignForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from task_app.models import Reporter, Reportee, User
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
    if request.user.is_admin == True:
        reporter = Reporter.objects.get(admin=request.user)
        project = Project_Has_Reporter.objects.get(Project_Reporter=reporter)
        context = {
        'project': project.Project_Name.all()
        }
    else:
        reportee = Reportee.objects.get(Reportee=request.user)
        my_task = Task_Has_Reportee.objects.filter(Reportee=reportee)
        context = {
            'my_task' : my_task
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
            print("here")
            reporter = Reporter.objects.get(admin=request.user)
            project = form.cleaned_data.get('title')
            title = Project.objects.get(title=project)
            project_has_task = Project_Has_Task.objects.create(project=title)
            print("hello")
            try:
                project_has_reporter = Project_Has_Reporter.objects.get(Project_Reporter=reporter)
                project_has_reporter.Project_Name.add(project_has_task)
                project_has_reporter.save()
            except Project_Has_Reporter.DoesNotExist as e:
                project_has_reporter = Project_Has_Reporter()
                project_has_reporter.Project_Reporter =  Reporter.objects.get(admin=request.user)
                project_has_reporter.save()
                project_has_reporter.Project_Name.add(project_has_task)
                project_has_reporter.save()           
            return redirect('home')
    context={
        'form': form
    }
    return render(request, 'create_project.html', context)

@login_required(login_url='/signin/')
def CreateTaskView(request, pk):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            project_has_task=Project_Has_Task.objects.get(id=pk)
            task = form.cleaned_data.get('task')
            new_task = Task.objects.get(task=task)
            project_has_task.task.add(new_task)
            return redirect('home')
    context = {
        'form' : form
    }
    return render(request, 'create_task.html', context)

@login_required(login_url='/signin/')
def AssignTaskView(request,pk, tk):
    # print(f"product id/{pk}/ task id {tk}")
    form = AssignForm()
    if request.method == 'POST':
        form = AssignForm(request.POST)
        if form.is_valid():
            reportee = form.cleaned_data.get('Reportee')
            user = User.objects.get(email=reportee)
            reporter = Reporter.objects.get(admin=request.user)
            reportee = Reportee.objects.get(Reportee=user)
            project = Project.objects.get(id=pk)
            task = Task.objects.get(id=tk)
            Task_Has_Reportee.objects.create(Project=project,Reporter=reporter, Reportee=reportee,task=task)
            return redirect('home')
    context = {
        'form' : form
    }
    return render(request, 'assign.html', context)


@login_required(login_url='/signin/')
def ProgressView(request, pk):
    data = Task_Has_Reportee.objects.get(id=pk)
    data.status = "In Progress"
    data.save()
    return redirect('home')

@login_required(login_url='/signin/')
def DoneView(request, pk):
    data = Task_Has_Reportee.objects.get(id=pk)
    data.status = "Done"
    data.save()
    return redirect('home')

    
