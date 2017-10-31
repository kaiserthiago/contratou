from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from contratou.models import Profissional


def login_view(request):
    next = request.GET.get('next', '/contratou/profissionais')
    if request.method == 'POST':
        user = authenticate(username=request.POST['nomeusuario'], password=request.POST['senha'])

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(next)
            # return redirect('contratou.home')

    return render(request, 'contratou/login.html', {})


def logout_view(request):
    logout(request)

    return redirect('contratou.home')


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
