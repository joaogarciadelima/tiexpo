import pytest
from model_bakery import baker

from tiexpo.catalogos import facade
from tiexpo.catalogos.models import Catalogo, Imagem


@pytest.fixture
def catalogos(db):
    return [baker.make(Catalogo, titulo=s) for s in 'Antes Depois'.split()]


def test_listar_catalogos_ordenados(catalogos):
    assert list(sorted(catalogos, key=lambda catalogo: catalogo.titulo)) == facade.listar_catalogos_ordenados()


@pytest.fixture
def imagens(db):
    return baker.make(Imagem, 5)


def test_listar_todas_fotos(imagens):
    assert list(imagens) == facade.listar_todas_imagens()


def test_listar_destaques(imagens):
    assert list(imagens) == facade.listar_destaques(destaque=False)


def test_likes(imagens, usuario_logado):
    for imagem in imagens:
        assert imagem == facade.new_like(slug=imagem.slug, user=usuario_logado)
