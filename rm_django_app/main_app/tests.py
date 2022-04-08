from django.test import TestCase
from .models import Client
import pytest

# Create your tests here.

@pytest.fixture
def client():
    fakeclient = Client(
        password="das8d97a@##", 
        username="fake_user", 
        first_name="Andrea", 
        last_name="Taylor", 
        email="not_real@mailinator.com",
        is_staff=True,
        is_active=True, 
        phone="7275551234",
        partner_name="Andrew", 
        partner_email="husbando@mailinator.com",
    )
    return fakeclient

@pytest.mark.django_db
def test_add_client(client):
    client.save()
    assert Client.objects.filter(username="fake_user")