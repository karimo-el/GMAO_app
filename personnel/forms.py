from re import U
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import UserLoginFor
INTERESTS_CHOICES = (
        ('EXPLOITATION', 'EXPLOITATION'),
        ("SECURITE", 'SECURITE'),
        ('BDM', 'BDM'),
        ('ELECTRIQUE', 'ELECTRIQUE'),
        ('MECANIQUE', 'MECANIQUE'),
)
class CreationForm(UserCreationForm):
    email = forms.EmailField()
    choice_sevice = forms.ChoiceField(choices=INTERESTS_CHOICES)
    class Meta:
        model = User
        fields = ['username',  'email', "choice_sevice",'password1', 'password2']

# class LoginForm(UserLoginForm):
#     rest_connecté = forms.BooleanField()
    
#     class Meta:
#         model = User
#         fields= ['username', 'password', "rest_connecté"]