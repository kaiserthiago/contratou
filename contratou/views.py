from django.shortcuts import render


# Create your views here.
from contratou.models import Profissional


def home(request):
    return render(request, 'contratou/home.html', {})


def contato(request):
    return render(request, 'contratou/contato.html', {})


def profissionais(request):
    profissionais = Profissional.objects.all()

    context = {
        'profissionais': profissionais,
    }
    return render(request, 'contratou/profissionais.html', context)

def profissional_detalhe(request, profissional_id):
    profissionais = Profissional.objects.filter(pk=profissional_id)

    context = {
        'profissionais': profissionais,
    }
    return render(request, 'contratou/profissional_detalhe.html', context)

def sobre(request):
    return render(request, 'contratou/sobre.html', {})
