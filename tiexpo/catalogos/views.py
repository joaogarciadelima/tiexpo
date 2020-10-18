from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from tiexpo.catalogos import facade


@login_required
def indice(request):
    ctx = {'catalogos': facade.listar_catalogos_com_imagens()}
    return render(request, 'catalogos/indice.html', ctx)


@login_required
def detalhe(request, slug):
    catalogo = facade.encontrar_catalogo(slug)
    imagens = facade.listar_imagens_de_catalogo_ordenadas(catalogo)
    return render(request, 'catalogos/imagens_por_album.html', {'catalogo': catalogo, 'imagens': imagens})


@login_required
def imagem(request, slug):
    imagem = facade.encontrar_imagem(slug)
    return render(request, 'catalogos/imagem_detalhe.html', {'imagem': imagem})


@login_required
def imagens(request):
    imagens = {'imagens': facade.listar_todas_imagens()}
    return render(request, 'catalogos/imagens.html', imagens)


@login_required
def procurar_imagens(request):
    search = request.GET.get('search')
    imagens = {'imagens': facade.listar_todas_imagens(search)}
    return render(request, 'catalogos/imagens.html', imagens)


@login_required
def indice_fabricantes(request):
    ctx = {'fabricantes': facade.listar_fabricantes_com_imagens()}
    return render(request, 'catalogos/indice_fabricantes.html', ctx)


@login_required
def detalhe_fabricante(request, slug):
    fabricante = facade.encontrar_fabricante(slug)
    imagens = facade.listar_imagens_de_fabricantes_ordenadas(fabricante)
    return render(request, 'catalogos/imagens_por_album.html', {'fabricante': fabricante, 'imagens': imagens})


@login_required
def imagem_fabricante(request, slug):
    imagem = facade.encontrar_imagem(slug)
    return render(request, 'fabricantes/imagem_detalhe.html', {'imagem': imagem})


@login_required
def imagens_destaques(request):
    imagens = {'imagens': facade.listar_destaques()}
    return render(request, 'catalogos/imagens.html', imagens)
