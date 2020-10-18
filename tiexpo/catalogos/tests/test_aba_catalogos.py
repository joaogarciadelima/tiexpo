import pytest
from django.urls import reverse
from model_bakery import baker

from tiexpo.django_assertions import assert_contains
from tiexpo.catalogos.models import Catalogo


@pytest.fixture
def catalogos(db):
    return baker.make(Catalogo, 2)


@pytest.fixture
def resp(client, catalogos):
    resp = client.get(reverse('base:home'))
    return resp


def test_titulos_dos_catalogos(resp, catalogos):
    for catalogo in catalogos:
        assert_contains(resp, catalogo.titulo)


def test_link_dos_catalogos(resp, catalogos):
    for catalogo in catalogos:
        assert_contains(resp, catalogo.get_absolute_url())
