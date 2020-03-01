from django.db import models
from django.urls import reverse
from datetime import datetime


class Album(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('albuns:detalhe', kwargs={'slug': self.slug})

    class Meta:
        ordering = ('titulo',)
        verbose_name_plural = 'Albuns'


class Imagem(models.Model):
    class Meta:
        verbose_name_plural = 'Imagens'
        verbose_name = 'Imagem'
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='img/imagens')
    descricao = models.TextField(blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    data_publicacao = models.DateField(default=datetime.now)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('albuns:imagem', kwargs={'slug': self.slug})

    # def get_exibicao(self):
    #     nome_arquivo = str(self.imagem)
    #     delimiter = nome_arquivo.find(".JPG")
    #     nome_arquivo = nome_arquivo[:delimiter] + ".500x500.jpg"
    #     return nome_arquivo
    #
    # def get_thumbnail(self):
    #     nome_arquivo = str(self.imagem)
    #     delimiter = nome_arquivo.find(".JPG")
    #     nome_arquivo = nome_arquivo[:delimiter] + ".125x125.jpg"
    #     return nome_arquivo
