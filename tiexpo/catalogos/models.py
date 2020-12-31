from datetime import datetime

from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Catalogo(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('catalogos:detalhe', kwargs={'slug': self.slug})

    class Meta:
        ordering = ('titulo',)
        verbose_name = 'Catalogo'
        verbose_name_plural = 'Catalogos'


class Fabricante(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('catalogos:fabricantes', kwargs={'slug': self.slug})

    class Meta:
        ordering = ('nome',)
        verbose_name_plural = 'Fabricantes'


class Imagem(models.Model):
    class Meta:
        verbose_name_plural = 'Imagens'
        verbose_name = 'Imagem'
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='img/imagens')
    descricao = models.TextField(blank=True)
    catalogo = models.ForeignKey(Catalogo, related_name="imagens_catalogos", on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    data_publicacao = models.DateField(default=datetime.now)
    fabricante = models.ForeignKey(Fabricante, related_name="imagens_fabricantes", on_delete=models.CASCADE, null=True)
    destaque = models.BooleanField(verbose_name="Destaque", default=False)
    user_likes = models.ManyToManyField(get_user_model())

    def __str__(self):
        return self.titulo

    def number_of_likes(self):
        return self.user_likes.count()

    def get_absolute_url(self):
        return reverse('catalogos:imagem', kwargs={'slug': self.slug})
