from django.contrib import admin
from tiexpo.albuns.models import Imagem, Album


@admin.register(Album)
class AdminAlbum(admin.ModelAdmin):
    list_display = ('titulo', )
    search_fields = ('titulo',)
    prepopulated_fields = {"slug": ("titulo",)}


@admin.register(Imagem)
class AdminImagem(admin.ModelAdmin):
    list_display = ('titulo', 'album', 'slug')
    list_filter = ['album']
    autocomplete_fields = ['album']
    prepopulated_fields = {"slug": ("titulo",)}
    ordering = ('data_publicacao',)
    search_fields = ('titulo', 'descricao',)
