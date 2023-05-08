from django.shortcuts import render
from django.views.generic import ListView
from social import models
from django.contrib.auth.mixins import LoginRequiredMixin



class Wall(LoginRequiredMixin , ListView):
    queryset = models.Post.objects.all()
    context_object_name = "posts"
    template_name = 'social/wall.html'
    login_url = 'auth/login'
