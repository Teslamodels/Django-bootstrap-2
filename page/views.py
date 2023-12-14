from django.shortcuts import render
from django.views.generic import TemplateView

class Page(TemplateView):
    template_name = 'home.html'