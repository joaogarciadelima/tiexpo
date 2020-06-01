from django.db import models
from django.urls import reverse


class Fabricante(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('fabricantes:detalhe', kwargs={'slug': self.slug})

    class Meta:
        ordering = ('nome',)
        verbose_name_plural = 'Fabricantes'
