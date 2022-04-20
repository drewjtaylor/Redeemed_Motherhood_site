from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Client


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=100, help_text='Required. Inform a valid email address.')
    phone = forms.CharField(max_length=10, required=False, help_text='Enter your 10 digit phone number with no dashes or spaces')
    partner_name = forms.CharField(max_length=50, required=False, help_text='Enter your spouse/partner\'s name')
    partner_email = forms.CharField(max_length=50, required=False, help_text='Enter your spouse/partner\'s email')
    address = forms.CharField(max_length=50, required=False, help_text='Enter your street address')
    city = forms.CharField(max_length=50, required=False, help_text='Enter your city')
    state = forms.CharField(max_length=2, required=False, help_text='Enter your state abbreviation (i.e., \'FL\'')
    zip = forms.CharField(max_length=9, required=False, help_text='Enter your zip code')
    due_date = forms.DateField(required=False, help_text='Enter your due date')

    class Meta:
        model = Client
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'phone',
            'partner_name',
            'partner_email',
            'address',
            'city',
            'zip',
            'state',
            'due_date')