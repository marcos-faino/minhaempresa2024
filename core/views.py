from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'index.html'


class Teste(TemplateView):
    template_name = 'teste.html'