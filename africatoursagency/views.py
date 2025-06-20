from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from .form import RegisterForm


# Create your views here.

def register_view(request):
    #check if the request is a POST request
    if request.method == "POST":
        form = RegisterForm(request.POST) 
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        redirect('home')
    else:
        form = RegisterForm()
        return render(request, 'tours/register.html', {'form': form})
    



def login_view(request):
    pass


def logout_view(request):
    pass


# home view
# using the decorator

@login_required
def home_view(request):
    pass
