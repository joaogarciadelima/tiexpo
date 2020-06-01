from typing import List

from django.db.models import Prefetch

from tiexpo.albuns.models import Imagem
from tiexpo.fabricantes.models import Fabricante


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


def encontrar_imagem(slug: str) -> Imagem:
    return Imagem.objects.select_related('fabricante').get(slug=slug)


def listar_fabricantes_com_imagens():
    imagens_ordenadas = Imagem.objects.order_by('titulo')
    return Fabricante.objects.order_by('nome').prefetch_related(
        Prefetch('imagem_set', queryset=imagens_ordenadas, to_attr='imagens')
    ).all()
