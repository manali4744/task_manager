from django.urls import path
from .views import SignInView, SignUpView

urlpatterns = [
    path('',SignInView, name='signin'), 
    path('signup/',SignUpView, name='signup'), 
]
