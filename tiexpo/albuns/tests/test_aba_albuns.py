import pytest
from django.urls import reverse
from model_mommy import mommy

from tiexpo.django_assertions import assert_contains
from tiexpo.albuns.models import Album


@pytest.fixture
def albuns(db):
    return mommy.make(Album, 2)


@pytest.fixture
def resp(client, albuns):
    resp = client.get(reverse('base:home'))
    return resp


def test_titulos_dos_albuns(resp, albuns):
    for album in albuns:
        assert_contains(resp, album.titulo)


def test_link_dos_albuns(resp, albuns):
    for album in albuns:
        assert_contains(resp, album.get_absolute_url())
