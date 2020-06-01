from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from tiexpo.fabricantes import facade


@login_required
def indice(request):
    ctx = {'fabricantes': facade.listar_fabricantes_com_imagens()}
    return render(request, 'fabricantes/indice.html', ctx)


@login_required
def detalhe(request, slug):
    fabricante = facade.encontrar_fabricante(slug)
    imagens = facade.listar_imagens_de_fabricantes_ordenadas(fabricante)
    return render(request, 'fabricantes/imagens_por_fabricante.html', {'fabricante': fabricante, 'imagens': imagens})


@login_required
def imagem(request, slug):
    imagem = facade.encontrar_imagem(slug)
    return render(request, 'fabricantes/imagem_detalhe.html', {'imagem': imagem})
