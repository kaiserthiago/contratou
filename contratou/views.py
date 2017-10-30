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

def sobre(request):
    return render(request, 'contratou/sobre.html', {})
