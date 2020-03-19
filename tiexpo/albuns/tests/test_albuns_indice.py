from typing import List

import pytest
from django.urls import reverse
from model_mommy import mommy

from tiexpo.albuns.models import Imagem, Album
from tiexpo.django_assertions import assert_contains


@pytest.fixture
def albuns(db):
    return mommy.make(Album, 3)


@pytest.fixture
def imagens(albuns):
    imagens = []
    for album in albuns:
        imagens.extend(mommy.make(Imagem, 3, album=album))
    return imagens


@pytest.fixture
def resp(client, albuns, imagens, django_user_model):
    user = mommy.make(django_user_model)
    client.force_login(user)
    return client.get(reverse(
        'albuns:indice',),
        secure=True)


def test_status_code(resp):
    assert resp.status_code == 200


def test_indice_disponivel(resp):
    assert resp.status_code == 200


def test_titulos(resp, albuns: List[Album]):
    for album in albuns:
        assert_contains(resp, album.titulo)


def test_imagens_titulos(resp, imagens: List[Imagem]):
    for imagem in imagens:
        assert_contains(resp, imagem.titulo)


def test_imagens_urls(resp, imagens: List[Imagem]):
    for imagem in imagens:
        assert_contains(resp, imagem.get_absolute_url())
