from django.urls import path
from .views import SignInView, SignUpView, QuestionView, HomeView, CreateProjectView, CreateTaskView, AssignTaskView

urlpatterns = [
    path('',SignInView, name='signin'), 
    path('signin/',SignInView, name='signin'), 
    path('signup/',SignUpView, name='signup'), 
    path('question/',QuestionView, name='question'),

    path('home/', HomeView, name='home'),
    path('createproject/', CreateProjectView, name='createproject'),  
    path('createtask/', CreateTaskView, name='createtask'),  
    path('assigntask/', AssignTaskView, name='assigntask'),  
]
