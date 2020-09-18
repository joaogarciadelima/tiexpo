import pytest
from django.urls import reverse

from tiexpo.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>TieExpo</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">Tiê Representações')


def test_footer_fone(resp):
    assert_contains(resp, '<a href="tel:+553732289500" class="text-light">+55 (37)3228-9500</a>')


def test_footer_email(resp):
    assert_contains(resp, '<a href="mailto:contato@tierepresentacoes.com.br" class="text-light">'
                          'contato@tierepresentacoes.com.br</a>')


def test_footer_privacy(resp):
    assert_contains(resp, f'<a href="{reverse("base:privacy")}" class="text-light">Política de Privacidade</a>')
