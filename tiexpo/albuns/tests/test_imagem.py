# import pytest
# from django.urls import reverse
# from model_mommy import mommy
#
# from tiexpo.albuns.models import Imagem, Album
# from tiexpo.django_assertions import assert_contains
#
#
# @pytest.fixture
# def album(db):
#     return mommy.make(Album)
#
#
# @pytest.fixture
# def imagem(album):
#     return mommy.make(Imagem, album=album)
#
#
# @pytest.fixture
# def resp(client, imagem):
#     resp = client.get(reverse('albuns:imagem', kwargs={'slug': imagem.slug}))
#     return resp
#
#
# def test_imagem(resp, imagem: Imagem):
#     assert_contains(resp, f'<img src="{imagem.imagem.url}" class="img-fluid" alt="Responsive image">')
#
# #
