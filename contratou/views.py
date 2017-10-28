from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'contratou/home.html', {})


def contato(request):
    return render(request, 'contratou/contato.html', {})


def profissionais(request):
    return render(request, 'contratou/profissionais.html', {})

def sobre(request):
    return render(request, 'contratou/sobre.html', {})
