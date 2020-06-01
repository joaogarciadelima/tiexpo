from django.contrib import admin
from tiexpo.fabricantes.models import Fabricante


@admin.register(Fabricante)
class AdminFabricante(admin.ModelAdmin):
    list_display = ('nome', )
    list_filter = ['nome']
    search_fields = ('nome',)
    ordering = ('nome',)
    prepopulated_fields = {"slug": ("nome",)}
