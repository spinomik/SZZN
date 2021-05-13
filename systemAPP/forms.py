from django import forms
import datetime


class LoginUser(forms.Form):
    login = forms.CharField(label='Nazwa użytkownika')
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)


class DeliveryForm(forms.Form):
    delivery_ID = forms.CharField(max_length=20, label="delivery iD")
    delivery_date = forms.DateField(initial=datetime.date.today)
    meal_name = forms.CharField()
    quantity = forms.IntegerField(max_value=200)