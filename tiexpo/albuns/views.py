from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from tiexpo.albuns import facade


@login_required
def indice(request):
    ctx = {'albuns': facade.listar_albuns_com_imagens()}
    return render(request, 'albuns/indice.html', ctx)


@login_required
def detalhe(request, slug):
    album = facade.encontrar_album(slug)
    imagens = facade.listar_imagens_de_album_ordenadas(album)
    return render(request, 'albuns/imagens_por_album.html', {'album': album, 'imagens': imagens})


@login_required
def imagem(request, slug):
    imagem = facade.encontrar_imagem(slug)
    return render(request, 'albuns/imagem_detalhe.html', {'imagem': imagem})


@login_required
def imagens(request):
    imagens = {'imagens': facade.listar_todas_imagens()}
    return render(request, 'albuns/imagens.html', imagens)
