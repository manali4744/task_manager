from django.urls import path
from .views import SignInView, SignUpView, QuestionView, HomeView, CreateProjectView, CreateTaskView, AssignTaskView, ProgressView, DoneView, PriorityView

urlpatterns = [
    path('',SignInView, name='signin'), 
    path('signin/',SignInView, name='signin'), 
    path('signup/',SignUpView, name='signup'), 
    path('question/',QuestionView, name='question'),

    path('home/', HomeView, name='home'),
    path('createproject/', CreateProjectView, name='createproject'),   
    path('createtask/<str:pk>', CreateTaskView, name='createtask'),  
    path('assigntask/<str:pk>/<str:tk>', AssignTaskView, name='assigntask'),
    path('progress/<str:pk>', ProgressView, name='progress'),  
    path('done/<str:pk>', DoneView, name='done'), 
    path('priority/<str:pk>', PriorityView, name='priority'),  
]
