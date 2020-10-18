from typing import List

import pytest
from django.urls import reverse
from model_bakery import baker

from tiexpo.catalogos.models import Imagem, Catalogo
from tiexpo.django_assertions import assert_contains


@pytest.fixture
def catalogos(db):
    return baker.make(Catalogo, 3)


@pytest.fixture
def imagens(catalogos):
    imagens = []
    for catalogo in catalogos:
        imagens.extend(baker.make(Imagem, 3, catalogo=catalogo))
    return imagens


@pytest.fixture
def resp(client, catalogos, imagens, django_user_model):
    user = baker.make(django_user_model)
    client.force_login(user)
    return client.get(reverse(
        'catalogos:indice',),
        secure=True)


def test_status_code(resp):
    assert resp.status_code == 200


def test_indice_disponivel(resp):
    assert resp.status_code == 200


def test_titulos(resp, catalogos: List[Catalogo]):
    for catalogo in catalogos:
        assert_contains(resp, catalogo.titulo)


def test_imagens_titulos(resp, imagens: List[Imagem]):
    for imagem in imagens:
        assert_contains(resp, imagem.titulo)


def test_imagens_urls(resp, imagens: List[Imagem]):
    for imagem in imagens:
        assert_contains(resp, imagem.get_absolute_url())
