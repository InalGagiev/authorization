from msilib.schema import ListView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'account/login.html'

    def get_success_url(self):
        return reverse_lazy('main_str')

def account(request):
    return HttpResponse('это главная страница аккаунта')

def MainHome(request):
    return render(request, 'home.html')

def logout_user(request):
    logout(request)
    return redirect('main_str')


class SingUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/register.html'
