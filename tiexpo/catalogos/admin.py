from django.contrib import admin
from tiexpo.catalogos.models import Imagem, Catalogo, Fabricante


@admin.register(Catalogo)
class AdminCatalogo(admin.ModelAdmin):
    list_display = ('titulo', )
    search_fields = ('titulo',)
    prepopulated_fields = {"slug": ("titulo",)}


@admin.register(Imagem)
class CatalogoImagem(admin.ModelAdmin):
    list_display = ('titulo', 'catalogo', 'slug', 'fabricante', 'destaque')
    list_filter = ['catalogo']
    autocomplete_fields = ['catalogo']
    prepopulated_fields = {"slug": ("titulo",)}
    ordering = ('data_publicacao',)
    search_fields = ('titulo', 'descricao', 'catalogo__titulo', 'fabricante__nome')
    exclude = ['user_likes']


@admin.register(Fabricante)
class AdminFabricante(admin.ModelAdmin):
    list_display = ('nome', )
    list_filter = ['nome']
    search_fields = ('nome',)
    ordering = ('nome',)
    prepopulated_fields = {"slug": ("nome",)}
