from typing import List

from django.db.models import Prefetch

from tiexpo.albuns.models import Album, Imagem


def listar_albuns_ordenados() -> List[Album]:
    '''
    Lista de todos os albuns cadastrados em ordem alfabética
    :return:
    '''
    return list(Album.objects.order_by('titulo').all())


def encontrar_album(slug: str) -> Album:
    return Album.objects.get(slug=slug)


def listar_imagens_de_album_ordenadas(album: Album):
    return list(album.imagem_set.order_by('titulo').all())


def encontrar_imagem(slug: str) -> Imagem:
    return Imagem.objects.select_related('album').get(slug=slug)


def listar_albuns_com_imagens():
    imagens_ordenadas = Imagem.objects.order_by('titulo')
    return Album.objects.order_by('titulo').prefetch_related(
        Prefetch('imagem_set', queryset=imagens_ordenadas, to_attr='imagens')
    ).all()


def listar_todas_imagens():
    return list(Imagem.objects.all())
