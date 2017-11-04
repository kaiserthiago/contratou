from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from contratou.models import Profissional, Contratante, Segmento, Area, Servico, AvaliacaoProfissional, \
    AvaliacaoContratante, UserProfile


class AvaliacaoContratanteAdmin(admin.ModelAdmin):
    list_display = ('contratante', 'servico', 'comentario')
    list_filter = ['servico']


class AvaliacaoProfissionalAdmin(admin.ModelAdmin):
    list_display = ('profissional', 'servico', 'comentario')
    list_filter = ['servico']


class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'uf')
    list_filter = ['nome', 'cidade', 'uf', 'area']


class ContratanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'uf')
    list_filter = ['nome', 'cidade', 'uf']


class SegmentoAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    list_filter = ['descricao', ]


class AreaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'segmento')
    list_filter = ['descricao', 'segmento']


class ServicoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'profissional', 'contratante', 'data')
    list_filter = ['profissional', 'contratante']


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profissional, ProfissionalAdmin)
admin.site.register(Contratante, ContratanteAdmin)
admin.site.register(Segmento, SegmentoAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(AvaliacaoProfissional, AvaliacaoProfissionalAdmin)
admin.site.register(AvaliacaoContratante, AvaliacaoContratanteAdmin)
