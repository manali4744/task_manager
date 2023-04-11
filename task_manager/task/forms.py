from django.contrib.auth.forms import UserCreationForm
from django import forms
from task_app.models import User

class CreateUserforms(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']