import pytest
from model_mommy import mommy

from tiexpo.albuns import facade
from tiexpo.albuns.models import Album


@pytest.fixture
def albuns(db):
    return [mommy.make(Album, titulo=s) for s in 'Antes Depois'.split()]


def test_listar_modulos_ordenados(albuns):
    assert list(sorted(albuns, key=lambda album: album.titulo)) == facade.listar_albuns_ordenados()
