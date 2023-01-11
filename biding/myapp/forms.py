from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import bid


class bid_amount(forms.Form):
    bid_amount_field=forms.IntegerField()



class Myform(UserCreationForm):
    password2 = forms.CharField(label='Re-password',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email-id'}
