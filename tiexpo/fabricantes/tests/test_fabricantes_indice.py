# from typing import List

# import pytest
# from django.urls import reverse
# from model_mommy import mommy

# from tiexpo.fabricantes.models import Fabricante
# from tiexpo.django_assertions import assert_contains


# @pytest.fixture
# def fabricantes(db):
#     return mommy.make(Fabricante, 3)


# def test_status_code(resp):
#     assert resp.status_code == 200


# def test_indice_disponivel(resp):
#     assert resp.status_code == 200


# def test_titulos(resp, albuns: List[Album]):
#     for album in albuns:
#         assert_contains(resp, album.titulo)


# def test_imagens_titulos(resp, imagens: List[Imagem]):
#     for imagem in imagens:
#         assert_contains(resp, imagem.titulo)


# def test_imagens_urls(resp, imagens: List[Imagem]):
#     for imagem in imagens:
#         assert_contains(resp, imagem.get_absolute_url())
