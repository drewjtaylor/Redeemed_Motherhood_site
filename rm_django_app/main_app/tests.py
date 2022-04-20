from django.test import TestCase
from django.test import Client
from django.urls import reverse

#Made a special kind of user called "client", not knowing there was a test client. The model, "Client", is userclient in these tests
from .models import Client as userclient

import pytest
from django.core import serializers
import json

# Create your tests here.

class UrlTests(TestCase):
    
    def test_home_page_with_no_url(self):
        client = Client()
        response = client.get('/')
        self.assertIs(response.status_code == 200, True)

    def test_signup_page(self):
        client = Client()
        response = client.get(reverse('main_app:signup'))
        self.assertIs(response.status_code == 200, True)


###Pytest tests created as part of Nucamp project
#Fixure client to be used for testing
@pytest.fixture
def client():
    fakeclient = userclient(
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
    assert userclient.objects.filter(username="fake_user")

@pytest.mark.django_db
def test_serialize_client(client):
    client.save()
    data = serializers.serialize('json', userclient.objects.filter(username="fake_user"))
    pydata = json.loads(data)
    assert 'fake_user' == (pydata[0]['fields']['username'])

