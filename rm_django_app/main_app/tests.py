from django.test import TestCase
from .models import Client
import pytest

# Create your tests here.

# @pytest.fixture
# def client():
#     return Client.objects.create(is_active=True)

# @pytest.mark.django_db
# def test_deactivate(client):
#     client.deactivate()
#     assert not client.is_active

# @pytest.mark.django_db
# def test_deactivate_reactivate(client):
#     client.deactivate()
#     client.activate()
#     assert client.is_active