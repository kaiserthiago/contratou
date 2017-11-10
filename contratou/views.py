from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import algoliasearch_django as algoliasearch
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from contratou.forms import FormAvaliacaoProfissional
from contratou.models import Profissional, AvaliacaoProfissional, Segmento, Area


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


def avaliacao_profissional(request):
    if request.method == 'POST':
        # recebe os dados do form
        form = FormAvaliacaoProfissional(request.POST)

        # se o form for válido vai coloccar os dados no BD
        if form.is_valid():
            post = AvaliacaoProfissional()

            post.profissional = form.cleaned_data['profissional']
            post.contratante = request.user
            post.servico = form.cleaned_data['servico']
            post.data_servico = form.cleaned_data['data_servico']
            post.comentario = form.cleaned_data['comentario']
            post.campo1 = form.cleaned_data['campo1']
            post.campo2 = form.cleaned_data['campo2']
            post.campo3 = form.cleaned_data['campo3']
            post.campo4 = form.cleaned_data['campo4']
            post.campo5 = form.cleaned_data['campo5']
            post.save()

            return redirect('contratou.home')
    else:
        form = FormAvaliacaoProfissional()

    return render(request, 'contratou/avaliacao_profissional.html', {'form': form})


def home(request):
    return render(request, 'contratou/home.html', {})


def contato(request):
    return render(request, 'contratou/contato.html', {})


def profissionais(request, segmento_id):
    profissionais = Profissional.objects.filter(area__segmento=segmento_id)
    segmentos = Segmento.objects.all()

    context = {
        'segmentos': segmentos,
        'profissionais': profissionais,
    }
    return render(request, 'contratou/segmentos.html', context)

def segmentos(request):
    segmentos = Segmento.objects.all()

    context = {
        'segmentos': segmentos
    }

    return render(request, 'contratou/segmentos.html', context)

def profissional_detalhe(request, profissional_id):
    profissionais = Profissional.objects.filter(pk=profissional_id)
    avaliacao = AvaliacaoProfissional.objects.filter(profissional=profissional_id)

    context = {
        'profissionais': profissionais,
        'avaliacao': avaliacao,
    }
    return render(request, 'contratou/profissional_detalhe.html', context)


def sobre(request):
    return render(request, 'contratou/sobre.html', {})

def search(request):
    areas = Area.objects.all().order_by('descricao')
    qs = request.GET.get('qs', '')
    id_area = request.GET.get('area', '')
    page = request.GET.get('page', '0')

    results = None
    area_descricao = ''
    previous_page = ''
    next_page = ''

    if page:
        next_page = int(page) + 1
        previous_page = int(page) - 1

    if qs:
        params = {'hitsPerPage': 2, 'page': page}
        results = algoliasearch.raw_search(Profissional, qs, params)

    if id_area:
        area = get_object_or_404(Area, id=id_area)
        area_descricao = area.descricao
        results = Profissional.objects.filter(area=area).order_by('nome')

        paginator = Paginator(results, 5)
        page = request.GET.get('page', 1)

        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(paginator.num_pages)

    context = {
        'areas': areas,
        'results': results,
        'area_descricao': area_descricao,
        'qs': qs,
        'previous_page': previous_page,
        'next_page': next_page,
        'id_area': id_area,
    }

    return render(request, 'contratou/profissional_search.html', context)