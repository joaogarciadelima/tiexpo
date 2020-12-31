from typing import List

from django.db.models import Prefetch

from tiexpo.catalogos.models import Catalogo, Fabricante, Imagem
from django.contrib.postgres.search import SearchVector


def listar_catalogos_ordenados() -> List[Catalogo]:
    '''
    Lista de todos os albuns cadastrados em ordem alfabética
    :return:
    '''
    return list(Catalogo.objects.order_by('titulo').all())


def encontrar_catalogo(slug: str) -> Catalogo:
    return Catalogo.objects.get(slug=slug)


def listar_imagens_de_catalogo_ordenadas(catalogo: Catalogo):
    return list(catalogo.imagens_catalogos.order_by('titulo').all())


def encontrar_imagem(slug: str) -> Imagem:
    return Imagem.objects.select_related('catalogo').get(slug=slug)


def listar_catalogos_com_imagens():
    imagens_ordenadas = Imagem.objects.order_by('titulo')
    return Catalogo.objects.order_by('titulo').prefetch_related(
        Prefetch('imagens_catalogos', queryset=imagens_ordenadas, to_attr='imagens')
    ).all()


def listar_todas_imagens(filter=None):
    if filter:
        return list(Imagem.objects.annotate(
            search=SearchVector('titulo', 'descricao', 'catalogo__titulo', 'fabricante__nome'),
            ).filter(search=filter))
    else:
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
    return list(fabricante.imagens_fabricantes.order_by('fabricante').all())


def encontrar_imagem_fabricante(slug: str) -> Imagem:
    return Imagem.objects.select_related('fabricante').get(slug=slug)


def listar_fabricantes_com_imagens():
    imagens_ordenadas = Imagem.objects.order_by('titulo')
    return Fabricante.objects.order_by('nome').prefetch_related(
        Prefetch('imagens_fabricantes', queryset=imagens_ordenadas, to_attr='imagens')
    ).all()


def listar_destaques(destaque=True):
    return list(Imagem.objects.filter(destaque=destaque))


def new_like(user, slug):
    imagem = Imagem.objects.get(slug=slug)
    if imagem.user_likes.filter(id=user.id).exists():
        imagem.user_likes.remove(user)
    else:
        imagem.user_likes.add(user)
    imagem.save()
    return imagem
