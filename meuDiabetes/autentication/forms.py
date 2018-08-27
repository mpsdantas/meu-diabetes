from django import forms
from .models import Usuario

class CadastroForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        fields = ['nome','email','senha']

class LoginForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        fields = ['email','senha']