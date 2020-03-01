from django.shortcuts import render
from tiexpo.albuns import facade


def indice(request):
    ctx = {'albuns': facade.listar_albuns_com_imagens()}
    return render(request, 'albuns/indice.html', ctx)


def detalhe(request, slug):
    album = facade.encontrar_album(slug)
    imagens = facade.listar_imagens_de_album_ordenadas(album)
    return render(request, 'albuns/album_detalhe.html', {'album': album, 'imagens': imagens})


def imagem(request, slug):
    imagem = facade.encontrar_imagem(slug)
    return render(request, 'albuns/imagem_detalhe.html', {'imagem': imagem})
