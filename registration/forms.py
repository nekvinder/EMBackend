from django import forms
from . models import Login

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Login
        fields = ('name','email','password','confirm_password')

    