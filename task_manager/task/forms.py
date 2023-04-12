from django.contrib.auth.forms import UserCreationForm
from django import forms
from task_app.models import User
from .models import Project, Task, Task_Has_Reportee

class CreateUserforms(UserCreationForm):
    name = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']

class ProjectForm(forms.ModelForm):
    title = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'placeholder': 'Project Title'}))
    detail = forms.CharField(max_length=1000,widget=forms.TextInput(attrs={'placeholder': 'Detail'}))
    class Meta:
        model = Project
        fields = ("title","detail")

class TaskForm(forms.ModelForm):
    task = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'placeholder': 'Task'}))
    task_description = forms.CharField(max_length=1000,widget=forms.TextInput(attrs={'placeholder': 'Task Description'}))
    class Meta:
        model = Task
        fields = ("task","task_description")

class AssignForm(forms.ModelForm):
    Project_info = forms.ChoiceField()
    Reportee = forms.ChoiceField()
    task = forms.ChoiceField()
    status = forms.ChoiceField()  
    class Meta:
        model = Task_Has_Reportee
        fields = ('Project_info', 'Reportee', 'task', 'status',)


