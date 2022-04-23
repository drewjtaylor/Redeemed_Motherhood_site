from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.contrib import auth

#Made a special kind of user called "client", not knowing there was a test client. The MODEL, "Client", is "userclient" in these tests
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

class UserTests(TestCase):
    def setUp(self):
        """
        Users are created with all fields, only required fields, and missing required fields.
        """
        userclient.objects.create(
            username='testuser', 
            password='12345',
            email='email@mailinator.com',
            phone='5559871234',
            partner_name='Joe Smith',
            partner_phone='5551234987',
            partner_email='jsmith@mailinator.com',
            address='123 Main Street',
            city='Tampa',
            zip='33478',
            state='FL',
            due_date='2022-05-21')
        
        userclient.objects.create(
            username='testuser_no_extra_fields', 
            password='12345',
            email='email@mailinator.com')

        userclient.objects.create(
            username='testuser_missed_required_fields')

    def test_was_user_created(self):
        testuser = userclient.objects.get(username='testuser')
        self.assertEqual(testuser.username, 'testuser')

    def test_new_user_required_fields_only(self):
        testuser = userclient.objects.get(username='testuser_no_extra_fields')
        self.assertEqual(testuser.username, 'testuser_no_extra_fields')

    def test_new_user_incomplete_fields(self):
        testuser = userclient.objects.get(username='testuser_missed_required_fields')
        print("last teset")
        self.assertNotEqual(testuser.username, 'testuser_missed_required_fields')


class NewEntryTests(TestCase):
    def test_new_video(self):
        pass
    
    def test_new_invoice(self):
        pass

    def test_new_provider(self):
        pass


###Pytest tests created as part of Nucamp project.  After making these and the django tests, I think I prefer the built-in Django tests.
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

