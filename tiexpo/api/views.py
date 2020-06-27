from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from tiexpo.catalogos.models import Catalogo, Imagem
from tiexpo.api.serializers import CatalogoSerializer, ImagemSerializer


@csrf_exempt
def catalogo_list(request):
    '''
    Lista todos os catalogos ou cria um novo
    :param request:
    :return:
    '''
    if request.method == 'GET':
        catalogos = Catalogo.objects.all()
        serializer = CatalogoSerializer(catalogos, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CatalogoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def imagem_list(request):
    '''
    Retrice all images of APP
    :param request:
    :return:
    '''
    if request.method == 'GET':
        imagens = Imagem.objects.all()
        serializer = ImagemSerializer(imagens, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ImagemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def imagem_detail(request, id):
    '''
    Retrieve, update or delete
    :param request:
    :param id:
    :return:
    '''
    try:
        imagem = Imagem.objects.get(id=id)
    except Imagem.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ImagemSerializer(imagem)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ImagemSerializer(imagem, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        imagem.delete()
        return HttpResponse(status=204)
