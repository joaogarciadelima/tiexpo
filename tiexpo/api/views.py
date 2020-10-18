from django.http import Http404  # HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, filters
# from rest_framework.parsers import JSONParser
# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from tiexpo.api.serializers import CatalogoSerializer, FabricanteSerializer, ImagemSerializer
from tiexpo.api.serializers import CatalogoImagensSerializer, FabricanteImagensSerializer
from tiexpo.catalogos.models import Catalogo, Imagem, Fabricante


class CatalogoList(APIView):
    """[summary]

    Api para retornar os catálogos cadastrados no sistema

    Retrieve details of catalogs

    """
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Catalogo.objects.get(pk=pk)
        except Catalogo.DoesNotExist:
            raise Http404

    def get(self, request):
        catalogos = Catalogo.objects.all()
        serializer = CatalogoSerializer(catalogos, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = CatalogoSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FabricanteList(APIView):
    """[summary]

    Api para retornar os fabricantes cadastrados no sistema

    Retrieve details of manufacters

    """
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Fabricante.objects.get(pk=pk)
        except Fabricante.DoesNotExist:
            raise Http404

    def get(self, request):
        fabricantes = Fabricante.objects.all()
        serializer = FabricanteSerializer(fabricantes, many=True)
        return Response(serializer.data)


class ImageList(APIView):
    """[summary]

    Api para retornar as imagens cadastradas no sistema

    Retrieve details of images

    """
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        imagens = Imagem.objects.all()
        serializer = ImagemSerializer(imagens, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = ImagemSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageCalalogDetail(APIView):
    """
    Retrieve
    """
    def get_object(self, pk):
        try:
            return Catalogo.objects.get(pk=pk)
        except Catalogo.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        catalogo = self.get_object(pk)
        serializer = CatalogoImagensSerializer(instance=catalogo)
        return Response(serializer.data)


class ImageFabricanteDetail(APIView):
    """
    Retrieve
    """
    def get_object(self, pk):
        try:
            return Fabricante.objects.get(pk=pk)
        except Catalogo.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        fabricante = self.get_object(pk)
        serializer = FabricanteImagensSerializer(instance=fabricante)
        return Response(serializer.data)


class ImageDetail(APIView):
    """
    Retrieve, update or delete a image instance.
    """
    def get_object(self, pk):
        try:
            return Imagem.objects.get(pk=pk)
        except Imagem.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        imagem = self.get_object(pk)
        serializer = ImagemSerializer(imagem)
        return Response(serializer.data)

    # def put(self, request, pk, format=None):
    #     imagem = self.get_object(pk)
    #     serializer = ImagemSerializer(imagem, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     imagem = self.get_object(pk)
    #     imagem.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class ImageApiView(generics.ListCreateAPIView):
    search_fields = ['titulo', 'descricao', 'catalogo__titulo', 'fabricante__nome']
    filter_backends = [filters.SearchFilter]
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer


class ImageDestaquesList(APIView):
    """[summary]

    Api para retornar as imagens em destaque no sistema

    Retrieve details of images

    """
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        imagens = Imagem.objects.filter(destaque=True)
        serializer = ImagemSerializer(imagens, many=True)
        return Response(serializer.data)
