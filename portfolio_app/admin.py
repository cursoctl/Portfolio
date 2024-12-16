from django.contrib import admin
from .models import Projeto, Experiencia

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'link')  # Campos que deseja exibir na lista
    search_fields = ('titulo',)  # Campos que permitem busca

class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_inicio', 'data_fim')
    search_fields = ('titulo',)
    list_filter = ('data_inicio', 'data_fim')  # Filtro por data

# Registrando com classes personalizadas
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Experiencia, ExperienciaAdmin)
