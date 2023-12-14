from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreateUser

class Signin(CreateView):
    form_class = CreateUser
    success_url = reverse_lazy('home')
    template_name = 'registration/signin.html'