from django.conf.urls import url

from contratou import views

urlpatterns = [
    url(r'^$', views.home, name='contratou.home'),


    url(r'^logout$', views.logout_view, name='contratou.logout'),

    url(r'^contato/$', views.contato, name='contratou.contato'),
    url(r'^segmentos/(?P<segmento_id>\d+)/profissionais$', views.profissionais, name='contratou.profissionais'),

    url(r'^segmentos/$', views.segmentos, name='contratou.segmentos'),

    url(r'^search/$', views.search, name='contratou.search'),


    url(r'^profissional/detalhe/(?P<profissional_id>\d+)/$', views.profissional_detalhe, name='contratou.profissional_detalhe'),
    url(r'^sobre/$', views.sobre, name='contratou.sobre'),

    url(r'^avaliacao_profissional$', views.avaliacao_profissional, name='contratou.avaliacao_profissional'),
]
