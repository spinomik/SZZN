from django import forms

class LoginUser(forms.Form):
    login = forms.CharField(label='Nazwa użytkownika')
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)