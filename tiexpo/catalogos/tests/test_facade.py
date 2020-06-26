import pytest
from model_mommy import mommy

from tiexpo.catalogos import facade
from tiexpo.catalogos.models import Catalogo, Imagem


@pytest.fixture
def catalogos(db):
    return [mommy.make(Catalogo, titulo=s) for s in 'Antes Depois'.split()]


def test_listar_catalogos_ordenados(catalogos):
    assert list(sorted(catalogos, key=lambda catalogo: catalogo.titulo)) == facade.listar_catalogos_ordenados()


@pytest.fixture
def imagens(db):
    return mommy.make(Imagem, 5)


def test_listar_todas_fotos(imagens):
    assert list(imagens) == facade.listar_todas_imagens()
