from django.contrib import admin

# Register your models here.
from contratou.models import Profissional, Contratante, Segmento, Area, Servico, AvaliacaoProfissional, \
    AvaliacaoContratante


class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'uf')
    list_filter = ['nome', 'cidade', 'uf', 'area']

class ContratanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'uf')
    list_filter = ['nome', 'cidade', 'uf']

class SegmentoAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    list_filter = ['descricao',]

class AreaAdmin(admin.ModelAdmin):
    list_display = ('segmento', 'descricao')
    list_filter = ['segmento', 'descricao']

admin.site.register(Profissional, ProfissionalAdmin)
admin.site.register(Contratante, ContratanteAdmin)
admin.site.register(Segmento, SegmentoAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Servico)
admin.site.register(AvaliacaoProfissional)
admin.site.register(AvaliacaoContratante)