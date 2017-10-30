from django.conf.urls import url

from contratou import views

urlpatterns = [
    url(r'^$', views.home, name='contratou.home'),
    url(r'^contato/$', views.contato, name='contratou.contato'),
    url(r'^profissionais/$', views.profissionais, name='contratou.profissionais'),
    url(r'^profissional/detalhe/(?P<profissional_id>\d+)/$', views.profissional_detalhe, name='contratou.profissional_detalhe'),
    url(r'^sobre/$', views.sobre, name='contratou.sobre'),
]
