from rest_framework import serializers
from tiexpo.albuns.models import Imagem, Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'titulo', 'slug']


class ImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = ['id', 'titulo', 'imagem', 'descricao', 'album', 'slug', 'data_publicacao']
