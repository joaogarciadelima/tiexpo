import pytest
from django.urls import reverse
from model_mommy import mommy

from tiexpo.django_assertions import assert_contains
from tiexpo.albuns.models import Album, Imagem


@pytest.fixture
def album(db):
    return mommy.make(Album)


@pytest.fixture
def imagens(album):
    return mommy.make(Imagem, 3, album=album)


@pytest.fixture
def resp(client, album, imagens, django_user_model):
    user = mommy.make(django_user_model)
    client.force_login(user)
    resp = client.get(reverse('albuns:detalhe', kwargs={'slug': album.slug}))
    return resp


def test_titulos(resp, album: album):
    assert_contains(resp, album.titulo)


def test_status_code(resp):
    assert resp.status_code == 200


def test_imagens_titulos(resp, imagens):
    for aula in imagens:
        assert_contains(resp, aula.titulo)


def test_imagens_links(resp, imagens):
    for aula in imagens:
        assert_contains(resp, aula.get_absolute_url())
