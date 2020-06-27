from rest_framework import serializers
from tiexpo.catalogos.models import Imagem, Catalogo, Fabricante


class CatalogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo
        fields = ['id', 'titulo', 'slug']


class ImagemSerializer(serializers.ModelSerializer):
    catalogo = serializers.StringRelatedField(read_only=True)
    fabricante = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Imagem
        fields = ['id', 'titulo', 'imagem', 'descricao', 'catalogo', 'slug',
                  'data_publicacao', 'fabricante']


class FabricanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabricante
        fields = ['id', 'nome', 'marca']
