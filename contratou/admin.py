from django.contrib import admin

# Register your models here.
from contratou.models import Profissional, Contratante, Segmento, Area, Servico, AvaliacaoProfissional, \
    AvaliacaoContratante


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


admin.site.register(Profissional, ProfissionalAdmin)
admin.site.register(Contratante, ContratanteAdmin)
admin.site.register(Segmento, SegmentoAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(AvaliacaoProfissional, AvaliacaoProfissionalAdmin)
admin.site.register(AvaliacaoContratante, AvaliacaoContratanteAdmin)
