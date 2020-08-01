from django.http import Http404  # HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
# from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from tiexpo.api.serializers import CatalogoSerializer, ImagemSerializer
from tiexpo.catalogos.models import Catalogo, Imagem


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

    def get(self, request, format=None):
        catalogos = Catalogo.objects.all()
        serializer = CatalogoSerializer(catalogos, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = CatalogoSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageList(APIView):
    """[summary]

    Api para retornar as imagens cadastradas no sistema

    Retrieve details of images

    """
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        imagens = Imagem.objects.all()
        serializer = ImagemSerializer(imagens, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ImagemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

    def put(self, request, pk, format=None):
        imagem = self.get_object(pk)
        serializer = ImagemSerializer(imagem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        imagem = self.get_object(pk)
        imagem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
