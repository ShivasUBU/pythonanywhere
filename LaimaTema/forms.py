from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50,)
    last_name = forms.CharField(max_length=50,)
    email = forms.EmailField(max_length=254,)
    phone = forms.CharField(max_length=10, min_length=9)
    address = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'email', 'address',)
