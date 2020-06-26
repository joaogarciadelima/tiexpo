from typing import List

from django.db.models import Prefetch

from tiexpo.catalogos.models import Catalogo, Imagem, Fabricante


def listar_catalogos_ordenados() -> List[Catalogo]:
    '''
    Lista de todos os albuns cadastrados em ordem alfabética
    :return:
    '''
    return list(Catalogo.objects.order_by('titulo').all())


def encontrar_catalogo(slug: str) -> Catalogo:
    return Catalogo.objects.get(slug=slug)


def listar_imagens_de_catalogo_ordenadas(catalogo: Catalogo):
    return list(catalogo.imagem_set.order_by('titulo').all())


def encontrar_imagem(slug: str) -> Imagem:
    return Imagem.objects.select_related('catalogo').get(slug=slug)


def listar_catalogos_com_imagens():
    imagens_ordenadas = Imagem.objects.order_by('titulo')
    return Catalogo.objects.order_by('titulo').prefetch_related(
        Prefetch('imagem_set', queryset=imagens_ordenadas, to_attr='imagens')
    ).all()


def listar_todas_imagens():
    return list(Imagem.objects.all())


# fabricantes
def listar_fabricantes_ordenados() -> List[Fabricante]:
    '''
    Lista de todos os fabricantes cadastrados em ordem alfabética
    :return:
    '''
    return list(Fabricante.objects.order_by('nome').all())


def encontrar_fabricante(slug: str) -> Fabricante:
    return Fabricante.objects.get(slug=slug)


def listar_imagens_de_fabricantes_ordenadas(fabricante: Fabricante):
    return list(fabricante.imagem_set.order_by('fabricante').all())


def encontrar_imagem_fabricante(slug: str) -> Imagem:
    return Imagem.objects.select_related('fabricante').get(slug=slug)


def listar_fabricantes_com_imagens():
    imagens_ordenadas = Imagem.objects.order_by('titulo')
    return Fabricante.objects.order_by('nome').prefetch_related(
        Prefetch('imagem_set', queryset=imagens_ordenadas, to_attr='imagens')
    ).all()
