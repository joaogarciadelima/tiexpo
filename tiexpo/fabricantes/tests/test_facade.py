import pytest
from model_mommy import mommy

from tiexpo.fabricantes import facade
from tiexpo.fabricantes.models import Fabricante


@pytest.fixture
def fabricantes(db):
    return [mommy.make(Fabricante, nome=s) for s in 'Antes Depois'.split()]


def test_listar_fabricantes_ordenados(fabricantes):
    assert list(sorted(fabricantes, key=lambda fabricante: fabricante.nome)) == facade.listar_fabricantes_ordenados()


# @pytest.fixture
# def imagens(db):
#     return mommy.make(Imagem, 5)
