from django.test import TestCase
from .models import Client
import pytest
from django.core import serializers
import json

# Create your tests here.

#Fixure client to be used for testing
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

# Test to see if clients can be added to database
@pytest.mark.django_db
def test_add_client(client):
    client.save()
    assert Client.objects.filter(username="fake_user")

@pytest.mark.django_db
def test_serialize_client(client):
    client.save()
    data = serializers.serialize('json', Client.objects.filter(username="fake_user"))
    pydata = json.loads(data)
    assert 'fake_user' == (pydata[0]['fields']['username'])

