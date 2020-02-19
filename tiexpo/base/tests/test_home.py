import pytest
from django.urls import reverse

from tiexpo.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Tiexpo</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">Controle Dental')


def test_footer_fone(resp):
    assert_contains(resp, '<a href="tel:+5537988323652" class="text-light">+55 (37)98832-3652</a>')


def test_footer_email(resp):
    assert_contains(resp, '<a href="mailto:joaogarciadelimaneto@gmail.com" class="text-light">'
                          'joaogarciadelimaneto@gmail.com</a>')
