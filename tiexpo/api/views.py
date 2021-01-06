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


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


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


# class ImageCalalogDetail(generics.ListAPIView):
#     """
#     Retrieve
#     """
#     def get_queryset(self):
#         try:
#             return Catalogo.objects.filter(pk=self.kwargs['pk'])
#         except Catalogo.DoesNotExist:
#             raise Http404
#
#     serializer_class = CatalogoImagensSerializer
#
#
# class ImageFabricanteDetail(generics.ListAPIView):
#     """
#     Retrieve
#     """
#     def get_queryset(self):
#         try:
#             return Fabricante.objects.filter(pk=self.kwargs['pk'])
#         except Catalogo.DoesNotExist:
#             raise Http404
#
#     serializer_class = FabricanteImagensSerializer
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


class ImageDestaquesList(generics.ListCreateAPIView):
    """[summary]

    Api para retornar as imagens em destaque no sistema

    Retrieve details of images

    """
    # permission_classes = [permissions.IsAuthenticated]
    search_fields = ['titulo', 'descricao', 'catalogo__titulo', 'fabricante__nome']
    filter_backends = [filters.SearchFilter]
    queryset = Imagem.objects.filter(destaque=True)
    serializer_class = ImagemSerializer

    # def get(self, request):
    #     imagens = Imagem.objects.filter(destaque=True)
    #     serializer = ImagemSerializer(imagens, many=True)
    #     return Response(serializer.data)


class LikeImage(APIView):
    """
    Like images
    """
    def get_object(self, pk):
        try:
            return Imagem.objects.get(pk=pk)
        except Imagem.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        imagem = self.get_object(pk)
        if imagem.user_likes.filter(id=request.user.id).exists():
            imagem.user_likes.remove(request.user.id)
        else:
            imagem.user_likes.add(request.user.id)
        imagem.save()
        serializer = ImagemSerializer(imagem)
        return Response(serializer.data)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
