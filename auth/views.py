from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.shortcuts import render, redirect
from auth import forms
from django.contrib.auth import login

class Login(LoginView):
    template_name = 'auth/login.html'

class Logout(LogoutView):
    pass

class Signup(View):
    def get(self, request):
        context = {
            "form": forms.Signupform()
        }
        return render(request, 'auth/signup.html', context)
    
    def post(self, request):
        form  = forms.Signupform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
        context = {
            "form" : form
        }
        return render(request, 'auth/signup.html', context)
    
