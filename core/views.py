from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from core.models import Funcionario


class Home(TemplateView):
    template_name = 'index.html'

    # sobreescrevendo o contexto da página
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['funcionarios'] = Funcionario.objects.order_by('?').all()
        return contexto


class Teste(TemplateView):
    template_name = 'teste.html'