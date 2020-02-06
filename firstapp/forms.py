from django import forms

class HouseForm(forms.Form):
    address = forms.CharField(label='Адрес')
    year = forms.IntegerField(label='Год постройки')
